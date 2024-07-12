"""PointLoadHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6153,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "PointLoadHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2491
    from mastapy.system_model.analyses_and_results.static_loads import _6960
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6108,
        _6054,
        _6110,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="PointLoadHarmonicAnalysisOfSingleExcitation")


class PointLoadHarmonicAnalysisOfSingleExcitation(
    _6153.VirtualComponentHarmonicAnalysisOfSingleExcitation
):
    """PointLoadHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PointLoadHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_PointLoadHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PointLoadHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation",
            parent: "PointLoadHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation",
        ) -> "_6153.VirtualComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6153.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation",
        ) -> "_6054.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(_6054.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(_6110.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation",
        ) -> "PointLoadHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "PointLoadHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2491.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6960.PointLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase

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
    ) -> "PointLoadHarmonicAnalysisOfSingleExcitation._Cast_PointLoadHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PointLoadHarmonicAnalysisOfSingleExcitation(self)
