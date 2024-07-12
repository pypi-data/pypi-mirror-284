"""PlanetCarrierLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6946
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PlanetCarrierLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2489
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6956,
        _6859,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierLoadCase",)


Self = TypeVar("Self", bound="PlanetCarrierLoadCase")


class PlanetCarrierLoadCase(_6946.MountableComponentLoadCase):
    """PlanetCarrierLoadCase

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierLoadCase")

    class _Cast_PlanetCarrierLoadCase:
        """Special nested class for casting PlanetCarrierLoadCase to subclasses."""

        def __init__(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
            parent: "PlanetCarrierLoadCase",
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "_6946.MountableComponentLoadCase":
            return self._parent._cast(_6946.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "_6859.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ComponentLoadCase)

        @property
        def part_load_case(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planet_carrier_load_case(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "PlanetCarrierLoadCase":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetCarrierLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2489.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planet_manufacture_errors(
        self: Self,
    ) -> "List[_6956.PlanetarySocketManufactureError]":
        """List[mastapy.system_model.analyses_and_results.static_loads.PlanetarySocketManufactureError]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetManufactureErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase":
        return self._Cast_PlanetCarrierLoadCase(self)
