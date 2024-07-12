"""PerMachineSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility import _1613
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PER_MACHINE_SETTINGS = python_net_import("SMT.MastaAPI.Utility", "PerMachineSettings")

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _68
    from mastapy.nodal_analysis.geometry_modeller_link import _163
    from mastapy.gears.materials import _599
    from mastapy.gears.ltca.cylindrical import _858
    from mastapy.gears.gear_designs.cylindrical import _1021
    from mastapy.utility import _1614, _1615
    from mastapy.utility.units_and_measurements import _1624
    from mastapy.utility.scripting import _1757
    from mastapy.utility.databases import _1845
    from mastapy.utility.cad_export import _1850
    from mastapy.bearings import _1919
    from mastapy.system_model.part_model import _2490


__docformat__ = "restructuredtext en"
__all__ = ("PerMachineSettings",)


Self = TypeVar("Self", bound="PerMachineSettings")


class PerMachineSettings(_1613.PersistentSingleton):
    """PerMachineSettings

    This is a mastapy class.
    """

    TYPE = _PER_MACHINE_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PerMachineSettings")

    class _Cast_PerMachineSettings:
        """Special nested class for casting PerMachineSettings to subclasses."""

        def __init__(
            self: "PerMachineSettings._Cast_PerMachineSettings",
            parent: "PerMachineSettings",
        ):
            self._parent = parent

        @property
        def persistent_singleton(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1613.PersistentSingleton":
            return self._parent._cast(_1613.PersistentSingleton)

        @property
        def fe_user_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_68.FEUserSettings":
            from mastapy.nodal_analysis import _68

            return self._parent._cast(_68.FEUserSettings)

        @property
        def geometry_modeller_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_163.GeometryModellerSettings":
            from mastapy.nodal_analysis.geometry_modeller_link import _163

            return self._parent._cast(_163.GeometryModellerSettings)

        @property
        def gear_material_expert_system_factor_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_599.GearMaterialExpertSystemFactorSettings":
            from mastapy.gears.materials import _599

            return self._parent._cast(_599.GearMaterialExpertSystemFactorSettings)

        @property
        def cylindrical_gear_fe_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_858.CylindricalGearFESettings":
            from mastapy.gears.ltca.cylindrical import _858

            return self._parent._cast(_858.CylindricalGearFESettings)

        @property
        def cylindrical_gear_defaults(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1021.CylindricalGearDefaults":
            from mastapy.gears.gear_designs.cylindrical import _1021

            return self._parent._cast(_1021.CylindricalGearDefaults)

        @property
        def program_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1614.ProgramSettings":
            from mastapy.utility import _1614

            return self._parent._cast(_1614.ProgramSettings)

        @property
        def pushbullet_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1615.PushbulletSettings":
            from mastapy.utility import _1615

            return self._parent._cast(_1615.PushbulletSettings)

        @property
        def measurement_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1624.MeasurementSettings":
            from mastapy.utility.units_and_measurements import _1624

            return self._parent._cast(_1624.MeasurementSettings)

        @property
        def scripting_setup(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1757.ScriptingSetup":
            from mastapy.utility.scripting import _1757

            return self._parent._cast(_1757.ScriptingSetup)

        @property
        def database_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1845.DatabaseSettings":
            from mastapy.utility.databases import _1845

            return self._parent._cast(_1845.DatabaseSettings)

        @property
        def cad_export_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1850.CADExportSettings":
            from mastapy.utility.cad_export import _1850

            return self._parent._cast(_1850.CADExportSettings)

        @property
        def skf_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1919.SKFSettings":
            from mastapy.bearings import _1919

            return self._parent._cast(_1919.SKFSettings)

        @property
        def planet_carrier_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_2490.PlanetCarrierSettings":
            from mastapy.system_model.part_model import _2490

            return self._parent._cast(_2490.PlanetCarrierSettings)

        @property
        def per_machine_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "PerMachineSettings":
            return self._parent

        def __getattr__(self: "PerMachineSettings._Cast_PerMachineSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PerMachineSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    def reset_to_defaults(self: Self):
        """Method does not return."""
        self.wrapped.ResetToDefaults()

    @property
    def cast_to(self: Self) -> "PerMachineSettings._Cast_PerMachineSettings":
        return self._Cast_PerMachineSettings(self)
