"""DatabaseKey"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATABASE_KEY = python_net_import("SMT.MastaAPI.Utility.Databases", "DatabaseKey")

if TYPE_CHECKING:
    from mastapy.utility.scripting import _1758
    from mastapy.utility.report import _1786
    from mastapy.utility.databases import _1848
    from mastapy.bearings import _1914


__docformat__ = "restructuredtext en"
__all__ = ("DatabaseKey",)


Self = TypeVar("Self", bound="DatabaseKey")


class DatabaseKey(_0.APIBase):
    """DatabaseKey

    This is a mastapy class.
    """

    TYPE = _DATABASE_KEY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatabaseKey")

    class _Cast_DatabaseKey:
        """Special nested class for casting DatabaseKey to subclasses."""

        def __init__(self: "DatabaseKey._Cast_DatabaseKey", parent: "DatabaseKey"):
            self._parent = parent

        @property
        def user_defined_property_key(
            self: "DatabaseKey._Cast_DatabaseKey",
        ) -> "_1758.UserDefinedPropertyKey":
            from mastapy.utility.scripting import _1758

            return self._parent._cast(_1758.UserDefinedPropertyKey)

        @property
        def custom_report_key(
            self: "DatabaseKey._Cast_DatabaseKey",
        ) -> "_1786.CustomReportKey":
            from mastapy.utility.report import _1786

            return self._parent._cast(_1786.CustomReportKey)

        @property
        def named_key(self: "DatabaseKey._Cast_DatabaseKey") -> "_1848.NamedKey":
            from mastapy.utility.databases import _1848

            return self._parent._cast(_1848.NamedKey)

        @property
        def rolling_bearing_key(
            self: "DatabaseKey._Cast_DatabaseKey",
        ) -> "_1914.RollingBearingKey":
            from mastapy.bearings import _1914

            return self._parent._cast(_1914.RollingBearingKey)

        @property
        def database_key(self: "DatabaseKey._Cast_DatabaseKey") -> "DatabaseKey":
            return self._parent

        def __getattr__(self: "DatabaseKey._Cast_DatabaseKey", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatabaseKey.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DatabaseKey._Cast_DatabaseKey":
        return self._Cast_DatabaseKey(self)
