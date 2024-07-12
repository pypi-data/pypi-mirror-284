"""UnbalancedMassHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6153,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "UnbalancedMassHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2497
    from mastapy.system_model.analyses_and_results.static_loads import _7002
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6108,
        _6054,
        _6110,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="UnbalancedMassHarmonicAnalysisOfSingleExcitation")


class UnbalancedMassHarmonicAnalysisOfSingleExcitation(
    _6153.VirtualComponentHarmonicAnalysisOfSingleExcitation
):
    """UnbalancedMassHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting UnbalancedMassHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation",
            parent: "UnbalancedMassHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation",
        ) -> "_6153.VirtualComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6153.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation",
        ) -> "_6054.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(_6054.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(_6110.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation",
        ) -> "UnbalancedMassHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "UnbalancedMassHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2497.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7002.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "UnbalancedMassHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation":
        return self._Cast_UnbalancedMassHarmonicAnalysisOfSingleExcitation(self)
