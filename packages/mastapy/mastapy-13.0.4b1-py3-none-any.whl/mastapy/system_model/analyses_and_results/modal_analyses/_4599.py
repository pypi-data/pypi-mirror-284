"""AGMAGleasonConicalGearSetModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AGMAGleasonConicalGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.system_deflections import _2711
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4606,
        _4611,
        _4662,
        _4706,
        _4712,
        _4715,
        _4736,
        _4658,
        _4703,
        _4593,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetModalAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetModalAnalysis")


class AGMAGleasonConicalGearSetModalAnalysis(_4627.ConicalGearSetModalAnalysis):
    """AGMAGleasonConicalGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetModalAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetModalAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
            parent: "AGMAGleasonConicalGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_4627.ConicalGearSetModalAnalysis":
            return self._parent._cast(_4627.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_4658.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_4703.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4703

            return self._parent._cast(_4703.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_4593.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_4606.BevelDifferentialGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606

            return self._parent._cast(_4606.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_4611.BevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.BevelGearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_4662.HypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.HypoidGearSetModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_4706.SpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4706

            return self._parent._cast(_4706.SpiralBevelGearSetModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_4712.StraightBevelDiffGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4712

            return self._parent._cast(_4712.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_4715.StraightBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4715

            return self._parent._cast(_4715.StraightBevelGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "_4736.ZerolBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4736

            return self._parent._cast(_4736.ZerolBevelGearSetModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "AGMAGleasonConicalGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetModalAnalysis.TYPE"
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
    def system_deflection_results(
        self: Self,
    ) -> "_2711.AGMAGleasonConicalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection

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
    ) -> "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetModalAnalysis(self)
