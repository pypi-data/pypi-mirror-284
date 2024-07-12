"""AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7057,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2456
    from mastapy.system_model.analyses_and_results.system_deflections import _2707
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7028,
        _7076,
        _7088,
        _7128,
        _7112,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation"
)


class AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation(
    _7057.ComponentAdvancedTimeSteppingAnalysisForModulation
):
    """AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
            parent: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7057.ComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7057.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7112.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7028.AbstractShaftAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7028,
            )

            return self._parent._cast(
                _7028.AbstractShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7076.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7088.FEPartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.FEPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7128.ShaftAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7128,
            )

            return self._parent._cast(
                _7128.ShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    ) -> "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )
