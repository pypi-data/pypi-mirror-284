"""GearSetCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4847
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "GearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4658
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4755,
        _4762,
        _4767,
        _4780,
        _4783,
        _4798,
        _4804,
        _4813,
        _4817,
        _4820,
        _4823,
        _4833,
        _4850,
        _4856,
        _4859,
        _4874,
        _4877,
        _4749,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="GearSetCompoundModalAnalysis")


class GearSetCompoundModalAnalysis(_4847.SpecialisedAssemblyCompoundModalAnalysis):
    """GearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCompoundModalAnalysis")

    class _Cast_GearSetCompoundModalAnalysis:
        """Special nested class for casting GearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
            parent: "GearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4847.SpecialisedAssemblyCompoundModalAnalysis":
            return self._parent._cast(_4847.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4749.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4755.AGMAGleasonConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(
                _4755.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4762.BevelDifferentialGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(
                _4762.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4767.BevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4767,
            )

            return self._parent._cast(_4767.BevelGearSetCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4780.ConceptGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4780,
            )

            return self._parent._cast(_4780.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4783.ConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.ConicalGearSetCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4798.CylindricalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4798,
            )

            return self._parent._cast(_4798.CylindricalGearSetCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4804.FaceGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.FaceGearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4813.HypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4817.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4817,
            )

            return self._parent._cast(
                _4817.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4820.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(
                _4820.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4823.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(
                _4823.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def planetary_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4833.PlanetaryGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4833,
            )

            return self._parent._cast(_4833.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4850.SpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4856.StraightBevelDiffGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(
                _4856.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4859.StraightBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4859,
            )

            return self._parent._cast(_4859.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4874.WormGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4874,
            )

            return self._parent._cast(_4874.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4877.ZerolBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4877,
            )

            return self._parent._cast(_4877.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "GearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4658.GearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearSetModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(self: Self) -> "List[_4658.GearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearSetModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis":
        return self._Cast_GearSetCompoundModalAnalysis(self)
