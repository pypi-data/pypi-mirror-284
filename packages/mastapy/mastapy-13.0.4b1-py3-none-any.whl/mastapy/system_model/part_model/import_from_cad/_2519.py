"""CylindricalGearInPlanetarySetFromCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.import_from_cad import _2518
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_IN_PLANETARY_SET_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD",
    "CylindricalGearInPlanetarySetFromCAD",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.import_from_cad import (
        _2520,
        _2521,
        _2522,
        _2524,
        _2515,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearInPlanetarySetFromCAD",)


Self = TypeVar("Self", bound="CylindricalGearInPlanetarySetFromCAD")


class CylindricalGearInPlanetarySetFromCAD(_2518.CylindricalGearFromCAD):
    """CylindricalGearInPlanetarySetFromCAD

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_IN_PLANETARY_SET_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearInPlanetarySetFromCAD")

    class _Cast_CylindricalGearInPlanetarySetFromCAD:
        """Special nested class for casting CylindricalGearInPlanetarySetFromCAD to subclasses."""

        def __init__(
            self: "CylindricalGearInPlanetarySetFromCAD._Cast_CylindricalGearInPlanetarySetFromCAD",
            parent: "CylindricalGearInPlanetarySetFromCAD",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_from_cad(
            self: "CylindricalGearInPlanetarySetFromCAD._Cast_CylindricalGearInPlanetarySetFromCAD",
        ) -> "_2518.CylindricalGearFromCAD":
            return self._parent._cast(_2518.CylindricalGearFromCAD)

        @property
        def mountable_component_from_cad(
            self: "CylindricalGearInPlanetarySetFromCAD._Cast_CylindricalGearInPlanetarySetFromCAD",
        ) -> "_2524.MountableComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2524

            return self._parent._cast(_2524.MountableComponentFromCAD)

        @property
        def component_from_cad(
            self: "CylindricalGearInPlanetarySetFromCAD._Cast_CylindricalGearInPlanetarySetFromCAD",
        ) -> "_2515.ComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2515

            return self._parent._cast(_2515.ComponentFromCAD)

        @property
        def cylindrical_planet_gear_from_cad(
            self: "CylindricalGearInPlanetarySetFromCAD._Cast_CylindricalGearInPlanetarySetFromCAD",
        ) -> "_2520.CylindricalPlanetGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2520

            return self._parent._cast(_2520.CylindricalPlanetGearFromCAD)

        @property
        def cylindrical_ring_gear_from_cad(
            self: "CylindricalGearInPlanetarySetFromCAD._Cast_CylindricalGearInPlanetarySetFromCAD",
        ) -> "_2521.CylindricalRingGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2521

            return self._parent._cast(_2521.CylindricalRingGearFromCAD)

        @property
        def cylindrical_sun_gear_from_cad(
            self: "CylindricalGearInPlanetarySetFromCAD._Cast_CylindricalGearInPlanetarySetFromCAD",
        ) -> "_2522.CylindricalSunGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2522

            return self._parent._cast(_2522.CylindricalSunGearFromCAD)

        @property
        def cylindrical_gear_in_planetary_set_from_cad(
            self: "CylindricalGearInPlanetarySetFromCAD._Cast_CylindricalGearInPlanetarySetFromCAD",
        ) -> "CylindricalGearInPlanetarySetFromCAD":
            return self._parent

        def __getattr__(
            self: "CylindricalGearInPlanetarySetFromCAD._Cast_CylindricalGearInPlanetarySetFromCAD",
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
        self: Self, instance_to_wrap: "CylindricalGearInPlanetarySetFromCAD.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearInPlanetarySetFromCAD._Cast_CylindricalGearInPlanetarySetFromCAD":
        return self._Cast_CylindricalGearInPlanetarySetFromCAD(self)
