"""MultiNodeFELink"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.fe.links import _2438
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_NODE_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "MultiNodeFELink"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe.links import (
        _2439,
        _2441,
        _2442,
        _2443,
        _2444,
        _2446,
        _2447,
        _2448,
        _2449,
        _2450,
        _2451,
    )


__docformat__ = "restructuredtext en"
__all__ = ("MultiNodeFELink",)


Self = TypeVar("Self", bound="MultiNodeFELink")


class MultiNodeFELink(_2438.FELink):
    """MultiNodeFELink

    This is a mastapy class.
    """

    TYPE = _MULTI_NODE_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MultiNodeFELink")

    class _Cast_MultiNodeFELink:
        """Special nested class for casting MultiNodeFELink to subclasses."""

        def __init__(
            self: "MultiNodeFELink._Cast_MultiNodeFELink", parent: "MultiNodeFELink"
        ):
            self._parent = parent

        @property
        def fe_link(self: "MultiNodeFELink._Cast_MultiNodeFELink") -> "_2438.FELink":
            return self._parent._cast(_2438.FELink)

        @property
        def electric_machine_stator_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2439.ElectricMachineStatorFELink":
            from mastapy.system_model.fe.links import _2439

            return self._parent._cast(_2439.ElectricMachineStatorFELink)

        @property
        def gear_mesh_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2441.GearMeshFELink":
            from mastapy.system_model.fe.links import _2441

            return self._parent._cast(_2441.GearMeshFELink)

        @property
        def gear_with_duplicated_meshes_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2442.GearWithDuplicatedMeshesFELink":
            from mastapy.system_model.fe.links import _2442

            return self._parent._cast(_2442.GearWithDuplicatedMeshesFELink)

        @property
        def multi_angle_connection_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2443.MultiAngleConnectionFELink":
            from mastapy.system_model.fe.links import _2443

            return self._parent._cast(_2443.MultiAngleConnectionFELink)

        @property
        def multi_node_connector_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2444.MultiNodeConnectorFELink":
            from mastapy.system_model.fe.links import _2444

            return self._parent._cast(_2444.MultiNodeConnectorFELink)

        @property
        def planetary_connector_multi_node_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2446.PlanetaryConnectorMultiNodeFELink":
            from mastapy.system_model.fe.links import _2446

            return self._parent._cast(_2446.PlanetaryConnectorMultiNodeFELink)

        @property
        def planet_based_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2447.PlanetBasedFELink":
            from mastapy.system_model.fe.links import _2447

            return self._parent._cast(_2447.PlanetBasedFELink)

        @property
        def planet_carrier_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2448.PlanetCarrierFELink":
            from mastapy.system_model.fe.links import _2448

            return self._parent._cast(_2448.PlanetCarrierFELink)

        @property
        def point_load_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2449.PointLoadFELink":
            from mastapy.system_model.fe.links import _2449

            return self._parent._cast(_2449.PointLoadFELink)

        @property
        def rolling_ring_connection_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2450.RollingRingConnectionFELink":
            from mastapy.system_model.fe.links import _2450

            return self._parent._cast(_2450.RollingRingConnectionFELink)

        @property
        def shaft_hub_connection_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2451.ShaftHubConnectionFELink":
            from mastapy.system_model.fe.links import _2451

            return self._parent._cast(_2451.ShaftHubConnectionFELink)

        @property
        def multi_node_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "MultiNodeFELink":
            return self._parent

        def __getattr__(self: "MultiNodeFELink._Cast_MultiNodeFELink", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MultiNodeFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MultiNodeFELink._Cast_MultiNodeFELink":
        return self._Cast_MultiNodeFELink(self)
