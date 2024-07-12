"""ShaftModalComplexShape"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.rotor_dynamics import _4048
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MODAL_COMPLEX_SHAPE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics",
    "ShaftModalComplexShape",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.rotor_dynamics import _4051, _4052


__docformat__ = "restructuredtext en"
__all__ = ("ShaftModalComplexShape",)


Self = TypeVar("Self", bound="ShaftModalComplexShape")


class ShaftModalComplexShape(_4048.ShaftComplexShape["_1706.Number", "_1706.Number"]):
    """ShaftModalComplexShape

    This is a mastapy class.
    """

    TYPE = _SHAFT_MODAL_COMPLEX_SHAPE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftModalComplexShape")

    class _Cast_ShaftModalComplexShape:
        """Special nested class for casting ShaftModalComplexShape to subclasses."""

        def __init__(
            self: "ShaftModalComplexShape._Cast_ShaftModalComplexShape",
            parent: "ShaftModalComplexShape",
        ):
            self._parent = parent

        @property
        def shaft_complex_shape(
            self: "ShaftModalComplexShape._Cast_ShaftModalComplexShape",
        ) -> "_4048.ShaftComplexShape":
            return self._parent._cast(_4048.ShaftComplexShape)

        @property
        def shaft_modal_complex_shape_at_speeds(
            self: "ShaftModalComplexShape._Cast_ShaftModalComplexShape",
        ) -> "_4051.ShaftModalComplexShapeAtSpeeds":
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4051

            return self._parent._cast(_4051.ShaftModalComplexShapeAtSpeeds)

        @property
        def shaft_modal_complex_shape_at_stiffness(
            self: "ShaftModalComplexShape._Cast_ShaftModalComplexShape",
        ) -> "_4052.ShaftModalComplexShapeAtStiffness":
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4052

            return self._parent._cast(_4052.ShaftModalComplexShapeAtStiffness)

        @property
        def shaft_modal_complex_shape(
            self: "ShaftModalComplexShape._Cast_ShaftModalComplexShape",
        ) -> "ShaftModalComplexShape":
            return self._parent

        def __getattr__(
            self: "ShaftModalComplexShape._Cast_ShaftModalComplexShape", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftModalComplexShape.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ShaftModalComplexShape._Cast_ShaftModalComplexShape":
        return self._Cast_ShaftModalComplexShape(self)
