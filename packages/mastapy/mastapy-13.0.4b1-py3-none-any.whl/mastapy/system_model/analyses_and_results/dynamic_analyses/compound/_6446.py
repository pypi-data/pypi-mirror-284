"""BevelGearMeshCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6434
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BevelGearMeshCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6441,
        _6529,
        _6535,
        _6538,
        _6556,
        _6462,
        _6488,
        _6494,
        _6464,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundDynamicAnalysis")


class BevelGearMeshCompoundDynamicAnalysis(
    _6434.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
):
    """BevelGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshCompoundDynamicAnalysis")

    class _Cast_BevelGearMeshCompoundDynamicAnalysis:
        """Special nested class for casting BevelGearMeshCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
            parent: "BevelGearMeshCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6434.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
            return self._parent._cast(
                _6434.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6462.ConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6462,
            )

            return self._parent._cast(_6462.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6488.GearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(_6488.GearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6494.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(
                _6494.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6464.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6441.BevelDifferentialGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(
                _6441.BevelDifferentialGearMeshCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6529.SpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6529,
            )

            return self._parent._cast(_6529.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6535.StraightBevelDiffGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6535,
            )

            return self._parent._cast(
                _6535.StraightBevelDiffGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6538.StraightBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6538,
            )

            return self._parent._cast(
                _6538.StraightBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6556.ZerolBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6556,
            )

            return self._parent._cast(_6556.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "BevelGearMeshCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMeshCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6315.BevelGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearMeshDynamicAnalysis]

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
    ) -> "List[_6315.BevelGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearMeshDynamicAnalysis]

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
    ) -> "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis":
        return self._Cast_BevelGearMeshCompoundDynamicAnalysis(self)
