"""AbstractShaftOrHousingHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AbstractShaftOrHousingHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2456
    from mastapy.system_model.analyses_and_results.system_deflections import _2707
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5701,
        _5746,
        _5771,
        _5827,
        _5809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingHarmonicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingHarmonicAnalysis")


class AbstractShaftOrHousingHarmonicAnalysis(_5726.ComponentHarmonicAnalysis):
    """AbstractShaftOrHousingHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingHarmonicAnalysis"
    )

    class _Cast_AbstractShaftOrHousingHarmonicAnalysis:
        """Special nested class for casting AbstractShaftOrHousingHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
            parent: "AbstractShaftOrHousingHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_5726.ComponentHarmonicAnalysis":
            return self._parent._cast(_5726.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_5701.AbstractShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5701,
            )

            return self._parent._cast(_5701.AbstractShaftHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_5746.CycloidalDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5746,
            )

            return self._parent._cast(_5746.CycloidalDiscHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_5771.FEPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5771,
            )

            return self._parent._cast(_5771.FEPartHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_5827.ShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5827,
            )

            return self._parent._cast(_5827.ShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "AbstractShaftOrHousingHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2456.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2707.AbstractShaftOrHousingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection

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
    ) -> "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis":
        return self._Cast_AbstractShaftOrHousingHarmonicAnalysis(self)
