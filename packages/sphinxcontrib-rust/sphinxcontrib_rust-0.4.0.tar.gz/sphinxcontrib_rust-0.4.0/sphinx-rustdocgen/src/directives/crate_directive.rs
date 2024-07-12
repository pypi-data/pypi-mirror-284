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

//! Implementation of the ``rust:crate`` directive.

use syn::File;

use crate::directives::{
    extract_doc_from_attrs,
    order_items,
    Directive,
    DirectiveOption,
    IndexEntryType,
};
use crate::formats::{MdContent, MdDirective, RstContent, RstDirective};
use crate::DirectiveVisibility;

/// Struct to hold data required for documenting a crate.
#[derive(Clone, Debug)]
pub(crate) struct CrateDirective {
    /// The name of the crate.
    pub(crate) name: String,
    /// The options for the crate directive.
    pub(crate) options: Vec<DirectiveOption>,
    /// The docstring for the crate's lib.rs file.
    pub(crate) content: Vec<String>,
    /// The items within the crate's lib.rs file.
    pub(crate) items: Vec<Directive>,
}

impl CrateDirective {
    const DIRECTIVE_NAME: &'static str = "crate";

    /// Create a new ``CrateDirective`` for the crate from the source file.
    ///
    /// The generated documentation produces a :rst:dir:`rust:crate` directive.
    ///
    /// Args:
    ///     :crate_name: The name of the crate.
    ///     :ast: Reference to ``syn::File`` struct from parsing the
    ///         crate's ``lib.rs`` file.
    pub(crate) fn new(name: &str, ast: &File) -> CrateDirective {
        CrateDirective {
            name: name.to_string(),
            options: vec![DirectiveOption::Index(IndexEntryType::Normal)],
            content: extract_doc_from_attrs(&ast.attrs),
            items: Directive::from_items(name, ast.items.iter(), &None),
        }
    }
}

impl RstDirective for CrateDirective {
    // noinspection DuplicatedCode
    fn get_rst_text(self, level: usize, max_visibility: &DirectiveVisibility) -> Vec<String> {
        // Do not filter for visibility here. Crates are always documented.
        let content_indent = Self::make_content_indent(level);

        // Get the text for the module
        let mut text =
            Self::make_rst_header(Self::DIRECTIVE_NAME, &self.name, &self.options, level);
        text.extend(self.content.get_rst_text(&content_indent));

        let (toc_tree_modules, ordered_items, uses) = order_items(self.items);

        for use_ in uses {
            text.extend(use_.get_rst_text(level + 1, max_visibility));
        }

        text.extend(Self::make_rst_toctree(
            &content_indent,
            "Modules",
            Some(1),
            toc_tree_modules.iter().map(|m| m.ident.as_str()),
        ));

        for (name, items) in ordered_items {
            text.extend(Self::make_rst_section(name, level, items, max_visibility));
        }

        text
    }
}

impl MdDirective for CrateDirective {
    // noinspection DuplicatedCode
    fn get_md_text(self, fence_size: usize, max_visibility: &DirectiveVisibility) -> Vec<String> {
        // Do not filter for visibility here. Crates are always documented.
        let fence = Self::make_fence(fence_size);

        // Get the text for the module
        let mut text =
            Self::make_md_header(Self::DIRECTIVE_NAME, &self.name, &self.options, &fence);
        text.extend(self.content.get_md_text());

        let (toc_tree_modules, ordered_items, uses) = order_items(self.items);

        for use_ in uses {
            text.extend(use_.get_md_text(3, max_visibility));
        }

        text.extend(Self::make_md_toctree(
            3,
            "Modules",
            Some(1),
            toc_tree_modules.iter().map(|m| m.ident.as_str()),
        ));

        for (name, items) in ordered_items {
            text.extend(Self::make_md_section(
                name,
                fence_size,
                items,
                max_visibility,
            ));
        }

        text
    }

    fn fence_size(&self) -> usize {
        Self::calc_fence_size(&self.items)
    }
}
