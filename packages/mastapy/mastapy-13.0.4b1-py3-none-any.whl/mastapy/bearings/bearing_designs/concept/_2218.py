"""ConceptClearanceBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_designs import _2154
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_CLEARANCE_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Concept", "ConceptClearanceBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.concept import _2217, _2219
    from mastapy.bearings.bearing_designs import _2150


__docformat__ = "restructuredtext en"
__all__ = ("ConceptClearanceBearing",)


Self = TypeVar("Self", bound="ConceptClearanceBearing")


class ConceptClearanceBearing(_2154.NonLinearBearing):
    """ConceptClearanceBearing

    This is a mastapy class.
    """

    TYPE = _CONCEPT_CLEARANCE_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptClearanceBearing")

    class _Cast_ConceptClearanceBearing:
        """Special nested class for casting ConceptClearanceBearing to subclasses."""

        def __init__(
            self: "ConceptClearanceBearing._Cast_ConceptClearanceBearing",
            parent: "ConceptClearanceBearing",
        ):
            self._parent = parent

        @property
        def non_linear_bearing(
            self: "ConceptClearanceBearing._Cast_ConceptClearanceBearing",
        ) -> "_2154.NonLinearBearing":
            return self._parent._cast(_2154.NonLinearBearing)

        @property
        def bearing_design(
            self: "ConceptClearanceBearing._Cast_ConceptClearanceBearing",
        ) -> "_2150.BearingDesign":
            from mastapy.bearings.bearing_designs import _2150

            return self._parent._cast(_2150.BearingDesign)

        @property
        def concept_axial_clearance_bearing(
            self: "ConceptClearanceBearing._Cast_ConceptClearanceBearing",
        ) -> "_2217.ConceptAxialClearanceBearing":
            from mastapy.bearings.bearing_designs.concept import _2217

            return self._parent._cast(_2217.ConceptAxialClearanceBearing)

        @property
        def concept_radial_clearance_bearing(
            self: "ConceptClearanceBearing._Cast_ConceptClearanceBearing",
        ) -> "_2219.ConceptRadialClearanceBearing":
            from mastapy.bearings.bearing_designs.concept import _2219

            return self._parent._cast(_2219.ConceptRadialClearanceBearing)

        @property
        def concept_clearance_bearing(
            self: "ConceptClearanceBearing._Cast_ConceptClearanceBearing",
        ) -> "ConceptClearanceBearing":
            return self._parent

        def __getattr__(
            self: "ConceptClearanceBearing._Cast_ConceptClearanceBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptClearanceBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactDiameter

        if temp is None:
            return 0.0

        return temp

    @contact_diameter.setter
    @enforce_parameter_types
    def contact_diameter(self: Self, value: "float"):
        self.wrapped.ContactDiameter = float(value) if value is not None else 0.0

    @property
    def contact_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactStiffness

        if temp is None:
            return 0.0

        return temp

    @contact_stiffness.setter
    @enforce_parameter_types
    def contact_stiffness(self: Self, value: "float"):
        self.wrapped.ContactStiffness = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ConceptClearanceBearing._Cast_ConceptClearanceBearing":
        return self._Cast_ConceptClearanceBearing(self)
