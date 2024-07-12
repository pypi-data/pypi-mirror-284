"""StraightBevelDiffGearMeshCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3935
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "StraightBevelDiffGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2345
    from mastapy.system_model.analyses_and_results.stability_analyses import _3894
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3923,
        _3951,
        _3977,
        _3983,
        _3953,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshCompoundStabilityAnalysis")


class StraightBevelDiffGearMeshCompoundStabilityAnalysis(
    _3935.BevelGearMeshCompoundStabilityAnalysis
):
    """StraightBevelDiffGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis"
    )

    class _Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting StraightBevelDiffGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis",
            parent: "StraightBevelDiffGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis",
        ) -> "_3935.BevelGearMeshCompoundStabilityAnalysis":
            return self._parent._cast(_3935.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis",
        ) -> "_3923.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(
                _3923.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis",
        ) -> "_3951.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(_3951.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis",
        ) -> "_3977.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3977,
            )

            return self._parent._cast(_3977.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis",
        ) -> "_3983.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(
                _3983.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis",
        ) -> "_3953.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis",
        ) -> "StraightBevelDiffGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearMeshCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2345.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2345.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3894.StraightBevelDiffGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearMeshStabilityAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3894.StraightBevelDiffGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearMeshStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMeshCompoundStabilityAnalysis._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis":
        return self._Cast_StraightBevelDiffGearMeshCompoundStabilityAnalysis(self)
