"""AbstractShaftOrHousingSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2736
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AbstractShaftOrHousingSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2456
    from mastapy.system_model.analyses_and_results.power_flows import _4054
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2708,
        _2759,
        _2778,
        _2825,
        _2806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingSystemDeflection",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingSystemDeflection")


class AbstractShaftOrHousingSystemDeflection(_2736.ComponentSystemDeflection):
    """AbstractShaftOrHousingSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingSystemDeflection"
    )

    class _Cast_AbstractShaftOrHousingSystemDeflection:
        """Special nested class for casting AbstractShaftOrHousingSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
            parent: "AbstractShaftOrHousingSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "_2736.ComponentSystemDeflection":
            return self._parent._cast(_2736.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "_2708.AbstractShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.AbstractShaftSystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "_2759.CycloidalDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.CycloidalDiscSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "_2778.FEPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(_2778.FEPartSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "_2825.ShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2825,
            )

            return self._parent._cast(_2825.ShaftSystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "AbstractShaftOrHousingSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mass_including_connected_components(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassIncludingConnectedComponents

        if temp is None:
            return 0.0

        return temp

    @property
    def polar_inertia_including_connected_components(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PolarInertiaIncludingConnectedComponents

        if temp is None:
            return 0.0

        return temp

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
    def power_flow_results(self: Self) -> "_4054.AbstractShaftOrHousingPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AbstractShaftOrHousingPowerFlow

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
    ) -> "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection":
        return self._Cast_AbstractShaftOrHousingSystemDeflection(self)
