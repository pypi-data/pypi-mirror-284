"""AbstractShaftModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4595
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AbstractShaftModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.system_deflections import _2708
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4639,
        _4700,
        _4618,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftModalAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftModalAnalysis")


class AbstractShaftModalAnalysis(_4595.AbstractShaftOrHousingModalAnalysis):
    """AbstractShaftModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftModalAnalysis")

    class _Cast_AbstractShaftModalAnalysis:
        """Special nested class for casting AbstractShaftModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
            parent: "AbstractShaftModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4595.AbstractShaftOrHousingModalAnalysis":
            return self._parent._cast(_4595.AbstractShaftOrHousingModalAnalysis)

        @property
        def component_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4618.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4639.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(_4639.CycloidalDiscModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4700.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.ShaftModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "AbstractShaftModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2708.AbstractShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftSystemDeflection

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
    ) -> "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis":
        return self._Cast_AbstractShaftModalAnalysis(self)
