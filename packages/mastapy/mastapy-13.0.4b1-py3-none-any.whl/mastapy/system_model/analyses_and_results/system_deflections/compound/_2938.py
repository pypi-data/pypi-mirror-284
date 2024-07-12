"""InterMountableComponentConnectionCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2907
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "InterMountableComponentConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2788
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2877,
        _2881,
        _2884,
        _2889,
        _2894,
        _2899,
        _2902,
        _2905,
        _2910,
        _2912,
        _2920,
        _2927,
        _2932,
        _2936,
        _2940,
        _2943,
        _2946,
        _2954,
        _2963,
        _2966,
        _2974,
        _2977,
        _2980,
        _2983,
        _2992,
        _2998,
        _3001,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundSystemDeflection"
)


class InterMountableComponentConnectionCompoundSystemDeflection(
    _2907.ConnectionCompoundSystemDeflection
):
    """InterMountableComponentConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundSystemDeflection",
    )

    class _Cast_InterMountableComponentConnectionCompoundSystemDeflection:
        """Special nested class for casting InterMountableComponentConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
            parent: "InterMountableComponentConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2907.ConnectionCompoundSystemDeflection":
            return self._parent._cast(_2907.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2877.AGMAGleasonConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(
                _2877.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def belt_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2881.BeltConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2881,
            )

            return self._parent._cast(_2881.BeltConnectionCompoundSystemDeflection)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2884.BevelDifferentialGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(
                _2884.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2889.BevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(_2889.BevelGearMeshCompoundSystemDeflection)

        @property
        def clutch_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2894.ClutchConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.ClutchConnectionCompoundSystemDeflection)

        @property
        def concept_coupling_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2899.ConceptCouplingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2899,
            )

            return self._parent._cast(
                _2899.ConceptCouplingConnectionCompoundSystemDeflection
            )

        @property
        def concept_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2902.ConceptGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2902,
            )

            return self._parent._cast(_2902.ConceptGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2905.ConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2905,
            )

            return self._parent._cast(_2905.ConicalGearMeshCompoundSystemDeflection)

        @property
        def coupling_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2910.CouplingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.CouplingConnectionCompoundSystemDeflection)

        @property
        def cvt_belt_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2912.CVTBeltConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2912,
            )

            return self._parent._cast(_2912.CVTBeltConnectionCompoundSystemDeflection)

        @property
        def cylindrical_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2920.CylindricalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(_2920.CylindricalGearMeshCompoundSystemDeflection)

        @property
        def face_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2927.FaceGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2927,
            )

            return self._parent._cast(_2927.FaceGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2932.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(_2932.GearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2936.HypoidGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2936,
            )

            return self._parent._cast(_2936.HypoidGearMeshCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2940.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(
                _2940.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2943.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2943,
            )

            return self._parent._cast(
                _2943.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> (
            "_2946.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2946,
            )

            return self._parent._cast(
                _2946.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2954.PartToPartShearCouplingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(
                _2954.PartToPartShearCouplingConnectionCompoundSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2963.RingPinsToDiscConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2963,
            )

            return self._parent._cast(
                _2963.RingPinsToDiscConnectionCompoundSystemDeflection
            )

        @property
        def rolling_ring_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2966.RollingRingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(
                _2966.RollingRingConnectionCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2974.SpiralBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def spring_damper_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2977.SpringDamperConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(
                _2977.SpringDamperConnectionCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2980.StraightBevelDiffGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2980,
            )

            return self._parent._cast(
                _2980.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2983.StraightBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2983,
            )

            return self._parent._cast(
                _2983.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def torque_converter_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2992.TorqueConverterConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2992,
            )

            return self._parent._cast(
                _2992.TorqueConverterConnectionCompoundSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2998.WormGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2998,
            )

            return self._parent._cast(_2998.WormGearMeshCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_3001.ZerolBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _3001,
            )

            return self._parent._cast(_3001.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "InterMountableComponentConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2788.InterMountableComponentConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection]

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
    ) -> "List[_2788.InterMountableComponentConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection]

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
    ) -> "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection":
        return self._Cast_InterMountableComponentConnectionCompoundSystemDeflection(
            self
        )
