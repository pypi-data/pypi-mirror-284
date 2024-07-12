"""ComponentFromCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "ComponentFromCAD"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.import_from_cad import (
        _2513,
        _2514,
        _2516,
        _2517,
        _2518,
        _2519,
        _2520,
        _2521,
        _2522,
        _2524,
        _2525,
        _2526,
        _2527,
        _2528,
        _2529,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentFromCAD",)


Self = TypeVar("Self", bound="ComponentFromCAD")


class ComponentFromCAD(_0.APIBase):
    """ComponentFromCAD

    This is a mastapy class.
    """

    TYPE = _COMPONENT_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentFromCAD")

    class _Cast_ComponentFromCAD:
        """Special nested class for casting ComponentFromCAD to subclasses."""

        def __init__(
            self: "ComponentFromCAD._Cast_ComponentFromCAD", parent: "ComponentFromCAD"
        ):
            self._parent = parent

        @property
        def abstract_shaft_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2513.AbstractShaftFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2513

            return self._parent._cast(_2513.AbstractShaftFromCAD)

        @property
        def clutch_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2514.ClutchFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2514

            return self._parent._cast(_2514.ClutchFromCAD)

        @property
        def concept_bearing_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2516.ConceptBearingFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2516

            return self._parent._cast(_2516.ConceptBearingFromCAD)

        @property
        def connector_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2517.ConnectorFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2517

            return self._parent._cast(_2517.ConnectorFromCAD)

        @property
        def cylindrical_gear_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2518.CylindricalGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2518

            return self._parent._cast(_2518.CylindricalGearFromCAD)

        @property
        def cylindrical_gear_in_planetary_set_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2519.CylindricalGearInPlanetarySetFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2519

            return self._parent._cast(_2519.CylindricalGearInPlanetarySetFromCAD)

        @property
        def cylindrical_planet_gear_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2520.CylindricalPlanetGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2520

            return self._parent._cast(_2520.CylindricalPlanetGearFromCAD)

        @property
        def cylindrical_ring_gear_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2521.CylindricalRingGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2521

            return self._parent._cast(_2521.CylindricalRingGearFromCAD)

        @property
        def cylindrical_sun_gear_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2522.CylindricalSunGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2522

            return self._parent._cast(_2522.CylindricalSunGearFromCAD)

        @property
        def mountable_component_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2524.MountableComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2524

            return self._parent._cast(_2524.MountableComponentFromCAD)

        @property
        def planet_shaft_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2525.PlanetShaftFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2525

            return self._parent._cast(_2525.PlanetShaftFromCAD)

        @property
        def pulley_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2526.PulleyFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2526

            return self._parent._cast(_2526.PulleyFromCAD)

        @property
        def rigid_connector_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2527.RigidConnectorFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2527

            return self._parent._cast(_2527.RigidConnectorFromCAD)

        @property
        def rolling_bearing_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2528.RollingBearingFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2528

            return self._parent._cast(_2528.RollingBearingFromCAD)

        @property
        def shaft_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "_2529.ShaftFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2529

            return self._parent._cast(_2529.ShaftFromCAD)

        @property
        def component_from_cad(
            self: "ComponentFromCAD._Cast_ComponentFromCAD",
        ) -> "ComponentFromCAD":
            return self._parent

        def __getattr__(self: "ComponentFromCAD._Cast_ComponentFromCAD", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def cast_to(self: Self) -> "ComponentFromCAD._Cast_ComponentFromCAD":
        return self._Cast_ComponentFromCAD(self)
