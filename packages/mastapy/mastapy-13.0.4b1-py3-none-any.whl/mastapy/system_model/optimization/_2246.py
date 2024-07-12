"""ConicalGearOptimisationStrategy"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.optimization import _2254
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_OPTIMISATION_STRATEGY = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization", "ConicalGearOptimisationStrategy"
)

if TYPE_CHECKING:
    from mastapy.system_model.optimization import _2255
    from mastapy.utility.databases import _1847


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearOptimisationStrategy",)


Self = TypeVar("Self", bound="ConicalGearOptimisationStrategy")


class ConicalGearOptimisationStrategy(
    _2254.OptimizationStrategy["_2247.ConicalGearOptimizationStep"]
):
    """ConicalGearOptimisationStrategy

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_OPTIMISATION_STRATEGY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearOptimisationStrategy")

    class _Cast_ConicalGearOptimisationStrategy:
        """Special nested class for casting ConicalGearOptimisationStrategy to subclasses."""

        def __init__(
            self: "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy",
            parent: "ConicalGearOptimisationStrategy",
        ):
            self._parent = parent

        @property
        def optimization_strategy(
            self: "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy",
        ) -> "_2254.OptimizationStrategy":
            return self._parent._cast(_2254.OptimizationStrategy)

        @property
        def optimization_strategy_base(
            self: "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy",
        ) -> "_2255.OptimizationStrategyBase":
            from mastapy.system_model.optimization import _2255

            return self._parent._cast(_2255.OptimizationStrategyBase)

        @property
        def named_database_item(
            self: "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy",
        ) -> "_1847.NamedDatabaseItem":
            from mastapy.utility.databases import _1847

            return self._parent._cast(_1847.NamedDatabaseItem)

        @property
        def conical_gear_optimisation_strategy(
            self: "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy",
        ) -> "ConicalGearOptimisationStrategy":
            return self._parent

        def __getattr__(
            self: "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearOptimisationStrategy.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy":
        return self._Cast_ConicalGearOptimisationStrategy(self)
