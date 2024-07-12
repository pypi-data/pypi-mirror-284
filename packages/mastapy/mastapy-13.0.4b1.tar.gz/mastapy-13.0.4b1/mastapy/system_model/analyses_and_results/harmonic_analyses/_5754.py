"""ElectricMachinePeriodicExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5813
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_PERIODIC_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachinePeriodicExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5755,
        _5756,
        _5757,
        _5758,
        _5759,
        _5760,
        _5761,
        _5762,
        _5763,
        _5764,
        _5765,
        _5700,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachinePeriodicExcitationDetail",)


Self = TypeVar("Self", bound="ElectricMachinePeriodicExcitationDetail")


class ElectricMachinePeriodicExcitationDetail(
    _5813.PeriodicExcitationWithReferenceShaft
):
    """ElectricMachinePeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_PERIODIC_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachinePeriodicExcitationDetail"
    )

    class _Cast_ElectricMachinePeriodicExcitationDetail:
        """Special nested class for casting ElectricMachinePeriodicExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
            parent: "ElectricMachinePeriodicExcitationDetail",
        ):
            self._parent = parent

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5813.PeriodicExcitationWithReferenceShaft":
            return self._parent._cast(_5813.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5700.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5700,
            )

            return self._parent._cast(_5700.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_force_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5755.ElectricMachineRotorXForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5755,
            )

            return self._parent._cast(
                _5755.ElectricMachineRotorXForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_x_moment_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5756.ElectricMachineRotorXMomentPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5756,
            )

            return self._parent._cast(
                _5756.ElectricMachineRotorXMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_force_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5757.ElectricMachineRotorYForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5757,
            )

            return self._parent._cast(
                _5757.ElectricMachineRotorYForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_moment_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5758.ElectricMachineRotorYMomentPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5758,
            )

            return self._parent._cast(
                _5758.ElectricMachineRotorYMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_z_force_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5759.ElectricMachineRotorZForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5759,
            )

            return self._parent._cast(
                _5759.ElectricMachineRotorZForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5760.ElectricMachineStatorToothAxialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5760,
            )

            return self._parent._cast(
                _5760.ElectricMachineStatorToothAxialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5761.ElectricMachineStatorToothLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5761,
            )

            return self._parent._cast(
                _5761.ElectricMachineStatorToothLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5762.ElectricMachineStatorToothMomentsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5762,
            )

            return self._parent._cast(
                _5762.ElectricMachineStatorToothMomentsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5763.ElectricMachineStatorToothRadialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5763,
            )

            return self._parent._cast(
                _5763.ElectricMachineStatorToothRadialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5764.ElectricMachineStatorToothTangentialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5764,
            )

            return self._parent._cast(
                _5764.ElectricMachineStatorToothTangentialLoadsExcitationDetail
            )

        @property
        def electric_machine_torque_ripple_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5765.ElectricMachineTorqueRipplePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5765,
            )

            return self._parent._cast(
                _5765.ElectricMachineTorqueRipplePeriodicExcitationDetail
            )

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "ElectricMachinePeriodicExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
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
        self: Self, instance_to_wrap: "ElectricMachinePeriodicExcitationDetail.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail":
        return self._Cast_ElectricMachinePeriodicExcitationDetail(self)
