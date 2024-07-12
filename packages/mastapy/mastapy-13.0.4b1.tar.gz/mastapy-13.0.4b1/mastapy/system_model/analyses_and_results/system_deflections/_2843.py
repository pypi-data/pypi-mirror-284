"""SynchroniserPartSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2751
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SynchroniserPartSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2626
    from mastapy.system_model.analyses_and_results.power_flows import _4172
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2842,
        _2844,
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
__all__ = ("SynchroniserPartSystemDeflection",)


Self = TypeVar("Self", bound="SynchroniserPartSystemDeflection")


class SynchroniserPartSystemDeflection(_2751.CouplingHalfSystemDeflection):
    """SynchroniserPartSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartSystemDeflection")

    class _Cast_SynchroniserPartSystemDeflection:
        """Special nested class for casting SynchroniserPartSystemDeflection to subclasses."""

        def __init__(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
            parent: "SynchroniserPartSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "_2751.CouplingHalfSystemDeflection":
            return self._parent._cast(_2751.CouplingHalfSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "_2803.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "_2736.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "_2842.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "_2844.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2844,
            )

            return self._parent._cast(_2844.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "SynchroniserPartSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPartSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2626.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4172.SynchroniserPartPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SynchroniserPartPowerFlow

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
    ) -> "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection":
        return self._Cast_SynchroniserPartSystemDeflection(self)
