"""AbstractAssemblyCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2952
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "AbstractAssemblyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2706
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2878,
        _2879,
        _2882,
        _2885,
        _2890,
        _2892,
        _2893,
        _2898,
        _2903,
        _2906,
        _2909,
        _2913,
        _2915,
        _2921,
        _2928,
        _2930,
        _2933,
        _2937,
        _2941,
        _2944,
        _2947,
        _2953,
        _2957,
        _2964,
        _2967,
        _2972,
        _2975,
        _2976,
        _2981,
        _2984,
        _2987,
        _2991,
        _2999,
        _3002,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundSystemDeflection",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundSystemDeflection")


class AbstractAssemblyCompoundSystemDeflection(_2952.PartCompoundSystemDeflection):
    """AbstractAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundSystemDeflection"
    )

    class _Cast_AbstractAssemblyCompoundSystemDeflection:
        """Special nested class for casting AbstractAssemblyCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
            parent: "AbstractAssemblyCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2878.AGMAGleasonConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2878,
            )

            return self._parent._cast(
                _2878.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2879.AssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2879,
            )

            return self._parent._cast(_2879.AssemblyCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2882.BeltDriveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2885.BevelDifferentialGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2885,
            )

            return self._parent._cast(
                _2885.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2890.BevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2890,
            )

            return self._parent._cast(_2890.BevelGearSetCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2892.BoltedJointCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2892,
            )

            return self._parent._cast(_2892.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2893.ClutchCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2893,
            )

            return self._parent._cast(_2893.ClutchCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2898.ConceptCouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2898,
            )

            return self._parent._cast(_2898.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2903.ConceptGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2903,
            )

            return self._parent._cast(_2903.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2906.ConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2906,
            )

            return self._parent._cast(_2906.ConicalGearSetCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2909.CouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.CouplingCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2913.CVTCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.CVTCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2915.CycloidalAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(_2915.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2921.CylindricalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2921,
            )

            return self._parent._cast(_2921.CylindricalGearSetCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2928.FaceGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(_2928.FaceGearSetCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2930.FlexiblePinAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2930,
            )

            return self._parent._cast(_2930.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2933.GearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.GearSetCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2937.HypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2941.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2941,
            )

            return self._parent._cast(
                _2941.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2944.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2944,
            )

            return self._parent._cast(
                _2944.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2947.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2947,
            )

            return self._parent._cast(
                _2947.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2953.PartToPartShearCouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2953,
            )

            return self._parent._cast(
                _2953.PartToPartShearCouplingCompoundSystemDeflection
            )

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2957.PlanetaryGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(_2957.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2964.RollingRingAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2964,
            )

            return self._parent._cast(_2964.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def root_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2967.RootAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2967,
            )

            return self._parent._cast(_2967.RootAssemblyCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2972.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2972,
            )

            return self._parent._cast(_2972.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2975.SpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(_2975.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2976.SpringDamperCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.SpringDamperCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2981.StraightBevelDiffGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2981,
            )

            return self._parent._cast(
                _2981.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2984.StraightBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2984,
            )

            return self._parent._cast(
                _2984.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def synchroniser_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2987.SynchroniserCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2987,
            )

            return self._parent._cast(_2987.SynchroniserCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2991.TorqueConverterCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2991,
            )

            return self._parent._cast(_2991.TorqueConverterCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2999.WormGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2999,
            )

            return self._parent._cast(_2999.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_3002.ZerolBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _3002,
            )

            return self._parent._cast(_3002.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "AbstractAssemblyCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2706.AbstractAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2706.AbstractAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection":
        return self._Cast_AbstractAssemblyCompoundSystemDeflection(self)
