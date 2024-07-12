"""BevelGearSetAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7037,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.system_deflections import _2728
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7045,
        _7134,
        _7140,
        _7143,
        _7161,
        _7066,
        _7092,
        _7131,
        _7027,
        _7112,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="BevelGearSetAdvancedTimeSteppingAnalysisForModulation")


class BevelGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7037.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
):
    """BevelGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7037.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7037.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7066.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7066,
            )

            return self._parent._cast(
                _7066.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7092.GearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7131.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7131,
            )

            return self._parent._cast(
                _7131.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7027.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7027,
            )

            return self._parent._cast(
                _7027.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7112.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7045.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7045,
            )

            return self._parent._cast(
                _7045.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7134.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7134,
            )

            return self._parent._cast(
                _7134.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7140.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7140,
            )

            return self._parent._cast(
                _7140.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7143.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7143,
            )

            return self._parent._cast(
                _7143.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7161.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7161,
            )

            return self._parent._cast(
                _7161.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BevelGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    def system_deflection_results(self: Self) -> "_2728.BevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BevelGearSetAdvancedTimeSteppingAnalysisForModulation(self)
