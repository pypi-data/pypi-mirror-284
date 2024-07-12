"""LeadReliefSpecificationForCustomer102"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1129
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEAD_RELIEF_SPECIFICATION_FOR_CUSTOMER_102 = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "LeadReliefSpecificationForCustomer102",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1145


__docformat__ = "restructuredtext en"
__all__ = ("LeadReliefSpecificationForCustomer102",)


Self = TypeVar("Self", bound="LeadReliefSpecificationForCustomer102")


class LeadReliefSpecificationForCustomer102(_1129.LeadReliefWithDeviation):
    """LeadReliefSpecificationForCustomer102

    This is a mastapy class.
    """

    TYPE = _LEAD_RELIEF_SPECIFICATION_FOR_CUSTOMER_102
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LeadReliefSpecificationForCustomer102"
    )

    class _Cast_LeadReliefSpecificationForCustomer102:
        """Special nested class for casting LeadReliefSpecificationForCustomer102 to subclasses."""

        def __init__(
            self: "LeadReliefSpecificationForCustomer102._Cast_LeadReliefSpecificationForCustomer102",
            parent: "LeadReliefSpecificationForCustomer102",
        ):
            self._parent = parent

        @property
        def lead_relief_with_deviation(
            self: "LeadReliefSpecificationForCustomer102._Cast_LeadReliefSpecificationForCustomer102",
        ) -> "_1129.LeadReliefWithDeviation":
            return self._parent._cast(_1129.LeadReliefWithDeviation)

        @property
        def relief_with_deviation(
            self: "LeadReliefSpecificationForCustomer102._Cast_LeadReliefSpecificationForCustomer102",
        ) -> "_1145.ReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1145

            return self._parent._cast(_1145.ReliefWithDeviation)

        @property
        def lead_relief_specification_for_customer_102(
            self: "LeadReliefSpecificationForCustomer102._Cast_LeadReliefSpecificationForCustomer102",
        ) -> "LeadReliefSpecificationForCustomer102":
            return self._parent

        def __getattr__(
            self: "LeadReliefSpecificationForCustomer102._Cast_LeadReliefSpecificationForCustomer102",
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
        self: Self, instance_to_wrap: "LeadReliefSpecificationForCustomer102.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LeadReliefSpecificationForCustomer102._Cast_LeadReliefSpecificationForCustomer102":
        return self._Cast_LeadReliefSpecificationForCustomer102(self)
