"""KlingelnbergCycloPalloidHypoidGearSetSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2790
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2559
    from mastapy.system_model.analyses_and_results.static_loads import _6939
    from mastapy.gears.rating.klingelnberg_hypoid import _413
    from mastapy.system_model.analyses_and_results.power_flows import _4127
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2794,
        _2792,
        _2746,
        _2781,
        _2827,
        _2706,
        _2806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSetSystemDeflection")


class KlingelnbergCycloPalloidHypoidGearSetSystemDeflection(
    _2790.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
):
    """KlingelnbergCycloPalloidHypoidGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
            parent: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2790.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            return self._parent._cast(
                _2790.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def conical_gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2746.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2746,
            )

            return self._parent._cast(_2746.ConicalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2781.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2827.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2706.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2559.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6939.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_413.KlingelnbergCycloPalloidHypoidGearSetRating":
        """mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_413.KlingelnbergCycloPalloidHypoidGearSetRating":
        """mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4127.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_system_deflection(
        self: Self,
    ) -> "List[_2794.KlingelnbergCycloPalloidHypoidGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_system_deflection(
        self: Self,
    ) -> "List[_2792.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection(self)
