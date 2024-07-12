"""AGMAGleasonConicalGearSetDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AGMAGleasonConicalGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6311,
        _6316,
        _6364,
        _6401,
        _6407,
        _6410,
        _6428,
        _6360,
        _6398,
        _6298,
        _6379,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetDynamicAnalysis")


class AGMAGleasonConicalGearSetDynamicAnalysis(_6332.ConicalGearSetDynamicAnalysis):
    """AGMAGleasonConicalGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetDynamicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetDynamicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
            parent: "AGMAGleasonConicalGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6332.ConicalGearSetDynamicAnalysis":
            return self._parent._cast(_6332.ConicalGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6360.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6398.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6298.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6311.BevelDifferentialGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6316.BevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.BevelGearSetDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6364.HypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.HypoidGearSetDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6401.SpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.SpiralBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6407.StraightBevelDiffGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6407

            return self._parent._cast(_6407.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6410.StraightBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6410

            return self._parent._cast(_6410.StraightBevelGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6428.ZerolBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6428

            return self._parent._cast(_6428.ZerolBevelGearSetDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "AGMAGleasonConicalGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2534.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

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
    ) -> "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetDynamicAnalysis(self)
