"""CouplingHalfLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6946
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingHalfLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6855,
        _6861,
        _6878,
        _6952,
        _6962,
        _6969,
        _6979,
        _6989,
        _6991,
        _6992,
        _6996,
        _6997,
        _6859,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfLoadCase",)


Self = TypeVar("Self", bound="CouplingHalfLoadCase")


class CouplingHalfLoadCase(_6946.MountableComponentLoadCase):
    """CouplingHalfLoadCase

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfLoadCase")

    class _Cast_CouplingHalfLoadCase:
        """Special nested class for casting CouplingHalfLoadCase to subclasses."""

        def __init__(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
            parent: "CouplingHalfLoadCase",
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6946.MountableComponentLoadCase":
            return self._parent._cast(_6946.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6859.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ComponentLoadCase)

        @property
        def part_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6855.ClutchHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6861.ConceptCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6861

            return self._parent._cast(_6861.ConceptCouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6878.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6878

            return self._parent._cast(_6878.CVTPulleyLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6952.PartToPartShearCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.PartToPartShearCouplingHalfLoadCase)

        @property
        def pulley_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6962.PulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.PulleyLoadCase)

        @property
        def rolling_ring_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6969.RollingRingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.RollingRingLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6979.SpringDamperHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6979

            return self._parent._cast(_6979.SpringDamperHalfLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6989.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6989

            return self._parent._cast(_6989.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6991.SynchroniserPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6991

            return self._parent._cast(_6991.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6992.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6992

            return self._parent._cast(_6992.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6996.TorqueConverterPumpLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6996

            return self._parent._cast(_6996.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6997.TorqueConverterTurbineLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6997

            return self._parent._cast(_6997.TorqueConverterTurbineLoadCase)

        @property
        def coupling_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "CouplingHalfLoadCase":
            return self._parent

        def __getattr__(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2605.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase":
        return self._Cast_CouplingHalfLoadCase(self)
