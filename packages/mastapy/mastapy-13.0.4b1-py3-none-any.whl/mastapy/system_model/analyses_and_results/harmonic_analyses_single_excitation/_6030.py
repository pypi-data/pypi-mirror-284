"""AbstractShaftHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6031,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "AbstractShaftHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6074,
        _6126,
        _6054,
        _6110,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="AbstractShaftHarmonicAnalysisOfSingleExcitation")


class AbstractShaftHarmonicAnalysisOfSingleExcitation(
    _6031.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
):
    """AbstractShaftHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractShaftHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6031.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6031.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6054.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(_6054.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(_6110.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6074.CycloidalDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(
                _6074.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6126.ShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6126,
            )

            return self._parent._cast(_6126.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractShaftHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
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
        self: Self,
        instance_to_wrap: "AbstractShaftHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

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
    ) -> "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation(self)
