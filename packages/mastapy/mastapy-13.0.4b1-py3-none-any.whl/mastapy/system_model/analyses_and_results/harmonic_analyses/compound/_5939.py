"""CouplingHalfCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5977
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "CouplingHalfCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5739
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5923,
        _5928,
        _5942,
        _5982,
        _5988,
        _5992,
        _6004,
        _6014,
        _6015,
        _6016,
        _6019,
        _6020,
        _5925,
        _5979,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundHarmonicAnalysis")


class CouplingHalfCompoundHarmonicAnalysis(
    _5977.MountableComponentCompoundHarmonicAnalysis
):
    """CouplingHalfCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundHarmonicAnalysis")

    class _Cast_CouplingHalfCompoundHarmonicAnalysis:
        """Special nested class for casting CouplingHalfCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
            parent: "CouplingHalfCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5977.MountableComponentCompoundHarmonicAnalysis":
            return self._parent._cast(_5977.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5925.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(_5925.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5979.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5923.ClutchHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5923,
            )

            return self._parent._cast(_5923.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5928.ConceptCouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5928,
            )

            return self._parent._cast(_5928.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5942.CVTPulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5942,
            )

            return self._parent._cast(_5942.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5982.PartToPartShearCouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(
                _5982.PartToPartShearCouplingHalfCompoundHarmonicAnalysis
            )

        @property
        def pulley_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5988.PulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5988,
            )

            return self._parent._cast(_5988.PulleyCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5992.RollingRingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5992,
            )

            return self._parent._cast(_5992.RollingRingCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_6004.SpringDamperHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6004,
            )

            return self._parent._cast(_6004.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_6014.SynchroniserHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6014,
            )

            return self._parent._cast(_6014.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_6015.SynchroniserPartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6015,
            )

            return self._parent._cast(_6015.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_6016.SynchroniserSleeveCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6016,
            )

            return self._parent._cast(_6016.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_6019.TorqueConverterPumpCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6019,
            )

            return self._parent._cast(_6019.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_6020.TorqueConverterTurbineCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6020,
            )

            return self._parent._cast(
                _6020.TorqueConverterTurbineCompoundHarmonicAnalysis
            )

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "CouplingHalfCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5739.CouplingHalfHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHalfHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5739.CouplingHalfHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHalfHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis":
        return self._Cast_CouplingHalfCompoundHarmonicAnalysis(self)
