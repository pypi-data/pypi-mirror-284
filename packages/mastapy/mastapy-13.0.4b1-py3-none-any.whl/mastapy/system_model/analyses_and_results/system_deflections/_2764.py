"""CylindricalGearSetSystemDeflectionTimestep"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.system_deflections import _2763
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_SYSTEM_DEFLECTION_TIMESTEP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalGearSetSystemDeflectionTimestep",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2781,
        _2827,
        _2706,
        _2806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetSystemDeflectionTimestep",)


Self = TypeVar("Self", bound="CylindricalGearSetSystemDeflectionTimestep")


class CylindricalGearSetSystemDeflectionTimestep(
    _2763.CylindricalGearSetSystemDeflection
):
    """CylindricalGearSetSystemDeflectionTimestep

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_SYSTEM_DEFLECTION_TIMESTEP
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetSystemDeflectionTimestep"
    )

    class _Cast_CylindricalGearSetSystemDeflectionTimestep:
        """Special nested class for casting CylindricalGearSetSystemDeflectionTimestep to subclasses."""

        def __init__(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
            parent: "CylindricalGearSetSystemDeflectionTimestep",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_system_deflection(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2763.CylindricalGearSetSystemDeflection":
            return self._parent._cast(_2763.CylindricalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2781.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2827.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2706.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "CylindricalGearSetSystemDeflectionTimestep":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
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
        self: Self, instance_to_wrap: "CylindricalGearSetSystemDeflectionTimestep.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep":
        return self._Cast_CylindricalGearSetSystemDeflectionTimestep(self)
