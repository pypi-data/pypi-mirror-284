"""CouplingHalfHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6108,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CouplingHalfHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6051,
        _6056,
        _6071,
        _6112,
        _6119,
        _6124,
        _6134,
        _6144,
        _6146,
        _6147,
        _6150,
        _6151,
        _6054,
        _6110,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CouplingHalfHarmonicAnalysisOfSingleExcitation")


class CouplingHalfHarmonicAnalysisOfSingleExcitation(
    _6108.MountableComponentHarmonicAnalysisOfSingleExcitation
):
    """CouplingHalfHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CouplingHalfHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
            parent: "CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.MountableComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6108.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6054.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(_6054.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(_6110.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.ClutchHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6056.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6056,
            )

            return self._parent._cast(
                _6056.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6071.CVTPulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(_6071.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6112.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6112,
            )

            return self._parent._cast(
                _6112.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6119.PulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(_6119.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6124.RollingRingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(
                _6124.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6134.SpringDamperHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6144.SynchroniserHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6144,
            )

            return self._parent._cast(
                _6144.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6146.SynchroniserPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6146,
            )

            return self._parent._cast(
                _6146.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6147.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6147,
            )

            return self._parent._cast(
                _6147.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6150.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6150,
            )

            return self._parent._cast(
                _6150.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6151.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6151,
            )

            return self._parent._cast(
                _6151.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "CouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CouplingHalfHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
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
    ) -> "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation(self)
