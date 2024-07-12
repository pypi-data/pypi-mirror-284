"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1760 import AdHocCustomTable
    from ._1761 import AxisSettings
    from ._1762 import BlankRow
    from ._1763 import CadPageOrientation
    from ._1764 import CadPageSize
    from ._1765 import CadTableBorderType
    from ._1766 import ChartDefinition
    from ._1767 import SMTChartPointShape
    from ._1768 import CustomChart
    from ._1769 import CustomDrawing
    from ._1770 import CustomGraphic
    from ._1771 import CustomImage
    from ._1772 import CustomReport
    from ._1773 import CustomReportCadDrawing
    from ._1774 import CustomReportChart
    from ._1775 import CustomReportChartItem
    from ._1776 import CustomReportColumn
    from ._1777 import CustomReportColumns
    from ._1778 import CustomReportDefinitionItem
    from ._1779 import CustomReportHorizontalLine
    from ._1780 import CustomReportHtmlItem
    from ._1781 import CustomReportItem
    from ._1782 import CustomReportItemContainer
    from ._1783 import CustomReportItemContainerCollection
    from ._1784 import CustomReportItemContainerCollectionBase
    from ._1785 import CustomReportItemContainerCollectionItem
    from ._1786 import CustomReportKey
    from ._1787 import CustomReportMultiPropertyItem
    from ._1788 import CustomReportMultiPropertyItemBase
    from ._1789 import CustomReportNameableItem
    from ._1790 import CustomReportNamedItem
    from ._1791 import CustomReportPropertyItem
    from ._1792 import CustomReportStatusItem
    from ._1793 import CustomReportTab
    from ._1794 import CustomReportTabs
    from ._1795 import CustomReportText
    from ._1796 import CustomRow
    from ._1797 import CustomSubReport
    from ._1798 import CustomTable
    from ._1799 import DefinitionBooleanCheckOptions
    from ._1800 import DynamicCustomReportItem
    from ._1801 import FontStyle
    from ._1802 import FontWeight
    from ._1803 import HeadingSize
    from ._1804 import SimpleChartDefinition
    from ._1805 import UserTextRow
else:
    import_structure = {
        "_1760": ["AdHocCustomTable"],
        "_1761": ["AxisSettings"],
        "_1762": ["BlankRow"],
        "_1763": ["CadPageOrientation"],
        "_1764": ["CadPageSize"],
        "_1765": ["CadTableBorderType"],
        "_1766": ["ChartDefinition"],
        "_1767": ["SMTChartPointShape"],
        "_1768": ["CustomChart"],
        "_1769": ["CustomDrawing"],
        "_1770": ["CustomGraphic"],
        "_1771": ["CustomImage"],
        "_1772": ["CustomReport"],
        "_1773": ["CustomReportCadDrawing"],
        "_1774": ["CustomReportChart"],
        "_1775": ["CustomReportChartItem"],
        "_1776": ["CustomReportColumn"],
        "_1777": ["CustomReportColumns"],
        "_1778": ["CustomReportDefinitionItem"],
        "_1779": ["CustomReportHorizontalLine"],
        "_1780": ["CustomReportHtmlItem"],
        "_1781": ["CustomReportItem"],
        "_1782": ["CustomReportItemContainer"],
        "_1783": ["CustomReportItemContainerCollection"],
        "_1784": ["CustomReportItemContainerCollectionBase"],
        "_1785": ["CustomReportItemContainerCollectionItem"],
        "_1786": ["CustomReportKey"],
        "_1787": ["CustomReportMultiPropertyItem"],
        "_1788": ["CustomReportMultiPropertyItemBase"],
        "_1789": ["CustomReportNameableItem"],
        "_1790": ["CustomReportNamedItem"],
        "_1791": ["CustomReportPropertyItem"],
        "_1792": ["CustomReportStatusItem"],
        "_1793": ["CustomReportTab"],
        "_1794": ["CustomReportTabs"],
        "_1795": ["CustomReportText"],
        "_1796": ["CustomRow"],
        "_1797": ["CustomSubReport"],
        "_1798": ["CustomTable"],
        "_1799": ["DefinitionBooleanCheckOptions"],
        "_1800": ["DynamicCustomReportItem"],
        "_1801": ["FontStyle"],
        "_1802": ["FontWeight"],
        "_1803": ["HeadingSize"],
        "_1804": ["SimpleChartDefinition"],
        "_1805": ["UserTextRow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdHocCustomTable",
    "AxisSettings",
    "BlankRow",
    "CadPageOrientation",
    "CadPageSize",
    "CadTableBorderType",
    "ChartDefinition",
    "SMTChartPointShape",
    "CustomChart",
    "CustomDrawing",
    "CustomGraphic",
    "CustomImage",
    "CustomReport",
    "CustomReportCadDrawing",
    "CustomReportChart",
    "CustomReportChartItem",
    "CustomReportColumn",
    "CustomReportColumns",
    "CustomReportDefinitionItem",
    "CustomReportHorizontalLine",
    "CustomReportHtmlItem",
    "CustomReportItem",
    "CustomReportItemContainer",
    "CustomReportItemContainerCollection",
    "CustomReportItemContainerCollectionBase",
    "CustomReportItemContainerCollectionItem",
    "CustomReportKey",
    "CustomReportMultiPropertyItem",
    "CustomReportMultiPropertyItemBase",
    "CustomReportNameableItem",
    "CustomReportNamedItem",
    "CustomReportPropertyItem",
    "CustomReportStatusItem",
    "CustomReportTab",
    "CustomReportTabs",
    "CustomReportText",
    "CustomRow",
    "CustomSubReport",
    "CustomTable",
    "DefinitionBooleanCheckOptions",
    "DynamicCustomReportItem",
    "FontStyle",
    "FontWeight",
    "HeadingSize",
    "SimpleChartDefinition",
    "UserTextRow",
)
