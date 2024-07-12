"""ProfileReliefSpecificationForCustomer102"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1143
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_RELIEF_SPECIFICATION_FOR_CUSTOMER_102 = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "ProfileReliefSpecificationForCustomer102",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1145


__docformat__ = "restructuredtext en"
__all__ = ("ProfileReliefSpecificationForCustomer102",)


Self = TypeVar("Self", bound="ProfileReliefSpecificationForCustomer102")


class ProfileReliefSpecificationForCustomer102(_1143.ProfileReliefWithDeviation):
    """ProfileReliefSpecificationForCustomer102

    This is a mastapy class.
    """

    TYPE = _PROFILE_RELIEF_SPECIFICATION_FOR_CUSTOMER_102
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ProfileReliefSpecificationForCustomer102"
    )

    class _Cast_ProfileReliefSpecificationForCustomer102:
        """Special nested class for casting ProfileReliefSpecificationForCustomer102 to subclasses."""

        def __init__(
            self: "ProfileReliefSpecificationForCustomer102._Cast_ProfileReliefSpecificationForCustomer102",
            parent: "ProfileReliefSpecificationForCustomer102",
        ):
            self._parent = parent

        @property
        def profile_relief_with_deviation(
            self: "ProfileReliefSpecificationForCustomer102._Cast_ProfileReliefSpecificationForCustomer102",
        ) -> "_1143.ProfileReliefWithDeviation":
            return self._parent._cast(_1143.ProfileReliefWithDeviation)

        @property
        def relief_with_deviation(
            self: "ProfileReliefSpecificationForCustomer102._Cast_ProfileReliefSpecificationForCustomer102",
        ) -> "_1145.ReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1145

            return self._parent._cast(_1145.ReliefWithDeviation)

        @property
        def profile_relief_specification_for_customer_102(
            self: "ProfileReliefSpecificationForCustomer102._Cast_ProfileReliefSpecificationForCustomer102",
        ) -> "ProfileReliefSpecificationForCustomer102":
            return self._parent

        def __getattr__(
            self: "ProfileReliefSpecificationForCustomer102._Cast_ProfileReliefSpecificationForCustomer102",
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
        self: Self, instance_to_wrap: "ProfileReliefSpecificationForCustomer102.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def involute_profile_mu_m(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InvoluteProfileMuM

        if temp is None:
            return ""

        return temp

    @property
    def roll_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ProfileReliefSpecificationForCustomer102._Cast_ProfileReliefSpecificationForCustomer102":
        return self._Cast_ProfileReliefSpecificationForCustomer102(self)
