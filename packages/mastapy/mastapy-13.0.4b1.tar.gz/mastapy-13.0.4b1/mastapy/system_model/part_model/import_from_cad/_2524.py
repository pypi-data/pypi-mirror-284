"""MountableComponentFromCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.import_from_cad import _2515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "MountableComponentFromCAD"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.import_from_cad import (
        _2514,
        _2516,
        _2517,
        _2518,
        _2519,
        _2520,
        _2521,
        _2522,
        _2526,
        _2527,
        _2528,
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentFromCAD",)


Self = TypeVar("Self", bound="MountableComponentFromCAD")


class MountableComponentFromCAD(_2515.ComponentFromCAD):
    """MountableComponentFromCAD

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentFromCAD")

    class _Cast_MountableComponentFromCAD:
        """Special nested class for casting MountableComponentFromCAD to subclasses."""

        def __init__(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
            parent: "MountableComponentFromCAD",
        ):
            self._parent = parent

        @property
        def component_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "_2515.ComponentFromCAD":
            return self._parent._cast(_2515.ComponentFromCAD)

        @property
        def clutch_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "_2514.ClutchFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2514

            return self._parent._cast(_2514.ClutchFromCAD)

        @property
        def concept_bearing_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "_2516.ConceptBearingFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2516

            return self._parent._cast(_2516.ConceptBearingFromCAD)

        @property
        def connector_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "_2517.ConnectorFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2517

            return self._parent._cast(_2517.ConnectorFromCAD)

        @property
        def cylindrical_gear_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "_2518.CylindricalGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2518

            return self._parent._cast(_2518.CylindricalGearFromCAD)

        @property
        def cylindrical_gear_in_planetary_set_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "_2519.CylindricalGearInPlanetarySetFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2519

            return self._parent._cast(_2519.CylindricalGearInPlanetarySetFromCAD)

        @property
        def cylindrical_planet_gear_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "_2520.CylindricalPlanetGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2520

            return self._parent._cast(_2520.CylindricalPlanetGearFromCAD)

        @property
        def cylindrical_ring_gear_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "_2521.CylindricalRingGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2521

            return self._parent._cast(_2521.CylindricalRingGearFromCAD)

        @property
        def cylindrical_sun_gear_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "_2522.CylindricalSunGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2522

            return self._parent._cast(_2522.CylindricalSunGearFromCAD)

        @property
        def pulley_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "_2526.PulleyFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2526

            return self._parent._cast(_2526.PulleyFromCAD)

        @property
        def rigid_connector_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "_2527.RigidConnectorFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2527

            return self._parent._cast(_2527.RigidConnectorFromCAD)

        @property
        def rolling_bearing_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "_2528.RollingBearingFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2528

            return self._parent._cast(_2528.RollingBearingFromCAD)

        @property
        def mountable_component_from_cad(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD",
        ) -> "MountableComponentFromCAD":
            return self._parent

        def __getattr__(
            self: "MountableComponentFromCAD._Cast_MountableComponentFromCAD", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponentFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    @enforce_parameter_types
    def offset(self: Self, value: "float"):
        self.wrapped.Offset = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentFromCAD._Cast_MountableComponentFromCAD":
        return self._Cast_MountableComponentFromCAD(self)
