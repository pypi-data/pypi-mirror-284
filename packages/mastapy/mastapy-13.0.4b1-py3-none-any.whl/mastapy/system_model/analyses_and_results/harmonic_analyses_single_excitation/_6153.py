"""VirtualComponentHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6108,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "VirtualComponentHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6105,
        _6106,
        _6117,
        _6118,
        _6152,
        _6054,
        _6110,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="VirtualComponentHarmonicAnalysisOfSingleExcitation")


class VirtualComponentHarmonicAnalysisOfSingleExcitation(
    _6108.MountableComponentHarmonicAnalysisOfSingleExcitation
):
    """VirtualComponentHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting VirtualComponentHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
            parent: "VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.MountableComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6108.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6054.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(_6054.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(_6110.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6105.MassDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(_6105.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6106.MeasurementComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6106,
            )

            return self._parent._cast(
                _6106.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6117.PointLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(_6117.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6118.PowerLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(_6118.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6152.UnbalancedMassHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6152,
            )

            return self._parent._cast(
                _6152.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "VirtualComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "VirtualComponentHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2499.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation":
        return self._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation(self)
