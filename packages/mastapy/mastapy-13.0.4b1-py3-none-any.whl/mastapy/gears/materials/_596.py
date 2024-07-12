"""CylindricalGearPlasticMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.materials import _595
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PLASTIC_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "CylindricalGearPlasticMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.materials import _273
    from mastapy.utility.databases import _1846, _1849, _1842


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearPlasticMaterialDatabase",)


Self = TypeVar("Self", bound="CylindricalGearPlasticMaterialDatabase")


class CylindricalGearPlasticMaterialDatabase(
    _595.CylindricalGearMaterialDatabase["_606.PlasticCylindricalGearMaterial"]
):
    """CylindricalGearPlasticMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PLASTIC_MATERIAL_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearPlasticMaterialDatabase"
    )

    class _Cast_CylindricalGearPlasticMaterialDatabase:
        """Special nested class for casting CylindricalGearPlasticMaterialDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
            parent: "CylindricalGearPlasticMaterialDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_material_database(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
        ) -> "_595.CylindricalGearMaterialDatabase":
            return self._parent._cast(_595.CylindricalGearMaterialDatabase)

        @property
        def material_database(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
        ) -> "_273.MaterialDatabase":
            from mastapy.materials import _273

            return self._parent._cast(_273.MaterialDatabase)

        @property
        def named_database(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
        ) -> "_1846.NamedDatabase":
            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
        ) -> "_1849.SQLDatabase":
            pass

            from mastapy.utility.databases import _1849

            return self._parent._cast(_1849.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
        ) -> "_1842.Database":
            pass

            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.Database)

        @property
        def cylindrical_gear_plastic_material_database(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
        ) -> "CylindricalGearPlasticMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
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
        self: Self, instance_to_wrap: "CylindricalGearPlasticMaterialDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase":
        return self._Cast_CylindricalGearPlasticMaterialDatabase(self)
