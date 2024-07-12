"""CVTPulleySystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2814
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CVTPulleySystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.power_flows import _4095
    from mastapy.math_utility.measured_vectors import _1580
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2751,
        _2803,
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
__all__ = ("CVTPulleySystemDeflection",)


Self = TypeVar("Self", bound="CVTPulleySystemDeflection")


class CVTPulleySystemDeflection(_2814.PulleySystemDeflection):
    """CVTPulleySystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleySystemDeflection")

    class _Cast_CVTPulleySystemDeflection:
        """Special nested class for casting CVTPulleySystemDeflection to subclasses."""

        def __init__(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
            parent: "CVTPulleySystemDeflection",
        ):
            self._parent = parent

        @property
        def pulley_system_deflection(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
        ) -> "_2814.PulleySystemDeflection":
            return self._parent._cast(_2814.PulleySystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
        ) -> "_2751.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2751,
            )

            return self._parent._cast(_2751.CouplingHalfSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
        ) -> "_2803.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
        ) -> "_2736.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_system_deflection(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection",
        ) -> "CVTPulleySystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleySystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4095.CVTPulleyPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CVTPulleyPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def fixed_sheave_contact_results(self: Self) -> "List[_1580.NodeResults]":
        """List[mastapy.math_utility.measured_vectors.NodeResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FixedSheaveContactResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def moving_sheave_contact_results(self: Self) -> "List[_1580.NodeResults]":
        """List[mastapy.math_utility.measured_vectors.NodeResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MovingSheaveContactResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleySystemDeflection._Cast_CVTPulleySystemDeflection":
        return self._Cast_CVTPulleySystemDeflection(self)
