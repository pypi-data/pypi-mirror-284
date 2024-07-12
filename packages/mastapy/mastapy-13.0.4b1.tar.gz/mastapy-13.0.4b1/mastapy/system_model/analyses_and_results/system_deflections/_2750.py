"""CouplingConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CouplingConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2366
    from mastapy.system_model.analyses_and_results.power_flows import _4090
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2732,
        _2738,
        _2807,
        _2831,
        _2849,
        _2748,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7561,
        _7562,
        _7559,
    )
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionSystemDeflection",)


Self = TypeVar("Self", bound="CouplingConnectionSystemDeflection")


class CouplingConnectionSystemDeflection(
    _2788.InterMountableComponentConnectionSystemDeflection
):
    """CouplingConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionSystemDeflection")

    class _Cast_CouplingConnectionSystemDeflection:
        """Special nested class for casting CouplingConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
            parent: "CouplingConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_2788.InterMountableComponentConnectionSystemDeflection":
            return self._parent._cast(
                _2788.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_2748.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_7561.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_2732.ClutchConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.ClutchConnectionSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_2738.ConceptCouplingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ConceptCouplingConnectionSystemDeflection)

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_2807.PartToPartShearCouplingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(
                _2807.PartToPartShearCouplingConnectionSystemDeflection
            )

        @property
        def spring_damper_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_2831.SpringDamperConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.SpringDamperConnectionSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "_2849.TorqueConverterConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2849,
            )

            return self._parent._cast(_2849.TorqueConverterConnectionSystemDeflection)

        @property
        def coupling_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "CouplingConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingConnectionSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2366.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4090.CouplingConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CouplingConnectionPowerFlow

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
    ) -> "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection":
        return self._Cast_CouplingConnectionSystemDeflection(self)
