"""Customer102AGMA2000AccuracyGrader"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOMER_102AGMA2000_ACCURACY_GRADER = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "Customer102AGMA2000AccuracyGrader",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1154


__docformat__ = "restructuredtext en"
__all__ = ("Customer102AGMA2000AccuracyGrader",)


Self = TypeVar("Self", bound="Customer102AGMA2000AccuracyGrader")


class Customer102AGMA2000AccuracyGrader(_1149.AGMA2000A88AccuracyGrader):
    """Customer102AGMA2000AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _CUSTOMER_102AGMA2000_ACCURACY_GRADER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Customer102AGMA2000AccuracyGrader")

    class _Cast_Customer102AGMA2000AccuracyGrader:
        """Special nested class for casting Customer102AGMA2000AccuracyGrader to subclasses."""

        def __init__(
            self: "Customer102AGMA2000AccuracyGrader._Cast_Customer102AGMA2000AccuracyGrader",
            parent: "Customer102AGMA2000AccuracyGrader",
        ):
            self._parent = parent

        @property
        def agma2000a88_accuracy_grader(
            self: "Customer102AGMA2000AccuracyGrader._Cast_Customer102AGMA2000AccuracyGrader",
        ) -> "_1149.AGMA2000A88AccuracyGrader":
            return self._parent._cast(_1149.AGMA2000A88AccuracyGrader)

        @property
        def cylindrical_accuracy_grader(
            self: "Customer102AGMA2000AccuracyGrader._Cast_Customer102AGMA2000AccuracyGrader",
        ) -> "_1154.CylindricalAccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1154,
            )

            return self._parent._cast(_1154.CylindricalAccuracyGrader)

        @property
        def customer_102agma2000_accuracy_grader(
            self: "Customer102AGMA2000AccuracyGrader._Cast_Customer102AGMA2000AccuracyGrader",
        ) -> "Customer102AGMA2000AccuracyGrader":
            return self._parent

        def __getattr__(
            self: "Customer102AGMA2000AccuracyGrader._Cast_Customer102AGMA2000AccuracyGrader",
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
        self: Self, instance_to_wrap: "Customer102AGMA2000AccuracyGrader.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def composite_tolerance_toothto_tooth_from_customer_102g_design(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompositeToleranceToothtoToothFromCustomer102GDesign

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_variation_allowable_from_customer_102g_design(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchVariationAllowableFromCustomer102GDesign

        if temp is None:
            return 0.0

        return temp

    @property
    def runout_radial_tolerance_from_customer_102g_design(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RunoutRadialToleranceFromCustomer102GDesign

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_alignment_tolerance_from_customer_102g_design(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothAlignmentToleranceFromCustomer102GDesign

        if temp is None:
            return 0.0

        return temp

    @property
    def total_composite_tolerance_from_customer_102g_design(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalCompositeToleranceFromCustomer102GDesign

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "Customer102AGMA2000AccuracyGrader._Cast_Customer102AGMA2000AccuracyGrader":
        return self._Cast_Customer102AGMA2000AccuracyGrader(self)
