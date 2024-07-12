"""PlanetCarrierFELink"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.fe.links import _2447
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "PlanetCarrierFELink"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe.links import _2445, _2438


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierFELink",)


Self = TypeVar("Self", bound="PlanetCarrierFELink")


class PlanetCarrierFELink(_2447.PlanetBasedFELink):
    """PlanetCarrierFELink

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierFELink")

    class _Cast_PlanetCarrierFELink:
        """Special nested class for casting PlanetCarrierFELink to subclasses."""

        def __init__(
            self: "PlanetCarrierFELink._Cast_PlanetCarrierFELink",
            parent: "PlanetCarrierFELink",
        ):
            self._parent = parent

        @property
        def planet_based_fe_link(
            self: "PlanetCarrierFELink._Cast_PlanetCarrierFELink",
        ) -> "_2447.PlanetBasedFELink":
            return self._parent._cast(_2447.PlanetBasedFELink)

        @property
        def multi_node_fe_link(
            self: "PlanetCarrierFELink._Cast_PlanetCarrierFELink",
        ) -> "_2445.MultiNodeFELink":
            from mastapy.system_model.fe.links import _2445

            return self._parent._cast(_2445.MultiNodeFELink)

        @property
        def fe_link(
            self: "PlanetCarrierFELink._Cast_PlanetCarrierFELink",
        ) -> "_2438.FELink":
            from mastapy.system_model.fe.links import _2438

            return self._parent._cast(_2438.FELink)

        @property
        def planet_carrier_fe_link(
            self: "PlanetCarrierFELink._Cast_PlanetCarrierFELink",
        ) -> "PlanetCarrierFELink":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierFELink._Cast_PlanetCarrierFELink", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetCarrierFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PlanetCarrierFELink._Cast_PlanetCarrierFELink":
        return self._Cast_PlanetCarrierFELink(self)
