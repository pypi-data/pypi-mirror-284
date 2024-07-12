"""InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6731,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6632
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6701,
        _6705,
        _6708,
        _6713,
        _6718,
        _6723,
        _6726,
        _6729,
        _6734,
        _6736,
        _6744,
        _6750,
        _6755,
        _6759,
        _6763,
        _6766,
        _6769,
        _6777,
        _6786,
        _6789,
        _6796,
        _6799,
        _6802,
        _6805,
        _6814,
        _6820,
        _6823,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"
)


class InterMountableComponentConnectionCompoundCriticalSpeedAnalysis(
    _6731.ConnectionCompoundCriticalSpeedAnalysis
):
    """InterMountableComponentConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
            parent: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6731.ConnectionCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6731.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6701.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(
                _6701.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def belt_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6705.BeltConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(_6705.BeltConnectionCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6708.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(
                _6708.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6713.BevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6713,
            )

            return self._parent._cast(_6713.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def clutch_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6718.ClutchConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(
                _6718.ClutchConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6723.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6723,
            )

            return self._parent._cast(
                _6723.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6726.ConceptGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(
                _6726.ConceptGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6729.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6729,
            )

            return self._parent._cast(
                _6729.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def coupling_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6734.CouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(
                _6734.CouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cvt_belt_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6736.CVTBeltConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(
                _6736.CVTBeltConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6744.CylindricalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6744,
            )

            return self._parent._cast(
                _6744.CylindricalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6750.FaceGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(_6750.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6755.GearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6755,
            )

            return self._parent._cast(_6755.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6759.HypoidGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(_6759.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6763.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6763,
            )

            return self._parent._cast(
                _6763.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6766.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6766,
            )

            return self._parent._cast(
                _6766.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6769.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6769,
            )

            return self._parent._cast(
                _6769.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6777.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6777,
            )

            return self._parent._cast(
                _6777.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6786.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6789.RollingRingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6789,
            )

            return self._parent._cast(
                _6789.RollingRingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6796.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6796,
            )

            return self._parent._cast(
                _6796.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6799.SpringDamperConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(
                _6799.SpringDamperConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6802.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6802,
            )

            return self._parent._cast(
                _6802.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6805.StraightBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6805,
            )

            return self._parent._cast(
                _6805.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6814.TorqueConverterConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6814,
            )

            return self._parent._cast(
                _6814.TorqueConverterConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6820.WormGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6820,
            )

            return self._parent._cast(_6820.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6823.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6823,
            )

            return self._parent._cast(
                _6823.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6632.InterMountableComponentConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.InterMountableComponentConnectionCriticalSpeedAnalysis]

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
    ) -> "List[_6632.InterMountableComponentConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.InterMountableComponentConnectionCriticalSpeedAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
        return (
            self._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis(
                self
            )
        )
