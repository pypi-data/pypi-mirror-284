"""MaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIAL_DATABASE = python_net_import("SMT.MastaAPI.Materials", "MaterialDatabase")

if TYPE_CHECKING:
    from mastapy.materials import _272
    from mastapy.shafts import _25
    from mastapy.gears.materials import _587, _589, _592, _593, _595, _596
    from mastapy.electric_machines import _1302, _1320, _1333
    from mastapy.cycloidal import _1475, _1482
    from mastapy.utility.databases import _1849, _1842


__docformat__ = "restructuredtext en"
__all__ = ("MaterialDatabase",)


Self = TypeVar("Self", bound="MaterialDatabase")
T = TypeVar("T", bound="_272.Material")


class MaterialDatabase(_1846.NamedDatabase[T]):
    """MaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MaterialDatabase")

    class _Cast_MaterialDatabase:
        """Special nested class for casting MaterialDatabase to subclasses."""

        def __init__(
            self: "MaterialDatabase._Cast_MaterialDatabase", parent: "MaterialDatabase"
        ):
            self._parent = parent

        @property
        def named_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1846.NamedDatabase":
            return self._parent._cast(_1846.NamedDatabase)

        @property
        def sql_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1849.SQLDatabase":
            pass

            from mastapy.utility.databases import _1849

            return self._parent._cast(_1849.SQLDatabase)

        @property
        def database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1842.Database":
            pass

            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.Database)

        @property
        def shaft_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_25.ShaftMaterialDatabase":
            from mastapy.shafts import _25

            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def bevel_gear_abstract_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_587.BevelGearAbstractMaterialDatabase":
            from mastapy.gears.materials import _587

            return self._parent._cast(_587.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_589.BevelGearISOMaterialDatabase":
            from mastapy.gears.materials import _589

            return self._parent._cast(_589.BevelGearISOMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_592.CylindricalGearAGMAMaterialDatabase":
            from mastapy.gears.materials import _592

            return self._parent._cast(_592.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_593.CylindricalGearISOMaterialDatabase":
            from mastapy.gears.materials import _593

            return self._parent._cast(_593.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_595.CylindricalGearMaterialDatabase":
            from mastapy.gears.materials import _595

            return self._parent._cast(_595.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_596.CylindricalGearPlasticMaterialDatabase":
            from mastapy.gears.materials import _596

            return self._parent._cast(_596.CylindricalGearPlasticMaterialDatabase)

        @property
        def magnet_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1302.MagnetMaterialDatabase":
            from mastapy.electric_machines import _1302

            return self._parent._cast(_1302.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1320.StatorRotorMaterialDatabase":
            from mastapy.electric_machines import _1320

            return self._parent._cast(_1320.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1333.WindingMaterialDatabase":
            from mastapy.electric_machines import _1333

            return self._parent._cast(_1333.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1475.CycloidalDiscMaterialDatabase":
            from mastapy.cycloidal import _1475

            return self._parent._cast(_1475.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1482.RingPinsMaterialDatabase":
            from mastapy.cycloidal import _1482

            return self._parent._cast(_1482.RingPinsMaterialDatabase)

        @property
        def material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "MaterialDatabase":
            return self._parent

        def __getattr__(self: "MaterialDatabase._Cast_MaterialDatabase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MaterialDatabase._Cast_MaterialDatabase":
        return self._Cast_MaterialDatabase(self)
