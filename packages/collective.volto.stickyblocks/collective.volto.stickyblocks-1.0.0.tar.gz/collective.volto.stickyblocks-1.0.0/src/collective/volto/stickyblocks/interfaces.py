# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
import json

from plone.restapi.controlpanels.interfaces import IControlpanel
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema import SourceText

from collective.volto.stickyblocks import _


class ICollectiveVoltoStickyblocksLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IStickyBlocks(IControlpanel):
    sticky_blocks_configuration = SourceText(
        title=_(
            "sticky_blocks_label",
            default="Sticky Blocks Configuration",
        ),
        description="",
        required=True,
        default=json.dumps([{"rootPath": "/", "items": []}]),
    )
