"""PartToPartShearCouplingConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6873
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2368
    from mastapy.system_model.analyses_and_results.static_loads import _6933, _6871
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionLoadCase",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionLoadCase")


class PartToPartShearCouplingConnectionLoadCase(_6873.CouplingConnectionLoadCase):
    """PartToPartShearCouplingConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingConnectionLoadCase"
    )

    class _Cast_PartToPartShearCouplingConnectionLoadCase:
        """Special nested class for casting PartToPartShearCouplingConnectionLoadCase to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionLoadCase._Cast_PartToPartShearCouplingConnectionLoadCase",
            parent: "PartToPartShearCouplingConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_connection_load_case(
            self: "PartToPartShearCouplingConnectionLoadCase._Cast_PartToPartShearCouplingConnectionLoadCase",
        ) -> "_6873.CouplingConnectionLoadCase":
            return self._parent._cast(_6873.CouplingConnectionLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "PartToPartShearCouplingConnectionLoadCase._Cast_PartToPartShearCouplingConnectionLoadCase",
        ) -> "_6933.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "PartToPartShearCouplingConnectionLoadCase._Cast_PartToPartShearCouplingConnectionLoadCase",
        ) -> "_6871.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionLoadCase._Cast_PartToPartShearCouplingConnectionLoadCase",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionLoadCase._Cast_PartToPartShearCouplingConnectionLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionLoadCase._Cast_PartToPartShearCouplingConnectionLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "PartToPartShearCouplingConnectionLoadCase._Cast_PartToPartShearCouplingConnectionLoadCase",
        ) -> "PartToPartShearCouplingConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionLoadCase._Cast_PartToPartShearCouplingConnectionLoadCase",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingConnectionLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2368.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

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
    ) -> "PartToPartShearCouplingConnectionLoadCase._Cast_PartToPartShearCouplingConnectionLoadCase":
        return self._Cast_PartToPartShearCouplingConnectionLoadCase(self)
