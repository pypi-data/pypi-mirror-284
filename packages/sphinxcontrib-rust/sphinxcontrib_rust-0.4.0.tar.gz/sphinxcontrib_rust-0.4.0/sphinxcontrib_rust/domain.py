# sphinxcontrib_rust - Sphinx extension for the Rust programming language
# Copyright (C) 2024  Munir Contractor
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""" Module for the ``rust`` Sphinx domain for documentation Rust items """

from collections import defaultdict
from typing import Optional, Type, Union, Iterable

from docutils.nodes import Element
from docutils.parsers.rst import Directive
from sphinx.addnodes import pending_xref
from sphinx.builders import Builder
from sphinx.domains import Domain, Index, ObjType
from sphinx.environment import BuildEnvironment
from sphinx.roles import XRefRole
from sphinx.util import logging
from sphinx.util.nodes import make_refnode
from sphinx.util.typing import RoleFunction

from sphinxcontrib_rust.directives import RustDirective
from sphinxcontrib_rust.index import RustIndex
from sphinxcontrib_rust.items import RustItem, RustItemType

LOGGER = logging.getLogger(__name__)


class RustXRefRole(XRefRole):
    """An :py:class:`XRefRole` extension for Rust roles"""

    def process_link(
        self,
        env: BuildEnvironment,
        refnode: Element,
        has_explicit_title: bool,
        title: str,
        target: str,
    ) -> tuple[str, str]:
        """Process the link by parsing the tile and the target"""
        # pylint: disable=too-many-arguments
        if not has_explicit_title:
            # This is the most common case where
            # only the target is specified as the title like
            # `` :rust:struct:`~crate::module::Struct` ``
            # title == target in this case

            # Remove any leading or trailing ::s.
            # Only meaningful for targets, once support
            # for relative references is added.
            title = title.strip("::")

            # Remove the ~ from the target, only meaningful for titles.
            target = target.lstrip("~")

            # ~ will use only the final part of the name as the title
            # instead of the full path.
            if title[0:1] == "~":
                _, _, title = title[1:].rpartition("::")

        return title, target


class RustDomain(Domain):
    """The Sphinx domain for the Rust programming language.

    The domain provides the various roles and directives that can be used in the Sphinx
    documentation for linking with Rust code.
    """

    name = "rust"
    label = "Rust"

    # The various object types provided by the domain
    object_types: dict[str, ObjType] = {
        t.value: t.get_sphinx_obj_type() for t in RustItemType
    }

    # The various directives add to Sphinx for documenting the Rust object types
    directives: dict[str, Type[Directive]] = {
        t.value: d for t, d in RustDirective.get_directives().items()
    }

    # The various roles added to Sphinx for referencing the Rust object types
    roles: dict[str, Union[RoleFunction, XRefRole]] = {
        r: RustXRefRole() for _, r in RustItemType.iter_roles()
    }

    # The indices for all the object types
    indices: list[Type[Index]] = [RustIndex]

    # The domain data created by Sphinx. This is here just for type annotation.
    data: dict[str, dict[RustItemType, list[RustItem]] | dict[str, dict[str, str]]]

    # Initial data for the domain, gets copied as self.data by Sphinx
    initial_data: dict[RustItemType, list[RustItem]] = {
        "items": {t: [] for t in RustItemType if t != RustItemType.USE},
        "uses": defaultdict(dict),
    }

    # Bump this when the data format changes.
    data_version = 0

    @property
    def items(self) -> dict[RustItemType, list[RustItem]]:
        """Return the Rust items with in the documentation"""
        return self.data["items"]

    @property
    def uses(self) -> dict[str, dict[str, str]]:
        """Return the dict of use statements per document within the documentation"""
        return self.data["uses"]

    def get_objects(self) -> Iterable[tuple[str, str, str, str, str, int]]:
        for _, objs in self.items.items():
            for obj in objs:
                yield (
                    obj.name,
                    obj.display_text,
                    obj.type_.value,
                    obj.docname,
                    obj.anchor,
                    obj.priority,
                )

    def clear_doc(self, docname: str) -> None:
        for typ, objs in self.items.items():
            if isinstance(typ, RustItemType):
                self.items[typ][:] = [o for o in objs if o.docname != docname]

    def _find_match(self, target: str, typ: str | None = None) -> Optional[RustItem]:
        search_types = [RustItemType.from_str(typ)] if typ else self.items.keys()

        matches = set()
        for search_type in search_types:
            matches.update(o for o in self.items[search_type] if o.name == target)

        # No match, return None
        if not matches:
            return None

        # Just 1 match, return it.
        if len(matches) == 1:
            return list(matches)[0]

        # Multiple matches, prefer a match that is not an impl.
        # This is likely to happen with a ref that matches a struct and the impl.
        for match in matches:
            if match.type_ != RustItemType.IMPL:
                return match

        # Return the first one if everything is an impl.
        return list(matches)[0]

    def resolve_xref(
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        typ: str,
        target: str,
        node: pending_xref,
        contnode: Element,
    ) -> Element | None:
        """Resolve a reference to a Rust item with the directive type specified"""
        # pylint:disable=too-many-arguments
        match = self._find_match(target, typ)
        return (
            make_refnode(
                builder,
                fromdocname,
                match.docname,
                match.name.replace("::", "-"),
                [contnode],
                match.name,
            )
            if match
            else None
        )

    def resolve_any_xref(
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        target: str,
        node: pending_xref,
        contnode: Element,
    ) -> list[tuple[str, Element]]:
        """Resolve a reference to a Rust item with an unspecified directive type"""
        # pylint:disable=too-many-arguments
        match = self._find_match(target)
        return (
            make_refnode(
                builder,
                fromdocname,
                match.docname,
                match.name.replace("::", "-"),
                [contnode],
                match.name,
            )
            if match
            else None
        )

    def merge_domaindata(self, docnames: list[str], otherdata: dict) -> None:
        for typ, objs in otherdata["items"].items():
            self.items[typ].extend(o for o in objs if o.docname in docnames)
        for doc, uses in otherdata["uses"].items():
            self.uses[doc].update(uses)
