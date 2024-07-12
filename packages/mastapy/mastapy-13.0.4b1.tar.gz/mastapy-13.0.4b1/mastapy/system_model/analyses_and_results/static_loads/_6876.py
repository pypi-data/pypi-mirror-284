"""CVTBeltConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6842
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CVTBeltConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2293
    from mastapy.system_model.analyses_and_results.static_loads import _6933, _6871
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionLoadCase",)


Self = TypeVar("Self", bound="CVTBeltConnectionLoadCase")


class CVTBeltConnectionLoadCase(_6842.BeltConnectionLoadCase):
    """CVTBeltConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTBeltConnectionLoadCase")

    class _Cast_CVTBeltConnectionLoadCase:
        """Special nested class for casting CVTBeltConnectionLoadCase to subclasses."""

        def __init__(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
            parent: "CVTBeltConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def belt_connection_load_case(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ) -> "_6842.BeltConnectionLoadCase":
            return self._parent._cast(_6842.BeltConnectionLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ) -> "_6933.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ) -> "_6871.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_load_case(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ) -> "CVTBeltConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTBeltConnectionLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2293.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

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
    ) -> "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase":
        return self._Cast_CVTBeltConnectionLoadCase(self)
