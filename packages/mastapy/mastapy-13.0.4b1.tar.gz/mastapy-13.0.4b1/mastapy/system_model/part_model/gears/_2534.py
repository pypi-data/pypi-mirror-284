"""AGMAGleasonConicalGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGearSet"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import (
        _2536,
        _2540,
        _2555,
        _2564,
        _2566,
        _2568,
        _2574,
        _2552,
    )
    from mastapy.system_model.part_model import _2496, _2454, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSet",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSet")


class AGMAGleasonConicalGearSet(_2544.ConicalGearSet):
    """AGMAGleasonConicalGearSet

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearSet")

    class _Cast_AGMAGleasonConicalGearSet:
        """Special nested class for casting AGMAGleasonConicalGearSet to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
            parent: "AGMAGleasonConicalGearSet",
        ):
            self._parent = parent

        @property
        def conical_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2544.ConicalGearSet":
            return self._parent._cast(_2544.ConicalGearSet)

        @property
        def gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2552.GearSet":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.GearSet)

        @property
        def specialised_assembly(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2496.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2496

            return self._parent._cast(_2496.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2454.AbstractAssembly":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.AbstractAssembly)

        @property
        def part(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def bevel_differential_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2536.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2540.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.BevelGearSet)

        @property
        def hypoid_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2555.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.HypoidGearSet)

        @property
        def spiral_bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2564.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2564

            return self._parent._cast(_2564.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2566.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2566

            return self._parent._cast(_2566.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2568.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2568

            return self._parent._cast(_2568.StraightBevelGearSet)

        @property
        def zerol_bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2574.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2574

            return self._parent._cast(_2574.ZerolBevelGearSet)

        @property
        def agma_gleason_conical_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "AGMAGleasonConicalGearSet":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet":
        return self._Cast_AGMAGleasonConicalGearSet(self)
