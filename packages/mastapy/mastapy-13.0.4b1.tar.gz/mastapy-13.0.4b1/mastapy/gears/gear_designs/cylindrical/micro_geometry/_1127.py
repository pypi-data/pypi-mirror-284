"""LeadModificationForCustomer102CAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1138
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEAD_MODIFICATION_FOR_CUSTOMER_102CAD = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "LeadModificationForCustomer102CAD",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1887
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1128


__docformat__ = "restructuredtext en"
__all__ = ("LeadModificationForCustomer102CAD",)


Self = TypeVar("Self", bound="LeadModificationForCustomer102CAD")


class LeadModificationForCustomer102CAD(_1138.ModificationForCustomer102CAD):
    """LeadModificationForCustomer102CAD

    This is a mastapy class.
    """

    TYPE = _LEAD_MODIFICATION_FOR_CUSTOMER_102CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LeadModificationForCustomer102CAD")

    class _Cast_LeadModificationForCustomer102CAD:
        """Special nested class for casting LeadModificationForCustomer102CAD to subclasses."""

        def __init__(
            self: "LeadModificationForCustomer102CAD._Cast_LeadModificationForCustomer102CAD",
            parent: "LeadModificationForCustomer102CAD",
        ):
            self._parent = parent

        @property
        def modification_for_customer_102cad(
            self: "LeadModificationForCustomer102CAD._Cast_LeadModificationForCustomer102CAD",
        ) -> "_1138.ModificationForCustomer102CAD":
            return self._parent._cast(_1138.ModificationForCustomer102CAD)

        @property
        def lead_modification_for_customer_102cad(
            self: "LeadModificationForCustomer102CAD._Cast_LeadModificationForCustomer102CAD",
        ) -> "LeadModificationForCustomer102CAD":
            return self._parent

        def __getattr__(
            self: "LeadModificationForCustomer102CAD._Cast_LeadModificationForCustomer102CAD",
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
        self: Self, instance_to_wrap: "LeadModificationForCustomer102CAD.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Crowning

        if temp is None:
            return 0.0

        return temp

    @property
    def lead_evaluation_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadEvaluationLength

        if temp is None:
            return 0.0

        return temp

    @property
    def lead_with_variation(self: Self) -> "_1887.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadWithVariation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_relief_points_for_customer_102(
        self: Self,
    ) -> "List[_1128.LeadReliefSpecificationForCustomer102]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.LeadReliefSpecificationForCustomer102]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadReliefPointsForCustomer102

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "LeadModificationForCustomer102CAD._Cast_LeadModificationForCustomer102CAD":
        return self._Cast_LeadModificationForCustomer102CAD(self)
