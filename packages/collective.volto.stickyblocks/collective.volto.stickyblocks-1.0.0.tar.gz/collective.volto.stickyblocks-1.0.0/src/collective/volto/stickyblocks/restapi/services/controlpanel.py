# -*- coding: utf-8 -*-
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import Interface, implementer

from collective.volto.stickyblocks.interfaces import (
    ICollectiveVoltoStickyblocksLayer,
    IStickyBlocks,
)


@adapter(Interface, ICollectiveVoltoStickyblocksLayer)
@implementer(IStickyBlocks)
class StickyBlocksControlpanel(RegistryConfigletPanel):
    schema = IStickyBlocks
    configlet_id = "StickyBlocks"
    configlet_category_id = "Products"
    schema_prefix = None
