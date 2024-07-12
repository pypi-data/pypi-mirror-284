"""CouplingHalfDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CouplingHalfDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6321,
        _6326,
        _6340,
        _6382,
        _6388,
        _6393,
        _6404,
        _6414,
        _6415,
        _6416,
        _6419,
        _6420,
        _6323,
        _6379,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfDynamicAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfDynamicAnalysis")


class CouplingHalfDynamicAnalysis(_6377.MountableComponentDynamicAnalysis):
    """CouplingHalfDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfDynamicAnalysis")

    class _Cast_CouplingHalfDynamicAnalysis:
        """Special nested class for casting CouplingHalfDynamicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
            parent: "CouplingHalfDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6377.MountableComponentDynamicAnalysis":
            return self._parent._cast(_6377.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6323.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6321.ClutchHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.ClutchHalfDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6326.ConceptCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.ConceptCouplingHalfDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6340.CVTPulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340

            return self._parent._cast(_6340.CVTPulleyDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6382.PartToPartShearCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6388.PulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.PulleyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6393.RollingRingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.RollingRingDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6404.SpringDamperHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.SpringDamperHalfDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6414.SynchroniserHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6414

            return self._parent._cast(_6414.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6415.SynchroniserPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6415

            return self._parent._cast(_6415.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6416.SynchroniserSleeveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6416

            return self._parent._cast(_6416.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6419.TorqueConverterPumpDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6419

            return self._parent._cast(_6419.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "_6420.TorqueConverterTurbineDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6420

            return self._parent._cast(_6420.TorqueConverterTurbineDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "CouplingHalfDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfDynamicAnalysis.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis":
        return self._Cast_CouplingHalfDynamicAnalysis(self)
