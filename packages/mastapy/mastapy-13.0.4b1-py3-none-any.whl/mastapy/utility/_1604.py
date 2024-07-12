"""IndependentReportablePropertiesBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_REPORTABLE_PROPERTIES_BASE = python_net_import(
    "SMT.MastaAPI.Utility", "IndependentReportablePropertiesBase"
)

if TYPE_CHECKING:
    from mastapy.materials.efficiency import _301
    from mastapy.geometry import _312
    from mastapy.gears import _349
    from mastapy.gears.gear_designs.cylindrical import (
        _1030,
        _1061,
        _1069,
        _1070,
        _1073,
        _1074,
        _1082,
        _1090,
        _1092,
        _1096,
        _1100,
    )
    from mastapy.electric_machines import _1278
    from mastapy.electric_machines.load_cases_and_analyses import _1395
    from mastapy.math_utility.measured_data import _1584, _1585, _1586
    from mastapy.bearings.tolerances import _1938
    from mastapy.bearings.bearing_results import _1965
    from mastapy.bearings.bearing_results.rolling import _1996, _2090
    from mastapy.system_model.analyses_and_results.static_loads import _6832


__docformat__ = "restructuredtext en"
__all__ = ("IndependentReportablePropertiesBase",)


Self = TypeVar("Self", bound="IndependentReportablePropertiesBase")
T = TypeVar("T", bound="IndependentReportablePropertiesBase")


class IndependentReportablePropertiesBase(_0.APIBase, Generic[T]):
    """IndependentReportablePropertiesBase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _INDEPENDENT_REPORTABLE_PROPERTIES_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_IndependentReportablePropertiesBase")

    class _Cast_IndependentReportablePropertiesBase:
        """Special nested class for casting IndependentReportablePropertiesBase to subclasses."""

        def __init__(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
            parent: "IndependentReportablePropertiesBase",
        ):
            self._parent = parent

        @property
        def oil_pump_detail(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_301.OilPumpDetail":
            from mastapy.materials.efficiency import _301

            return self._parent._cast(_301.OilPumpDetail)

        @property
        def packaging_limits(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_312.PackagingLimits":
            from mastapy.geometry import _312

            return self._parent._cast(_312.PackagingLimits)

        @property
        def specification_for_the_effect_of_oil_kinematic_viscosity(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_349.SpecificationForTheEffectOfOilKinematicViscosity":
            from mastapy.gears import _349

            return self._parent._cast(
                _349.SpecificationForTheEffectOfOilKinematicViscosity
            )

        @property
        def cylindrical_gear_micro_geometry_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1030.CylindricalGearMicroGeometrySettings":
            from mastapy.gears.gear_designs.cylindrical import _1030

            return self._parent._cast(_1030.CylindricalGearMicroGeometrySettings)

        @property
        def hardened_material_properties(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1061.HardenedMaterialProperties":
            from mastapy.gears.gear_designs.cylindrical import _1061

            return self._parent._cast(_1061.HardenedMaterialProperties)

        @property
        def ltca_load_case_modifiable_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1069.LTCALoadCaseModifiableSettings":
            from mastapy.gears.gear_designs.cylindrical import _1069

            return self._parent._cast(_1069.LTCALoadCaseModifiableSettings)

        @property
        def ltca_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1070.LTCASettings":
            from mastapy.gears.gear_designs.cylindrical import _1070

            return self._parent._cast(_1070.LTCASettings)

        @property
        def micropitting(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1073.Micropitting":
            from mastapy.gears.gear_designs.cylindrical import _1073

            return self._parent._cast(_1073.Micropitting)

        @property
        def muller_residual_stress_definition(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1074.MullerResidualStressDefinition":
            from mastapy.gears.gear_designs.cylindrical import _1074

            return self._parent._cast(_1074.MullerResidualStressDefinition)

        @property
        def scuffing(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1082.Scuffing":
            from mastapy.gears.gear_designs.cylindrical import _1082

            return self._parent._cast(_1082.Scuffing)

        @property
        def surface_roughness(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1090.SurfaceRoughness":
            from mastapy.gears.gear_designs.cylindrical import _1090

            return self._parent._cast(_1090.SurfaceRoughness)

        @property
        def tiff_analysis_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1092.TiffAnalysisSettings":
            from mastapy.gears.gear_designs.cylindrical import _1092

            return self._parent._cast(_1092.TiffAnalysisSettings)

        @property
        def tooth_flank_fracture_analysis_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1096.ToothFlankFractureAnalysisSettings":
            from mastapy.gears.gear_designs.cylindrical import _1096

            return self._parent._cast(_1096.ToothFlankFractureAnalysisSettings)

        @property
        def usage(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1100.Usage":
            from mastapy.gears.gear_designs.cylindrical import _1100

            return self._parent._cast(_1100.Usage)

        @property
        def eccentricity(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1278.Eccentricity":
            from mastapy.electric_machines import _1278

            return self._parent._cast(_1278.Eccentricity)

        @property
        def temperatures(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1395.Temperatures":
            from mastapy.electric_machines.load_cases_and_analyses import _1395

            return self._parent._cast(_1395.Temperatures)

        @property
        def lookup_table_base(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1584.LookupTableBase":
            from mastapy.math_utility.measured_data import _1584

            return self._parent._cast(_1584.LookupTableBase)

        @property
        def onedimensional_function_lookup_table(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1585.OnedimensionalFunctionLookupTable":
            from mastapy.math_utility.measured_data import _1585

            return self._parent._cast(_1585.OnedimensionalFunctionLookupTable)

        @property
        def twodimensional_function_lookup_table(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1586.TwodimensionalFunctionLookupTable":
            from mastapy.math_utility.measured_data import _1586

            return self._parent._cast(_1586.TwodimensionalFunctionLookupTable)

        @property
        def roundness_specification(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1938.RoundnessSpecification":
            from mastapy.bearings.tolerances import _1938

            return self._parent._cast(_1938.RoundnessSpecification)

        @property
        def equivalent_load_factors(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1965.EquivalentLoadFactors":
            from mastapy.bearings.bearing_results import _1965

            return self._parent._cast(_1965.EquivalentLoadFactors)

        @property
        def iso14179_settings_per_bearing_type(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1996.ISO14179SettingsPerBearingType":
            from mastapy.bearings.bearing_results.rolling import _1996

            return self._parent._cast(_1996.ISO14179SettingsPerBearingType)

        @property
        def rolling_bearing_friction_coefficients(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_2090.RollingBearingFrictionCoefficients":
            from mastapy.bearings.bearing_results.rolling import _2090

            return self._parent._cast(_2090.RollingBearingFrictionCoefficients)

        @property
        def additional_acceleration_options(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_6832.AdditionalAccelerationOptions":
            from mastapy.system_model.analyses_and_results.static_loads import _6832

            return self._parent._cast(_6832.AdditionalAccelerationOptions)

        @property
        def independent_reportable_properties_base(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "IndependentReportablePropertiesBase":
            return self._parent

        def __getattr__(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
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
        self: Self, instance_to_wrap: "IndependentReportablePropertiesBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase"
    ):
        return self._Cast_IndependentReportablePropertiesBase(self)
