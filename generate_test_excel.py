#!/usr/bin/env python3
"""Generate a test Excel file with sample data."""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from datetime import datetime, timedelta


def generate_test_excel(filename="test_data.xlsx"):
    """Generate a test Excel file with various types of data.
    
    Args:
        filename: Output filename for the Excel file
    """
    # Create a new workbook
    wb = Workbook()
    
    # Remove default sheet and create custom sheets
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])
    
    # Sheet 1: Employee Data
    ws1 = wb.create_sheet("员工信息", 0)
    headers1 = ["姓名", "部门", "职位", "入职日期", "薪资", "绩效评分"]
    ws1.append(headers1)
    
    # Style header row
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF")
    for cell in ws1[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
    
    # Add sample employee data
    employees = [
        ["张三", "技术部", "高级工程师", datetime(2020, 3, 15), 25000, 4.5],
        ["李四", "市场部", "市场经理", datetime(2019, 6, 20), 18000, 4.8],
        ["王五", "财务部", "财务分析师", datetime(2021, 1, 10), 22000, 4.2],
        ["赵六", "技术部", "软件工程师", datetime(2022, 5, 8), 20000, 4.6],
        ["钱七", "人事部", "HR专员", datetime(2020, 9, 12), 15000, 4.3],
        ["孙八", "市场部", "市场专员", datetime(2023, 2, 1), 12000, 4.0],
    ]
    
    for row in employees:
        ws1.append(row)
    
    # Format date column
    for row in ws1.iter_rows(min_row=2, max_row=ws1.max_row, min_col=4, max_col=4):
        for cell in row:
            cell.number_format = "YYYY-MM-DD"
    
    # Format salary column
    for row in ws1.iter_rows(min_row=2, max_row=ws1.max_row, min_col=5, max_col=5):
        for cell in row:
            cell.number_format = "#,##0"
    
    # Auto-adjust column widths
    for column in ws1.columns:
        max_length = 0
        column_letter = get_column_letter(column[0].column)
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = min(max_length + 2, 50)
        ws1.column_dimensions[column_letter].width = adjusted_width
    
    # Sheet 2: Sales Data with Formulas
    ws2 = wb.create_sheet("销售数据", 1)
    headers2 = ["产品", "数量", "单价", "小计", "折扣率", "实付金额"]
    ws2.append(headers2)
    
    # Style header row
    for cell in ws2[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
    
    # Add sales data with formulas
    sales_data = [
        ["产品A", 10, 100, "=B2*C2", 0.1, "=D2*(1-E2)"],
        ["产品B", 5, 200, "=B3*C3", 0.15, "=D3*(1-E3)"],
        ["产品C", 8, 150, "=B4*C4", 0.05, "=D4*(1-E4)"],
        ["产品D", 12, 80, "=B5*C5", 0.2, "=D5*(1-E5)"],
        ["产品E", 6, 300, "=B6*C6", 0.1, "=D6*(1-E6)"],
    ]
    
    for row in sales_data:
        ws2.append(row)
    
    # Add total row
    ws2.append(["总计", "=SUM(B2:B6)", "", "=SUM(D2:D6)", "", "=SUM(F2:F6)"])
    total_row = ws2[ws2.max_row]
    for cell in total_row:
        cell.font = Font(bold=True)
        cell.fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    
    # Format currency columns
    for row in ws2.iter_rows(min_row=2, max_row=ws2.max_row, min_col=3, max_col=6):
        for cell in row:
            if cell.column in [3, 4, 6]:  # 单价, 小计, 实付金额
                cell.number_format = "#,##0.00"
            elif cell.column == 5:  # 折扣率
                cell.number_format = "0.00%"
    
    # Auto-adjust column widths
    for column in ws2.columns:
        max_length = 0
        column_letter = get_column_letter(column[0].column)
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = min(max_length + 2, 50)
        ws2.column_dimensions[column_letter].width = adjusted_width
    
    # Sheet 3: Test Data Types
    ws3 = wb.create_sheet("数据类型测试", 2)
    headers3 = ["数据类型", "示例值", "说明"]
    ws3.append(headers3)
    
    # Style header row
    for cell in ws3[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
    
    # Add various data types
    test_data = [
        ["整数", 12345, "普通整数"],
        ["小数", 123.456, "浮点数"],
        ["百分比", 0.85, "百分比格式"],
        ["日期", datetime.now(), "当前日期"],
        ["日期时间", datetime.now(), "日期时间"],
        ["文本", "这是测试文本", "字符串"],
        ["布尔值", True, "布尔类型"],
        ["公式", "=SUM(1,2,3)", "Excel公式"],
        ["空值", None, "空单元格"],
    ]
    
    for row in test_data:
        ws3.append(row)
    
    # Format percentage
    ws3["C3"].number_format = "0.00%"
    ws3["B3"] = 0.85
    
    # Format dates
    ws3["C4"].number_format = "YYYY-MM-DD"
    ws3["C5"].number_format = "YYYY-MM-DD HH:MM:SS"
    
    # Auto-adjust column widths
    for column in ws3.columns:
        max_length = 0
        column_letter = get_column_letter(column[0].column)
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = min(max_length + 2, 50)
        ws3.column_dimensions[column_letter].width = adjusted_width
    
    # Save the workbook
    wb.save(filename)
    print(f"✓ 测试Excel文件已生成: {filename}")
    print(f"  - 包含 {len(wb.sheetnames)} 个工作表")
    print(f"  - 工作表名称: {', '.join(wb.sheetnames)}")


if __name__ == "__main__":
    import sys
    
    filename = sys.argv[1] if len(sys.argv) > 1 else "test_data.xlsx"
    generate_test_excel(filename)

