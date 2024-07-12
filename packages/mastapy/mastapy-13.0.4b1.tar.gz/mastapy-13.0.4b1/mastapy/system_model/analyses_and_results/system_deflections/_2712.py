"""AGMAGleasonConicalGearSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2747
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AGMAGleasonConicalGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.power_flows import _4058
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2724,
        _2725,
        _2726,
        _2729,
        _2786,
        _2830,
        _2836,
        _2839,
        _2840,
        _2841,
        _2862,
        _2782,
        _2803,
        _2736,
        _2806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSystemDeflection")


class AGMAGleasonConicalGearSystemDeflection(_2747.ConicalGearSystemDeflection):
    """AGMAGleasonConicalGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
            parent: "AGMAGleasonConicalGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2747.ConicalGearSystemDeflection":
            return self._parent._cast(_2747.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2782.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2803.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2736.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2724.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2725.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2726.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2729.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.BevelGearSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2786.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.HypoidGearSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2830.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.SpiralBevelGearSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2836.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2839.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2840.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2841.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2841,
            )

            return self._parent._cast(_2841.StraightBevelSunGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2862.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2862,
            )

            return self._parent._cast(_2862.ZerolBevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "AGMAGleasonConicalGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4058.AGMAGleasonConicalGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearSystemDeflection(self)
