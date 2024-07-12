"""ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _930
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_CYLINDRICAL_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE = (
    python_net_import(
        "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
        "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
    )
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1570, _1558
    from mastapy.utility.databases import _1846, _1849, _1842


__docformat__ = "restructuredtext en"
__all__ = ("ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",)


Self = TypeVar(
    "Self", bound="ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase"
)


class ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase(
    _930.ParetoCylindricalRatingOptimisationStrategyDatabase
):
    """ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_CYLINDRICAL_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
    )

    class _Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase:
        """Special nested class for casting ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
            parent: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_930.ParetoCylindricalRatingOptimisationStrategyDatabase":
            return self._parent._cast(
                _930.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1570.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1570

            return self._parent._cast(_1570.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1558.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1558

            return self._parent._cast(_1558.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1846.NamedDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1849.SQLDatabase":
            pass

            from mastapy.utility.databases import _1849

            return self._parent._cast(_1849.SQLDatabase)

        @property
        def database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1842.Database":
            pass

            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.Database)

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
        return self._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase(
            self
        )
