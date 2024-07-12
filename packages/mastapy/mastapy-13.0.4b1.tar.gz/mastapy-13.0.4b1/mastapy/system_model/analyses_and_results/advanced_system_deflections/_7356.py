"""GearSetAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7395
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "GearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7371,
        _7300,
        _7307,
        _7312,
        _7325,
        _7328,
        _7344,
        _7351,
        _7360,
        _7364,
        _7367,
        _7370,
        _7381,
        _7398,
        _7404,
        _7407,
        _7423,
        _7426,
        _7291,
        _7376,
    )
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.gears.rating import _366
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="GearSetAdvancedSystemDeflection")


class GearSetAdvancedSystemDeflection(
    _7395.SpecialisedAssemblyAdvancedSystemDeflection
):
    """GearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetAdvancedSystemDeflection")

    class _Cast_GearSetAdvancedSystemDeflection:
        """Special nested class for casting GearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
            parent: "GearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7395.SpecialisedAssemblyAdvancedSystemDeflection":
            return self._parent._cast(_7395.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7291.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7291,
            )

            return self._parent._cast(_7291.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7376.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7300.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(
                _7300.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7307.BevelDifferentialGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(
                _7307.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7312.BevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.BevelGearSetAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7325.ConceptGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7325,
            )

            return self._parent._cast(_7325.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7328.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7328,
            )

            return self._parent._cast(_7328.ConicalGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7344.CylindricalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(_7344.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7351.FaceGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.FaceGearSetAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7360.HypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7360,
            )

            return self._parent._cast(_7360.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7364.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(
                _7364.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7367.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7367,
            )

            return self._parent._cast(
                _7367.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7370.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(
                _7370.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7381.PlanetaryGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7398.SpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7404.StraightBevelDiffGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7404,
            )

            return self._parent._cast(
                _7404.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7407.StraightBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7407,
            )

            return self._parent._cast(
                _7407.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7423.WormGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7423,
            )

            return self._parent._cast(_7423.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7426.ZerolBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7426,
            )

            return self._parent._cast(_7426.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "GearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def use_ltca_in_advanced_system_deflection(
        self: Self,
    ) -> "_7371.UseLtcaInAsdOption":
        """mastapy.system_model.analyses_and_results.advanced_system_deflections.UseLtcaInAsdOption"""
        temp = self.wrapped.UseLTCAInAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.UseLtcaInAsdOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.advanced_system_deflections._7371",
            "UseLtcaInAsdOption",
        )(value)

    @use_ltca_in_advanced_system_deflection.setter
    @enforce_parameter_types
    def use_ltca_in_advanced_system_deflection(
        self: Self, value: "_7371.UseLtcaInAsdOption"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.UseLtcaInAsdOption",
        )
        self.wrapped.UseLTCAInAdvancedSystemDeflection = value

    @property
    def assembly_design(self: Self) -> "_2552.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_366.GearSetRating":
        """mastapy.gears.rating.GearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection":
        return self._Cast_GearSetAdvancedSystemDeflection(self)
