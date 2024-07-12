"""StraightBevelGearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6850
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearMeshLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2347
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6836,
        _6868,
        _6914,
        _6933,
        _6871,
    )
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshLoadCase",)


Self = TypeVar("Self", bound="StraightBevelGearMeshLoadCase")


class StraightBevelGearMeshLoadCase(_6850.BevelGearMeshLoadCase):
    """StraightBevelGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearMeshLoadCase")

    class _Cast_StraightBevelGearMeshLoadCase:
        """Special nested class for casting StraightBevelGearMeshLoadCase to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase",
            parent: "StraightBevelGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_load_case(
            self: "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase",
        ) -> "_6850.BevelGearMeshLoadCase":
            return self._parent._cast(_6850.BevelGearMeshLoadCase)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase",
        ) -> "_6836.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6836

            return self._parent._cast(_6836.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase",
        ) -> "_6868.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6868

            return self._parent._cast(_6868.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase",
        ) -> "_6914.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(_6914.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase",
        ) -> "_6933.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase",
        ) -> "_6871.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase",
        ) -> "StraightBevelGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2347.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

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
    ) -> "StraightBevelGearMeshLoadCase._Cast_StraightBevelGearMeshLoadCase":
        return self._Cast_StraightBevelGearMeshLoadCase(self)
