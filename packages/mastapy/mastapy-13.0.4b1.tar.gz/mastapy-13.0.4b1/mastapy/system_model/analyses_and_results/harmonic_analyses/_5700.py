"""AbstractPeriodicExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_PERIODIC_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AbstractPeriodicExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.electric_machines.harmonic_load_data import _1398
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5754,
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
        _5775,
        _5777,
        _5778,
        _5780,
        _5813,
        _5830,
        _5856,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractPeriodicExcitationDetail",)


Self = TypeVar("Self", bound="AbstractPeriodicExcitationDetail")


class AbstractPeriodicExcitationDetail(_0.APIBase):
    """AbstractPeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_PERIODIC_EXCITATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractPeriodicExcitationDetail")

    class _Cast_AbstractPeriodicExcitationDetail:
        """Special nested class for casting AbstractPeriodicExcitationDetail to subclasses."""

        def __init__(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
            parent: "AbstractPeriodicExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5754.ElectricMachinePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5754,
            )

            return self._parent._cast(_5754.ElectricMachinePeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_force_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5755.ElectricMachineRotorXForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5755,
            )

            return self._parent._cast(
                _5755.ElectricMachineRotorXForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_x_moment_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5756.ElectricMachineRotorXMomentPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5756,
            )

            return self._parent._cast(
                _5756.ElectricMachineRotorXMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_force_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5757.ElectricMachineRotorYForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5757,
            )

            return self._parent._cast(
                _5757.ElectricMachineRotorYForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_moment_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5758.ElectricMachineRotorYMomentPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5758,
            )

            return self._parent._cast(
                _5758.ElectricMachineRotorYMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_z_force_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5759.ElectricMachineRotorZForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5759,
            )

            return self._parent._cast(
                _5759.ElectricMachineRotorZForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5760.ElectricMachineStatorToothAxialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5760,
            )

            return self._parent._cast(
                _5760.ElectricMachineStatorToothAxialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5761.ElectricMachineStatorToothLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5761,
            )

            return self._parent._cast(
                _5761.ElectricMachineStatorToothLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5762.ElectricMachineStatorToothMomentsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5762,
            )

            return self._parent._cast(
                _5762.ElectricMachineStatorToothMomentsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5763.ElectricMachineStatorToothRadialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5763,
            )

            return self._parent._cast(
                _5763.ElectricMachineStatorToothRadialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5764.ElectricMachineStatorToothTangentialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5764,
            )

            return self._parent._cast(
                _5764.ElectricMachineStatorToothTangentialLoadsExcitationDetail
            )

        @property
        def electric_machine_torque_ripple_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5765.ElectricMachineTorqueRipplePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5765,
            )

            return self._parent._cast(
                _5765.ElectricMachineTorqueRipplePeriodicExcitationDetail
            )

        @property
        def gear_mesh_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5775.GearMeshExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5775,
            )

            return self._parent._cast(_5775.GearMeshExcitationDetail)

        @property
        def gear_mesh_misalignment_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5777.GearMeshMisalignmentExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5777,
            )

            return self._parent._cast(_5777.GearMeshMisalignmentExcitationDetail)

        @property
        def gear_mesh_te_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5778.GearMeshTEExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5778,
            )

            return self._parent._cast(_5778.GearMeshTEExcitationDetail)

        @property
        def general_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5780.GeneralPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5780,
            )

            return self._parent._cast(_5780.GeneralPeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5813.PeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5813,
            )

            return self._parent._cast(_5813.PeriodicExcitationWithReferenceShaft)

        @property
        def single_node_periodic_excitation_with_reference_shaft(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5830.SingleNodePeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5830,
            )

            return self._parent._cast(
                _5830.SingleNodePeriodicExcitationWithReferenceShaft
            )

        @property
        def unbalanced_mass_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5856.UnbalancedMassExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5856,
            )

            return self._parent._cast(_5856.UnbalancedMassExcitationDetail)

        @property
        def abstract_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "AbstractPeriodicExcitationDetail":
            return self._parent

        def __getattr__(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractPeriodicExcitationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_load_data(self: Self) -> "_1398.HarmonicLoadDataBase":
        """mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicLoadData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail":
        return self._Cast_AbstractPeriodicExcitationDetail(self)
