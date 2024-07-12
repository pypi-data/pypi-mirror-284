"""CVTPulleyHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5819
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CVTPulleyHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.system_deflections import _2754
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5739,
        _5807,
        _5726,
        _5809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyHarmonicAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyHarmonicAnalysis")


class CVTPulleyHarmonicAnalysis(_5819.PulleyHarmonicAnalysis):
    """CVTPulleyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyHarmonicAnalysis")

    class _Cast_CVTPulleyHarmonicAnalysis:
        """Special nested class for casting CVTPulleyHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
            parent: "CVTPulleyHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_harmonic_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_5819.PulleyHarmonicAnalysis":
            return self._parent._cast(_5819.PulleyHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_5739.CouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5739,
            )

            return self._parent._cast(_5739.CouplingHalfHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_5807.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5807,
            )

            return self._parent._cast(_5807.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_5726.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "CVTPulleyHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2754.CVTPulleySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection

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
    ) -> "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis":
        return self._Cast_CVTPulleyHarmonicAnalysis(self)
