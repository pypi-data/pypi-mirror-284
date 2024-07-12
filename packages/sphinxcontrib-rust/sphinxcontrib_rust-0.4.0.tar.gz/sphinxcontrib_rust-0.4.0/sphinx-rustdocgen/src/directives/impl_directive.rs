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

//! Implementation of the ``rust:impl`` directive

use syn::{ItemImpl, Visibility};

use crate::directives::{
    extract_doc_from_attrs,
    Directive,
    DirectiveOption,
    DirectiveVisibility,
    IndexEntryType,
};
use crate::formats::{MdContent, MdDirective, RstContent, RstDirective};
use crate::nodes::{
    nodes_for_generics,
    nodes_for_path,
    nodes_for_type,
    nodes_for_where_clause,
    type_name,
    Node,
};

#[derive(Clone, Debug)]
pub(crate) struct ImplDirective {
    pub(crate) name: String,
    pub(crate) options: Vec<DirectiveOption>,
    pub(crate) content: Vec<String>,
    pub(crate) items: Vec<Directive>,
}

/// Generate docutils nodes for the impl block's signature.
fn nodes_for_impl(item: &ItemImpl) -> Vec<Node> {
    let mut nodes = vec![];
    if item.unsafety.is_some() {
        nodes.extend_from_slice(&[Node::Keyword("unsafe"), Node::Space]);
    }
    nodes.extend_from_slice(&[Node::Keyword("impl")]);
    nodes.extend(nodes_for_generics(&item.generics));
    nodes.push(Node::Space);
    if let Some((bang, path, _)) = &item.trait_ {
        if bang.is_some() {
            nodes.push(Node::Operator("!"));
        }
        nodes.extend(nodes_for_path(path));
        nodes.extend_from_slice(&[Node::Space, Node::Keyword("for"), Node::Space]);
    }
    nodes.extend(nodes_for_type(&item.self_ty));
    if let Some(wc) = &item.generics.where_clause {
        nodes.extend(nodes_for_where_clause(wc));
    }
    nodes
}

impl ImplDirective {
    const DIRECTIVE_NAME: &'static str = "impl";

    pub(crate) fn from_item(
        parent_path: &str,
        item: &ItemImpl,
        inherited_visibility: &Option<&Visibility>,
    ) -> Directive {
        let self_ty = type_name(&item.self_ty);
        let mut name = format!("{parent_path}::{self_ty}");

        let mut trait_name = String::new();
        if let Some((bang, path, _)) = &item.trait_ {
            if bang.is_some() {
                trait_name += "!";
            }
            trait_name += &*path.segments.last().unwrap().ident.to_string();
            name += "::";
            name += &*trait_name;
            trait_name += " for ";
        };

        let options = vec![
            DirectiveOption::Index(IndexEntryType::None),
            DirectiveOption::Vis(DirectiveVisibility::Pub),
            DirectiveOption::Layout(nodes_for_impl(item)),
            DirectiveOption::Toc(format!("impl {}{self_ty}", trait_name,)),
        ];

        let items = Directive::from_impl_items(&name, item.items.iter(), inherited_visibility);
        Directive::Impl(ImplDirective {
            name,
            options,
            content: extract_doc_from_attrs(&item.attrs),
            items,
        })
    }
}

impl RstDirective for ImplDirective {
    fn get_rst_text(self, level: usize, max_visibility: &DirectiveVisibility) -> Vec<String> {
        let content_indent = Self::make_content_indent(level + 1);

        let mut text =
            Self::make_rst_header(Self::DIRECTIVE_NAME, &self.name, &self.options, level);
        text.extend(self.content.get_rst_text(&content_indent));

        for item in self.items {
            text.extend(item.get_rst_text(level + 1, max_visibility))
        }

        text
    }
}

impl MdDirective for ImplDirective {
    fn get_md_text(self, fence_size: usize, max_visibility: &DirectiveVisibility) -> Vec<String> {
        let fence = Self::make_fence(fence_size);

        let mut text =
            Self::make_md_header(Self::DIRECTIVE_NAME, &self.name, &self.options, &fence);
        text.extend(self.content.get_md_text());

        for item in self.items {
            text.extend(item.get_md_text(fence_size - 1, max_visibility));
        }

        text.push(fence);
        text
    }

    fn fence_size(&self) -> usize {
        Self::calc_fence_size(&self.items)
    }
}
