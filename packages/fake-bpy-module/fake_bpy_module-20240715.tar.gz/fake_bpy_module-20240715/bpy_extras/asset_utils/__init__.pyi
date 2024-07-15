"""
Helpers for asset management tasks.

"""

import typing
import collections.abc
import typing_extensions

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class AssetBrowserPanel:
    bl_space_type: typing.Any

    def asset_browser_panel_poll(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

class AssetMetaDataPanel:
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def poll(self, context):
        """

        :param context:
        """
        ...

class SpaceAssetInfo: ...
