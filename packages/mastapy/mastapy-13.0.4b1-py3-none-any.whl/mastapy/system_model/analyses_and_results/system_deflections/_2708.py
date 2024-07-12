"""AbstractShaftSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2707
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AbstractShaftSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.power_flows import _4055
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2759,
        _2825,
        _2736,
        _2806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftSystemDeflection",)


Self = TypeVar("Self", bound="AbstractShaftSystemDeflection")


class AbstractShaftSystemDeflection(_2707.AbstractShaftOrHousingSystemDeflection):
    """AbstractShaftSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftSystemDeflection")

    class _Cast_AbstractShaftSystemDeflection:
        """Special nested class for casting AbstractShaftSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
            parent: "AbstractShaftSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "_2707.AbstractShaftOrHousingSystemDeflection":
            return self._parent._cast(_2707.AbstractShaftOrHousingSystemDeflection)

        @property
        def component_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "_2736.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "_2759.CycloidalDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.CycloidalDiscSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "_2825.ShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2825,
            )

            return self._parent._cast(_2825.ShaftSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "AbstractShaftSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftSystemDeflection.TYPE"):
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
    def power_flow_results(self: Self) -> "_4055.AbstractShaftPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AbstractShaftPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection":
        return self._Cast_AbstractShaftSystemDeflection(self)
