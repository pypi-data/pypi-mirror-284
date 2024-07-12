"""BevelGearCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4753
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BevelGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4610
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4760,
        _4763,
        _4764,
        _4848,
        _4854,
        _4857,
        _4860,
        _4861,
        _4875,
        _4781,
        _4807,
        _4826,
        _4774,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BevelGearCompoundModalAnalysis")


class BevelGearCompoundModalAnalysis(_4753.AGMAGleasonConicalGearCompoundModalAnalysis):
    """BevelGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearCompoundModalAnalysis")

    class _Cast_BevelGearCompoundModalAnalysis:
        """Special nested class for casting BevelGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
            parent: "BevelGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4753.AGMAGleasonConicalGearCompoundModalAnalysis":
            return self._parent._cast(_4753.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4781.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4781,
            )

            return self._parent._cast(_4781.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4807.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4826.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4774.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(_4774.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4760.BevelDifferentialGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4760,
            )

            return self._parent._cast(_4760.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4763.BevelDifferentialPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(
                _4763.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4764.BevelDifferentialSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4764,
            )

            return self._parent._cast(
                _4764.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4848.SpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4848,
            )

            return self._parent._cast(_4848.SpiralBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4854.StraightBevelDiffGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4854,
            )

            return self._parent._cast(_4854.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4857.StraightBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4857,
            )

            return self._parent._cast(_4857.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4860.StraightBevelPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4860,
            )

            return self._parent._cast(
                _4860.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4861.StraightBevelSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4861,
            )

            return self._parent._cast(_4861.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "_4875.ZerolBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4875,
            )

            return self._parent._cast(_4875.ZerolBevelGearCompoundModalAnalysis)

        @property
        def bevel_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "BevelGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4610.BevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearModalAnalysis]

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
    ) -> "List[_4610.BevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearModalAnalysis]

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
    ) -> "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis":
        return self._Cast_BevelGearCompoundModalAnalysis(self)
