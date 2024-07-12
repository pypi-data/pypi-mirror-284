"""BevelGearMeshCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3923
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "BevelGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3800
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3930,
        _4018,
        _4024,
        _4027,
        _4045,
        _3951,
        _3977,
        _3983,
        _3953,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundStabilityAnalysis")


class BevelGearMeshCompoundStabilityAnalysis(
    _3923.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
):
    """BevelGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshCompoundStabilityAnalysis"
    )

    class _Cast_BevelGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting BevelGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
            parent: "BevelGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3923.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            return self._parent._cast(
                _3923.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3951.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(_3951.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3977.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3977,
            )

            return self._parent._cast(_3977.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3983.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(
                _3983.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3953.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3930.BevelDifferentialGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(
                _3930.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_4018.SpiralBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(
                _4018.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_4024.StraightBevelDiffGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(
                _4024.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_4027.StraightBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4027,
            )

            return self._parent._cast(
                _4027.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "_4045.ZerolBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4045,
            )

            return self._parent._cast(_4045.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "BevelGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMeshCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3800.BevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelGearMeshStabilityAnalysis]

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
    ) -> "List[_3800.BevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelGearMeshStabilityAnalysis]

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
    ) -> "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis":
        return self._Cast_BevelGearMeshCompoundStabilityAnalysis(self)
