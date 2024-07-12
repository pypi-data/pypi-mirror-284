// sphinxcontrib_rust - Sphinx extension for the Rust programming language
// Copyright (C) 2024  Munir Contractor
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.

//! Implementation of the ``rust:struct`` directive

use syn::{Fields, Generics, ItemStruct, ItemUnion, Variant, Visibility};

use crate::directives::variable_directive::VariableDirective;
use crate::directives::{
    extract_doc_from_attrs,
    Directive,
    DirectiveOption,
    DirectiveVisibility,
    IndexEntryType,
};
use crate::formats::{MdContent, MdDirective, RstContent, RstDirective};
use crate::nodes::{nodes_for_generics, nodes_for_type, nodes_for_where_clause, Node};
use crate::{check_visibility, visibility_to_inherit};

#[derive(Clone, Debug)]
pub(crate) struct StructDirective {
    pub(crate) name: String,
    pub(crate) options: Vec<DirectiveOption>,
    pub(crate) content: Vec<String>,
    pub(crate) fields: Vec<VariableDirective>,
}

macro_rules! make_nodes {
    ($ident:expr, $fields:expr, $generics:expr, $item_keyword:expr) => {{
        let mut nodes = if let Some(keyword) = $item_keyword {
            vec![
                Node::Keyword(keyword),
                Node::Space,
                Node::Name($ident.to_string()),
            ]
        }
        else {
            vec![Node::Name($ident.to_string())]
        };

        if let Some(generics) = $generics {
            nodes.extend(nodes_for_generics(generics));
        }

        if let Fields::Unnamed(fields) = &$fields {
            nodes.push(Node::Punctuation("("));
            for field in &fields.unnamed {
                nodes.extend(nodes_for_type(&field.ty));
                nodes.push(Node::Punctuation(", "));
            }
            nodes.pop();
            nodes.push(Node::Punctuation(")"));
        }

        if let Some(generics) = $generics {
            if let Some(wc) = &generics.where_clause {
                nodes.extend(nodes_for_where_clause(wc));
            }
        }

        nodes
    }};
}

impl StructDirective {
    const DIRECTIVE_NAME: &'static str = "struct";

    pub(crate) fn from_variant(
        parent_path: &str,
        variant: &Variant,
        inherited_visibility: &Option<&Visibility>,
    ) -> StructDirective {
        let name = format!("{}::{}", parent_path, variant.ident);

        let options = vec![
            DirectiveOption::Index(IndexEntryType::SubEntry),
            DirectiveOption::Vis(DirectiveVisibility::effective_visibility(
                &Visibility::Inherited,
                inherited_visibility,
            )),
            DirectiveOption::Toc(format!("{}", &variant.ident)),
            DirectiveOption::Layout(make_nodes!(
                variant.ident,
                variant.fields,
                None::<&Generics>,
                None
            )),
        ];

        let fields = VariableDirective::from_fields(
            &name,
            &variant.fields,
            inherited_visibility,
            IndexEntryType::None,
        );

        StructDirective {
            name,
            options,
            content: extract_doc_from_attrs(&variant.attrs),
            fields,
        }
    }

    pub(crate) fn from_item(
        parent_path: &str,
        item: &ItemStruct,
        inherited_visibility: &Option<&Visibility>,
    ) -> Directive {
        let name = format!("{}::{}", parent_path, item.ident);

        let options = vec![
            DirectiveOption::Index(IndexEntryType::WithSubEntries),
            DirectiveOption::Vis(DirectiveVisibility::effective_visibility(
                &item.vis,
                inherited_visibility,
            )),
            DirectiveOption::Toc(format!("struct {}", &item.ident)),
            DirectiveOption::Layout(make_nodes!(
                item.ident,
                item.fields,
                Some(&item.generics),
                Some(Self::DIRECTIVE_NAME)
            )),
        ];

        let fields = VariableDirective::from_fields(
            &name,
            &item.fields,
            &visibility_to_inherit!(item.vis, *inherited_visibility),
            IndexEntryType::SubEntry,
        );

        Directive::Struct(StructDirective {
            name,
            options,
            content: extract_doc_from_attrs(&item.attrs),
            fields,
        })
    }

    pub(crate) fn from_union(
        parent_path: &str,
        item: &ItemUnion,
        inherited_visibility: &Option<&Visibility>,
    ) -> Directive {
        let name = format!("{parent_path}::{}", item.ident);
        let fields = Fields::Named(item.fields.clone());

        let options = vec![
            DirectiveOption::Index(IndexEntryType::WithSubEntries),
            DirectiveOption::Vis(DirectiveVisibility::effective_visibility(
                &item.vis,
                inherited_visibility,
            )),
            DirectiveOption::Toc(format!("union {}", item.ident)),
            DirectiveOption::Layout(make_nodes!(
                item.ident,
                fields,
                Some(&item.generics),
                Some("union")
            )),
        ];

        let fields = VariableDirective::from_fields(
            &name,
            &fields,
            &visibility_to_inherit!(item.vis, *inherited_visibility),
            IndexEntryType::SubEntry,
        );

        Directive::Struct(StructDirective {
            name,
            options,
            content: extract_doc_from_attrs(&item.attrs),
            fields,
        })
    }
}

impl RstDirective for StructDirective {
    fn get_rst_text(self, level: usize, max_visibility: &DirectiveVisibility) -> Vec<String> {
        check_visibility!(self.options, max_visibility);
        let content_indent = Self::make_content_indent(level);

        let mut text =
            Self::make_rst_header(Self::DIRECTIVE_NAME, &self.name, &self.options, level);
        text.extend(self.content.get_rst_text(&content_indent));

        for field in self.fields {
            text.extend(field.get_rst_text(level + 1, max_visibility));
        }

        text
    }
}

impl MdDirective for StructDirective {
    fn get_md_text(self, fence_size: usize, max_visibility: &DirectiveVisibility) -> Vec<String> {
        check_visibility!(self.options, max_visibility);
        let fence = Self::make_fence(fence_size);

        let mut text =
            Self::make_md_header(Self::DIRECTIVE_NAME, &self.name, &self.options, &fence);
        text.extend(self.content.get_md_text());

        for field in self.fields {
            text.extend(field.get_md_text(fence_size - 1, max_visibility));
        }

        text.push(fence);
        text
    }

    // noinspection DuplicatedCode
    fn fence_size(&self) -> usize {
        match self.fields.iter().map(VariableDirective::fence_size).max() {
            Some(s) => s + 1,
            None => 3,
        }
    }
}
