import json

from plone import api
from plone.restapi.interfaces import IExpandableElement
from plone.restapi.serializer.converters import json_compatible
from plone.restapi.services import Service
from zope.component import adapter
from zope.interface import Interface, implementer

from collective.volto.stickyblocks.interfaces import IStickyBlocks


@implementer(IExpandableElement)
@adapter(Interface, Interface)
class StickyBlocks(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, expand=False):
        result = {
            "sticky-blocks": {
                "@id": "{}/@sticky-blocks".format(self.context.absolute_url())
            }
        }

        if not expand:
            return result

        result["sticky-blocks"] = self.get_sticky_blocks()

        return json_compatible(result)

    def get_sticky_blocks(self):
        """Get sticky blocks for the current context"""
        from functools import cmp_to_key

        context_path = "/" + "/".join(self.context.getPhysicalPath()[2:])

        matches = sorted(
            [i for i in self.get_config() if context_path.startswith(i["rootPath"])],
            key=cmp_to_key(lambda a, b: len(a) > len(b)),
        )

        return matches and matches[-1] or []

    def get_config(self):
        return json.loads(
            api.portal.get_registry_record(
                interface=IStickyBlocks,
                name="sticky_blocks_configuration",
                default="[]",
            )
        )


class StickyBlocksGet(Service):
    def reply(self):
        sticky_blocks = StickyBlocks(self.context, self.request)

        return sticky_blocks(expand=True)
