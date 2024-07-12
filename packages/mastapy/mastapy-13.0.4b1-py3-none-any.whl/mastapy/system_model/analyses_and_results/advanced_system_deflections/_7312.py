"""BevelGearSetAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7300
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "BevelGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7307,
        _7398,
        _7404,
        _7407,
        _7426,
        _7328,
        _7356,
        _7395,
        _7291,
        _7376,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearSetAdvancedSystemDeflection")


class BevelGearSetAdvancedSystemDeflection(
    _7300.AGMAGleasonConicalGearSetAdvancedSystemDeflection
):
    """BevelGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetAdvancedSystemDeflection")

    class _Cast_BevelGearSetAdvancedSystemDeflection:
        """Special nested class for casting BevelGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
            parent: "BevelGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7300.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            return self._parent._cast(
                _7300.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7328.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7328,
            )

            return self._parent._cast(_7328.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7356.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(_7356.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7395.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7395,
            )

            return self._parent._cast(_7395.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7291.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7291,
            )

            return self._parent._cast(_7291.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7376.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7307.BevelDifferentialGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(
                _7307.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7398.SpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7404.StraightBevelDiffGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7404,
            )

            return self._parent._cast(
                _7404.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7407.StraightBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7407,
            )

            return self._parent._cast(
                _7407.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "_7426.ZerolBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7426,
            )

            return self._parent._cast(_7426.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "BevelGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelGearSetAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2540.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection":
        return self._Cast_BevelGearSetAdvancedSystemDeflection(self)
