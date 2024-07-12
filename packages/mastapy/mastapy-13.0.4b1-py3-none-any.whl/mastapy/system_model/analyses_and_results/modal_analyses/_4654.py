"""FlexiblePinAssemblyModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4703
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "FlexiblePinAssemblyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474
    from mastapy.system_model.analyses_and_results.static_loads import _6910
    from mastapy.system_model.analyses_and_results.system_deflections import _2779
    from mastapy.system_model.analyses_and_results.modal_analyses import _4593, _4683
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyModalAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyModalAnalysis")


class FlexiblePinAssemblyModalAnalysis(_4703.SpecialisedAssemblyModalAnalysis):
    """FlexiblePinAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAssemblyModalAnalysis")

    class _Cast_FlexiblePinAssemblyModalAnalysis:
        """Special nested class for casting FlexiblePinAssemblyModalAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis",
            parent: "FlexiblePinAssemblyModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis(
            self: "FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis",
        ) -> "_4703.SpecialisedAssemblyModalAnalysis":
            return self._parent._cast(_4703.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis",
        ) -> "_4593.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis",
        ) -> "FlexiblePinAssemblyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FlexiblePinAssemblyModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2474.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6910.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2779.FlexiblePinAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection

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
    ) -> "FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis":
        return self._Cast_FlexiblePinAssemblyModalAnalysis(self)
