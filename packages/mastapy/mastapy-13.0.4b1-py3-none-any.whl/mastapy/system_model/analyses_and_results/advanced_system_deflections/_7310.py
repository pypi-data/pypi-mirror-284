"""BevelGearAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7298
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "BevelGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7305,
        _7308,
        _7309,
        _7396,
        _7402,
        _7405,
        _7408,
        _7409,
        _7424,
        _7326,
        _7354,
        _7374,
        _7319,
        _7376,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearAdvancedSystemDeflection")


class BevelGearAdvancedSystemDeflection(
    _7298.AGMAGleasonConicalGearAdvancedSystemDeflection
):
    """BevelGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearAdvancedSystemDeflection")

    class _Cast_BevelGearAdvancedSystemDeflection:
        """Special nested class for casting BevelGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
            parent: "BevelGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7298.AGMAGleasonConicalGearAdvancedSystemDeflection":
            return self._parent._cast(
                _7298.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def conical_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7326.ConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7326,
            )

            return self._parent._cast(_7326.ConicalGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7354.GearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7374.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7374,
            )

            return self._parent._cast(_7374.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7319.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7376.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7305.BevelDifferentialGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(
                _7305.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7308.BevelDifferentialPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7308,
            )

            return self._parent._cast(
                _7308.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7309.BevelDifferentialSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(
                _7309.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7396.SpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(_7396.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7402.StraightBevelDiffGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7402,
            )

            return self._parent._cast(
                _7402.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7405.StraightBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7405,
            )

            return self._parent._cast(_7405.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7408.StraightBevelPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7408,
            )

            return self._parent._cast(
                _7408.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7409.StraightBevelSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7409,
            )

            return self._parent._cast(
                _7409.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7424.ZerolBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7424,
            )

            return self._parent._cast(_7424.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def bevel_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "BevelGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelGearAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2539.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection":
        return self._Cast_BevelGearAdvancedSystemDeflection(self)
