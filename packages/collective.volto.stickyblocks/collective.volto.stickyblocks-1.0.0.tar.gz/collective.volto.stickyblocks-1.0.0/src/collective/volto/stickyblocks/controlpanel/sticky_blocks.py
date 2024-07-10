from plone.app.registry.browser import controlpanel

from collective.volto.stickyblocks import _
from collective.volto.stickyblocks.interfaces import IStickyBlocks


class StickyBlocksForm(controlpanel.RegistryEditForm):
    schema = IStickyBlocks
    label = _("sticky_blocks_settings_label", default="Sticky Blocks Settings")
    description = ""


class StickyBlocks(controlpanel.ControlPanelFormWrapper):
    form = StickyBlocksForm
