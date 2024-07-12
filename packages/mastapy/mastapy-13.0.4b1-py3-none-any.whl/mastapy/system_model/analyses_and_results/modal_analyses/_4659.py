"""GuideDxfModelModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4618
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "GuideDxfModelModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.system_deflections import _2783
    from mastapy.system_model.analyses_and_results.modal_analyses import _4683
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelModalAnalysis",)


Self = TypeVar("Self", bound="GuideDxfModelModalAnalysis")


class GuideDxfModelModalAnalysis(_4618.ComponentModalAnalysis):
    """GuideDxfModelModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideDxfModelModalAnalysis")

    class _Cast_GuideDxfModelModalAnalysis:
        """Special nested class for casting GuideDxfModelModalAnalysis to subclasses."""

        def __init__(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
            parent: "GuideDxfModelModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_modal_analysis(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ) -> "_4618.ComponentModalAnalysis":
            return self._parent._cast(_4618.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ) -> "GuideDxfModelModalAnalysis":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GuideDxfModelModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2475.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6918.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2783.GuideDxfModelSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GuideDxfModelSystemDeflection

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
    ) -> "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis":
        return self._Cast_GuideDxfModelModalAnalysis(self)
