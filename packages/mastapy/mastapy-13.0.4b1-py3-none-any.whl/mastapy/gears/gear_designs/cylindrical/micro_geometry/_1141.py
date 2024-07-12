"""ProfileModificationForCustomer102CAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Optional, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1138
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_MODIFICATION_FOR_CUSTOMER_102CAD = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "ProfileModificationForCustomer102CAD",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1887
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1142


__docformat__ = "restructuredtext en"
__all__ = ("ProfileModificationForCustomer102CAD",)


Self = TypeVar("Self", bound="ProfileModificationForCustomer102CAD")


class ProfileModificationForCustomer102CAD(_1138.ModificationForCustomer102CAD):
    """ProfileModificationForCustomer102CAD

    This is a mastapy class.
    """

    TYPE = _PROFILE_MODIFICATION_FOR_CUSTOMER_102CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProfileModificationForCustomer102CAD")

    class _Cast_ProfileModificationForCustomer102CAD:
        """Special nested class for casting ProfileModificationForCustomer102CAD to subclasses."""

        def __init__(
            self: "ProfileModificationForCustomer102CAD._Cast_ProfileModificationForCustomer102CAD",
            parent: "ProfileModificationForCustomer102CAD",
        ):
            self._parent = parent

        @property
        def modification_for_customer_102cad(
            self: "ProfileModificationForCustomer102CAD._Cast_ProfileModificationForCustomer102CAD",
        ) -> "_1138.ModificationForCustomer102CAD":
            return self._parent._cast(_1138.ModificationForCustomer102CAD)

        @property
        def profile_modification_for_customer_102cad(
            self: "ProfileModificationForCustomer102CAD._Cast_ProfileModificationForCustomer102CAD",
        ) -> "ProfileModificationForCustomer102CAD":
            return self._parent

        def __getattr__(
            self: "ProfileModificationForCustomer102CAD._Cast_ProfileModificationForCustomer102CAD",
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
        self: Self, instance_to_wrap: "ProfileModificationForCustomer102CAD.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def involute_range(self: Self) -> "Optional[float]":
        """Optional[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InvoluteRange

        if temp is None:
            return None

        return temp

    @property
    def profile_tolerance_form_with_variation(
        self: Self,
    ) -> "_1887.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileToleranceFormWithVariation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def show_nominal_design(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowNominalDesign

        if temp is None:
            return False

        return temp

    @show_nominal_design.setter
    @enforce_parameter_types
    def show_nominal_design(self: Self, value: "bool"):
        self.wrapped.ShowNominalDesign = bool(value) if value is not None else False

    @property
    def profile_relief_points_for_customer_102(
        self: Self,
    ) -> "List[_1142.ProfileReliefSpecificationForCustomer102]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.ProfileReliefSpecificationForCustomer102]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileReliefPointsForCustomer102

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ProfileModificationForCustomer102CAD._Cast_ProfileModificationForCustomer102CAD":
        return self._Cast_ProfileModificationForCustomer102CAD(self)
