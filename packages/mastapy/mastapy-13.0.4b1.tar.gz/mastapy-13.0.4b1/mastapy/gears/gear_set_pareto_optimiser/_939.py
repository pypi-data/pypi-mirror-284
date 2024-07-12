"""ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _927
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_STRAIGHT_BEVEL_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE = (
    python_net_import(
        "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
        "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
    )
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1570, _1558
    from mastapy.utility.databases import _1846, _1849, _1842


__docformat__ = "restructuredtext en"
__all__ = ("ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",)


Self = TypeVar(
    "Self", bound="ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase"
)


class ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase(
    _927.ParetoConicalRatingOptimisationStrategyDatabase
):
    """ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_STRAIGHT_BEVEL_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
    )

    class _Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase:
        """Special nested class for casting ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
            parent: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_927.ParetoConicalRatingOptimisationStrategyDatabase":
            return self._parent._cast(
                _927.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1570.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1570

            return self._parent._cast(_1570.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1558.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1558

            return self._parent._cast(_1558.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1846.NamedDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1849.SQLDatabase":
            pass

            from mastapy.utility.databases import _1849

            return self._parent._cast(_1849.SQLDatabase)

        @property
        def database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1842.Database":
            pass

            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.Database)

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
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
        self: Self,
        instance_to_wrap: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
        return (
            self._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase(
                self
            )
        )
