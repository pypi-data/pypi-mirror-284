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

use syn::{ItemUse, UseTree};

use crate::directives::{Directive, DirectiveVisibility, MdDirective, RstDirective};
use crate::formats::{MdOption, RstOption};

#[derive(Clone, Debug, Default)]
pub(crate) struct UsePath {
    pub(crate) path: Vec<String>,
    pub(crate) target: Option<String>,
}

impl RstOption for UsePath {
    fn get_rst_text(&self, indent: &str) -> Option<String> {
        let target = self.target.as_ref().unwrap_or(self.path.last().unwrap());
        Some(format!("{indent}:{target}: {}", self.path.join("::")))
    }
}

impl MdOption for UsePath {
    fn get_md_text(&self) -> Option<String> {
        let target = self.target.as_ref().unwrap_or(self.path.last().unwrap());
        Some(format!(":{target}: {}", self.path.join("::")))
    }
}

#[derive(Clone, Debug)]
pub(crate) struct UseDirective {
    pub(crate) paths: Vec<UsePath>,
}

impl UseDirective {
    pub(crate) fn from_item(parent_path: &str, item: &ItemUse) -> Directive {
        if !matches!(&item.tree, UseTree::Path(_)) {
            panic!("Expected UseTree to start with path");
        }

        // This is always the name of the crate being processed since the parent
        // path is either the crate name or the module path in which the use
        // statement appears. The module path will always begin with the crate
        // name.
        let crate_name = &parent_path[0..parent_path.find("::").unwrap_or(parent_path.len())];

        // Vec to hold use paths that are completely parsed out.
        let mut complete_paths = vec![];

        // Vec to hold use paths that are still being parsed out.
        // This is initialized with one empty path.
        let mut incomplete_paths = vec![UsePath::default()];

        // Stack of the items identified from the use paths.
        let mut item_stack = vec![&item.tree];

        while let Some(t) = item_stack.pop() {
            match t {
                UseTree::Path(p) => {
                    // Next ident from the path.
                    // Add this to the incomplete path at the top of the stack.

                    incomplete_paths
                        .last_mut()
                        .unwrap()
                        .path
                        .push(p.ident.to_string());
                    item_stack.push(&p.tree);
                }
                UseTree::Name(n) => {
                    // Imported a name. This completes the use path.

                    let mut use_path = incomplete_paths.pop().unwrap();
                    // Handle self imports
                    let name = n.ident.to_string();
                    if name == "self" {
                        use_path.target = Some(use_path.path.last().unwrap().clone())
                    }
                    else {
                        use_path.path.push(name.clone());
                        use_path.target = Some(name);
                    }
                    if use_path.path[0] == "crate" {
                        use_path.path[0] = crate_name.to_string();
                    }
                    complete_paths.push(use_path);
                }
                UseTree::Rename(r) => {
                    // Imported and renamed. This completes the use path.

                    let mut use_path = incomplete_paths.pop().unwrap();
                    // Handle self imports
                    let name = r.ident.to_string();
                    if name != "self" {
                        use_path.path.push(name);
                    }
                    use_path.target = Some(r.rename.to_string());
                    if use_path.path[0] == "crate" {
                        use_path.path[0] = crate_name.to_string();
                    }
                    complete_paths.push(use_path);
                }
                UseTree::Glob(_) => {
                    // Glob import. This completes the use path.
                    // Unsure what to do with the target here.

                    let mut use_path = incomplete_paths.pop().unwrap();
                    use_path.path.push(String::from("*"));
                    if use_path.path[0] == "crate" {
                        use_path.path[0] = crate_name.to_string();
                    }
                    complete_paths.push(use_path);
                }
                UseTree::Group(g) => {
                    // Group of imports within curly braces.
                    // Create a copy of the current path on the stack for each
                    // item of the group and add back to the incomplete paths.
                    // Add all items from the group to the stack. In the next
                    // iteration of the loop, the last item from the group is
                    // fetched and processed until it terminates, and then the
                    // next item from the group is processed.

                    let last = incomplete_paths.pop().unwrap();
                    for _ in 0..g.items.len() {
                        incomplete_paths.push(last.clone());
                    }
                    for item in &g.items {
                        item_stack.push(item);
                    }
                }
            }
        }
        Directive::Use(UseDirective {
            paths: complete_paths,
        })
    }
}

impl RstDirective for UseDirective {
    fn get_rst_text(self, level: usize, _: &DirectiveVisibility) -> Vec<String> {
        let mut text = Self::make_rst_header("use", "", &self.paths, level);
        text.push(String::new());

        text
    }
}

impl MdDirective for UseDirective {
    fn get_md_text(self, fence_size: usize, _: &DirectiveVisibility) -> Vec<String> {
        let fence = Self::make_fence(fence_size);
        let mut text = Self::make_md_header("use", "", &self.paths, &fence);
        text.push(fence);
        text
    }
}
