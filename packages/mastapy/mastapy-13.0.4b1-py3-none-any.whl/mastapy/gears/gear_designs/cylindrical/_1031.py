"""CylindricalGearMicroGeometrySettingsDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "CylindricalGearMicroGeometrySettingsDatabase",
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1849, _1842


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMicroGeometrySettingsDatabase",)


Self = TypeVar("Self", bound="CylindricalGearMicroGeometrySettingsDatabase")


class CylindricalGearMicroGeometrySettingsDatabase(
    _1846.NamedDatabase["_1032.CylindricalGearMicroGeometrySettingsItem"]
):
    """CylindricalGearMicroGeometrySettingsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMicroGeometrySettingsDatabase"
    )

    class _Cast_CylindricalGearMicroGeometrySettingsDatabase:
        """Special nested class for casting CylindricalGearMicroGeometrySettingsDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase",
            parent: "CylindricalGearMicroGeometrySettingsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase",
        ) -> "_1846.NamedDatabase":
            return self._parent._cast(_1846.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase",
        ) -> "_1849.SQLDatabase":
            pass

            from mastapy.utility.databases import _1849

            return self._parent._cast(_1849.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase",
        ) -> "_1842.Database":
            pass

            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.Database)

        @property
        def cylindrical_gear_micro_geometry_settings_database(
            self: "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase",
        ) -> "CylindricalGearMicroGeometrySettingsDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "CylindricalGearMicroGeometrySettingsDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase":
        return self._Cast_CylindricalGearMicroGeometrySettingsDatabase(self)
