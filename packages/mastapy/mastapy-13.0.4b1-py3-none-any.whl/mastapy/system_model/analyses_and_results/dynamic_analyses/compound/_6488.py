"""GearMeshCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6494
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "GearMeshCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6434,
        _6441,
        _6446,
        _6459,
        _6462,
        _6477,
        _6483,
        _6492,
        _6496,
        _6499,
        _6502,
        _6529,
        _6535,
        _6538,
        _6553,
        _6556,
        _6464,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="GearMeshCompoundDynamicAnalysis")


class GearMeshCompoundDynamicAnalysis(
    _6494.InterMountableComponentConnectionCompoundDynamicAnalysis
):
    """GearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundDynamicAnalysis")

    class _Cast_GearMeshCompoundDynamicAnalysis:
        """Special nested class for casting GearMeshCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
            parent: "GearMeshCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6494.InterMountableComponentConnectionCompoundDynamicAnalysis":
            return self._parent._cast(
                _6494.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6464.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6434.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(
                _6434.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6441.BevelDifferentialGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(
                _6441.BevelDifferentialGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6446.BevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(_6446.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def concept_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6459.ConceptGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.ConceptGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6462.ConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6462,
            )

            return self._parent._cast(_6462.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6477.CylindricalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6477,
            )

            return self._parent._cast(_6477.CylindricalGearMeshCompoundDynamicAnalysis)

        @property
        def face_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6483.FaceGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6483,
            )

            return self._parent._cast(_6483.FaceGearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6492.HypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(_6492.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6496.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6496,
            )

            return self._parent._cast(
                _6496.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6499.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(
                _6499.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6502.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6502,
            )

            return self._parent._cast(
                _6502.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6529.SpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6529,
            )

            return self._parent._cast(_6529.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6535.StraightBevelDiffGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6535,
            )

            return self._parent._cast(
                _6535.StraightBevelDiffGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6538.StraightBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6538,
            )

            return self._parent._cast(
                _6538.StraightBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def worm_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6553.WormGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6553,
            )

            return self._parent._cast(_6553.WormGearMeshCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6556.ZerolBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6556,
            )

            return self._parent._cast(_6556.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "GearMeshCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self: Self) -> "List[_6359.GearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.GearMeshDynamicAnalysis]

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
    ) -> "List[_6359.GearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.GearMeshDynamicAnalysis]

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
    ) -> "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis":
        return self._Cast_GearMeshCompoundDynamicAnalysis(self)
