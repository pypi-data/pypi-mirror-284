"""StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2565
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5518
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5661,
        _5662,
        _5554,
        _5582,
        _5608,
        _5627,
        _5575,
        _5629,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis")


class StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis(
    _5566.BevelGearCompoundMultibodyDynamicsAnalysis
):
    """StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
            parent: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5566.BevelGearCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5566.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5554.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(
                _5554.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5582.ConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5582,
            )

            return self._parent._cast(
                _5582.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.GearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5627.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5575.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5575,
            )

            return self._parent._cast(_5575.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(_5629.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5661.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5661,
            )

            return self._parent._cast(
                _5661.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5662.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5662,
            )

            return self._parent._cast(
                _5662.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
        ) -> "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2565.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5518.StraightBevelDiffGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearMultibodyDynamicsAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5518.StraightBevelDiffGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis(self)
