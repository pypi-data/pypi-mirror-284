"""CouplingHalfHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CouplingHalfHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.system_deflections import _2751
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5722,
        _5728,
        _5743,
        _5811,
        _5819,
        _5825,
        _5837,
        _5848,
        _5850,
        _5851,
        _5854,
        _5855,
        _5726,
        _5809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfHarmonicAnalysis")


class CouplingHalfHarmonicAnalysis(_5807.MountableComponentHarmonicAnalysis):
    """CouplingHalfHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfHarmonicAnalysis")

    class _Cast_CouplingHalfHarmonicAnalysis:
        """Special nested class for casting CouplingHalfHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
            parent: "CouplingHalfHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5807.MountableComponentHarmonicAnalysis":
            return self._parent._cast(_5807.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5726.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5722.ClutchHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(_5722.ClutchHalfHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5728.ConceptCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5728,
            )

            return self._parent._cast(_5728.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5743.CVTPulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5743,
            )

            return self._parent._cast(_5743.CVTPulleyHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5811.PartToPartShearCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5811,
            )

            return self._parent._cast(_5811.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5819.PulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5819,
            )

            return self._parent._cast(_5819.PulleyHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5825.RollingRingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.RollingRingHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5837.SpringDamperHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.SpringDamperHalfHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5848.SynchroniserHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5848,
            )

            return self._parent._cast(_5848.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5850.SynchroniserPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5850,
            )

            return self._parent._cast(_5850.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5851.SynchroniserSleeveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5851,
            )

            return self._parent._cast(_5851.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5854.TorqueConverterPumpHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5854,
            )

            return self._parent._cast(_5854.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5855.TorqueConverterTurbineHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5855,
            )

            return self._parent._cast(_5855.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "CouplingHalfHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfHarmonicAnalysis.TYPE"):
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
    def system_deflection_results(self: Self) -> "_2751.CouplingHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis":
        return self._Cast_CouplingHalfHarmonicAnalysis(self)
