"""AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6729,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6569
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6708,
        _6713,
        _6759,
        _6796,
        _6802,
        _6805,
        _6823,
        _6755,
        _6761,
        _6731,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis")


class AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis(
    _6729.ConicalGearMeshCompoundCriticalSpeedAnalysis
):
    """AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
            parent: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6729.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6729.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6755.GearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6755,
            )

            return self._parent._cast(_6755.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6761.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(
                _6761.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6731.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(_6731.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6708.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(
                _6708.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6713.BevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6713,
            )

            return self._parent._cast(_6713.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6759.HypoidGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(_6759.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6796.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6796,
            )

            return self._parent._cast(
                _6796.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6802.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6802,
            )

            return self._parent._cast(
                _6802.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6805.StraightBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6805,
            )

            return self._parent._cast(
                _6805.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6823.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6823,
            )

            return self._parent._cast(
                _6823.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6569.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6569.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis(self)
