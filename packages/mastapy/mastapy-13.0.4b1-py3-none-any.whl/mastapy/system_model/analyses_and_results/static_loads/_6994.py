"""TorqueConverterConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6873
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2372
    from mastapy.system_model.analyses_and_results.static_loads import _6933, _6871
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionLoadCase",)


Self = TypeVar("Self", bound="TorqueConverterConnectionLoadCase")


class TorqueConverterConnectionLoadCase(_6873.CouplingConnectionLoadCase):
    """TorqueConverterConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterConnectionLoadCase")

    class _Cast_TorqueConverterConnectionLoadCase:
        """Special nested class for casting TorqueConverterConnectionLoadCase to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
            parent: "TorqueConverterConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_connection_load_case(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "_6873.CouplingConnectionLoadCase":
            return self._parent._cast(_6873.CouplingConnectionLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "_6933.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "_6871.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def torque_converter_connection_load_case(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "TorqueConverterConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
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
        self: Self, instance_to_wrap: "TorqueConverterConnectionLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2372.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase":
        return self._Cast_TorqueConverterConnectionLoadCase(self)
