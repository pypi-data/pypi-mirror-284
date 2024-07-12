"""HarmonicLoadDataJMAGImport"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6920
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_JMAG_IMPORT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "HarmonicLoadDataJMAGImport",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6924, _6923


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataJMAGImport",)


Self = TypeVar("Self", bound="HarmonicLoadDataJMAGImport")


class HarmonicLoadDataJMAGImport(
    _6920.HarmonicLoadDataCSVImport[
        "_6903.ElectricMachineHarmonicLoadJMAGImportOptions"
    ]
):
    """HarmonicLoadDataJMAGImport

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_JMAG_IMPORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicLoadDataJMAGImport")

    class _Cast_HarmonicLoadDataJMAGImport:
        """Special nested class for casting HarmonicLoadDataJMAGImport to subclasses."""

        def __init__(
            self: "HarmonicLoadDataJMAGImport._Cast_HarmonicLoadDataJMAGImport",
            parent: "HarmonicLoadDataJMAGImport",
        ):
            self._parent = parent

        @property
        def harmonic_load_data_csv_import(
            self: "HarmonicLoadDataJMAGImport._Cast_HarmonicLoadDataJMAGImport",
        ) -> "_6920.HarmonicLoadDataCSVImport":
            return self._parent._cast(_6920.HarmonicLoadDataCSVImport)

        @property
        def harmonic_load_data_import_from_motor_packages(
            self: "HarmonicLoadDataJMAGImport._Cast_HarmonicLoadDataJMAGImport",
        ) -> "_6924.HarmonicLoadDataImportFromMotorPackages":
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.HarmonicLoadDataImportFromMotorPackages)

        @property
        def harmonic_load_data_import_base(
            self: "HarmonicLoadDataJMAGImport._Cast_HarmonicLoadDataJMAGImport",
        ) -> "_6923.HarmonicLoadDataImportBase":
            from mastapy.system_model.analyses_and_results.static_loads import _6923

            return self._parent._cast(_6923.HarmonicLoadDataImportBase)

        @property
        def harmonic_load_data_jmag_import(
            self: "HarmonicLoadDataJMAGImport._Cast_HarmonicLoadDataJMAGImport",
        ) -> "HarmonicLoadDataJMAGImport":
            return self._parent

        def __getattr__(
            self: "HarmonicLoadDataJMAGImport._Cast_HarmonicLoadDataJMAGImport",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicLoadDataJMAGImport.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    def select_jmag_file(self: Self):
        """Method does not return."""
        self.wrapped.SelectJMAGFile()

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicLoadDataJMAGImport._Cast_HarmonicLoadDataJMAGImport":
        return self._Cast_HarmonicLoadDataJMAGImport(self)
