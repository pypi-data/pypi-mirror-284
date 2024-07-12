"""InterMountableComponentConnectionCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3953
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "InterMountableComponentConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3851
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3923,
        _3927,
        _3930,
        _3935,
        _3940,
        _3945,
        _3948,
        _3951,
        _3956,
        _3958,
        _3966,
        _3972,
        _3977,
        _3981,
        _3985,
        _3988,
        _3991,
        _3999,
        _4008,
        _4011,
        _4018,
        _4021,
        _4024,
        _4027,
        _4036,
        _4042,
        _4045,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundStabilityAnalysis"
)


class InterMountableComponentConnectionCompoundStabilityAnalysis(
    _3953.ConnectionCompoundStabilityAnalysis
):
    """InterMountableComponentConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundStabilityAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
            parent: "InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3953.ConnectionCompoundStabilityAnalysis":
            return self._parent._cast(_3953.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3923.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(
                _3923.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def belt_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3927.BeltConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.BeltConnectionCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3930.BevelDifferentialGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(
                _3930.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3935.BevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3935,
            )

            return self._parent._cast(_3935.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def clutch_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3940.ClutchConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.ClutchConnectionCompoundStabilityAnalysis)

        @property
        def concept_coupling_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3945.ConceptCouplingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(
                _3945.ConceptCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def concept_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3948.ConceptGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(_3948.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3951.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(_3951.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def coupling_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3956.CouplingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def cvt_belt_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3958.CVTBeltConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3958,
            )

            return self._parent._cast(_3958.CVTBeltConnectionCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3966.CylindricalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3966,
            )

            return self._parent._cast(
                _3966.CylindricalGearMeshCompoundStabilityAnalysis
            )

        @property
        def face_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3972.FaceGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3977.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3977,
            )

            return self._parent._cast(_3977.GearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3981.HypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3981,
            )

            return self._parent._cast(_3981.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3985.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3988.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3988,
            )

            return self._parent._cast(
                _3988.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> (
            "_3991.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3991,
            )

            return self._parent._cast(
                _3991.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3999.PartToPartShearCouplingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(
                _3999.PartToPartShearCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_4008.RingPinsToDiscConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4008,
            )

            return self._parent._cast(
                _4008.RingPinsToDiscConnectionCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_4011.RollingRingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4011,
            )

            return self._parent._cast(
                _4011.RollingRingConnectionCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_4018.SpiralBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(
                _4018.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def spring_damper_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_4021.SpringDamperConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(
                _4021.SpringDamperConnectionCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_4024.StraightBevelDiffGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(
                _4024.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_4027.StraightBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4027,
            )

            return self._parent._cast(
                _4027.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def torque_converter_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_4036.TorqueConverterConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4036,
            )

            return self._parent._cast(
                _4036.TorqueConverterConnectionCompoundStabilityAnalysis
            )

        @property
        def worm_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_4042.WormGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4042,
            )

            return self._parent._cast(_4042.WormGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_4045.ZerolBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4045,
            )

            return self._parent._cast(_4045.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "InterMountableComponentConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3851.InterMountableComponentConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.InterMountableComponentConnectionStabilityAnalysis]

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
    ) -> "List[_3851.InterMountableComponentConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.InterMountableComponentConnectionStabilityAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis(
            self
        )
