"""HarmonicLoadDataCSVImport"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.static_loads import _6924
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_CSV_IMPORT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "HarmonicLoadDataCSVImport",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6890,
        _6902,
        _6922,
        _6925,
        _6923,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataCSVImport",)


Self = TypeVar("Self", bound="HarmonicLoadDataCSVImport")
T = TypeVar("T", bound="_6902.ElectricMachineHarmonicLoadImportOptionsBase")


class HarmonicLoadDataCSVImport(_6924.HarmonicLoadDataImportFromMotorPackages[T]):
    """HarmonicLoadDataCSVImport

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _HARMONIC_LOAD_DATA_CSV_IMPORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicLoadDataCSVImport")

    class _Cast_HarmonicLoadDataCSVImport:
        """Special nested class for casting HarmonicLoadDataCSVImport to subclasses."""

        def __init__(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport",
            parent: "HarmonicLoadDataCSVImport",
        ):
            self._parent = parent

        @property
        def harmonic_load_data_import_from_motor_packages(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport",
        ) -> "_6924.HarmonicLoadDataImportFromMotorPackages":
            return self._parent._cast(_6924.HarmonicLoadDataImportFromMotorPackages)

        @property
        def harmonic_load_data_import_base(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport",
        ) -> "_6923.HarmonicLoadDataImportBase":
            from mastapy.system_model.analyses_and_results.static_loads import _6923

            return self._parent._cast(_6923.HarmonicLoadDataImportBase)

        @property
        def harmonic_load_data_flux_import(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport",
        ) -> "_6922.HarmonicLoadDataFluxImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.HarmonicLoadDataFluxImport)

        @property
        def harmonic_load_data_jmag_import(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport",
        ) -> "_6925.HarmonicLoadDataJMAGImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.HarmonicLoadDataJMAGImport)

        @property
        def harmonic_load_data_csv_import(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport",
        ) -> "HarmonicLoadDataCSVImport":
            return self._parent

        def __getattr__(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicLoadDataCSVImport.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electric_machine_data_per_speed(
        self: Self,
    ) -> "List[_6890.DataFromMotorPackagePerSpeed]":
        """List[mastapy.system_model.analyses_and_results.static_loads.DataFromMotorPackagePerSpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineDataPerSpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport":
        return self._Cast_HarmonicLoadDataCSVImport(self)
