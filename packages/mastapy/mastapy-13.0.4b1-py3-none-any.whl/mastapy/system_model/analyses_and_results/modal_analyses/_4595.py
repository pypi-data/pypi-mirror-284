"""AbstractShaftOrHousingModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4618
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AbstractShaftOrHousingModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2456
    from mastapy.system_model.analyses_and_results.system_deflections import _2707
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4594,
        _4639,
        _4653,
        _4700,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingModalAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingModalAnalysis")


class AbstractShaftOrHousingModalAnalysis(_4618.ComponentModalAnalysis):
    """AbstractShaftOrHousingModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftOrHousingModalAnalysis")

    class _Cast_AbstractShaftOrHousingModalAnalysis:
        """Special nested class for casting AbstractShaftOrHousingModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
            parent: "AbstractShaftOrHousingModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "_4618.ComponentModalAnalysis":
            return self._parent._cast(_4618.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "_4594.AbstractShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.AbstractShaftModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "_4639.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(_4639.CycloidalDiscModalAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "_4653.FEPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653

            return self._parent._cast(_4653.FEPartModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "_4700.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.ShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "AbstractShaftOrHousingModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2456.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2707.AbstractShaftOrHousingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection

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
    ) -> (
        "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis"
    ):
        return self._Cast_AbstractShaftOrHousingModalAnalysis(self)
