from pprint import pprint
from openpyxl import Workbook, load_workbook

# 엑셀 모듈
class ExcelModule: 
  def __init__(self) -> None:
    pass

  # 파일 생성
  def createExcelFile(self, rows, filename: str) -> None:
    wb = Workbook()
    ws = wb.active

    for row in rows:
      ws.append(row)
    wb.save(filename)
    pprint(rows)

  # 파일 읽기
  def readExcelFile(self, filename: str) -> None:
    obj = load_workbook(filename)
    sheets = obj.sheetnames

    for sheet in sheets:
      rows = list(obj[sheet].values)
      pprint(rows)


if __name__ == "__main__":
  filename = "CHOEWY-R0.xlsx"
  excelModule = ExcelModule()
  excelModule.createExcelFile([
    ['No.', 'Building', 'FireArea', 'FireArea Name'], 
    ['1', 'Reactor Building', 'CNB-000', 'Reactor building common Area'], 
    ['2', 'Primary Building', 'PB-014', 'Cable Spreding Room'],
    ['3', 'Turbine Building', 'TB-100', 'N-1E Battery Room']
  ], filename)
  excelModule.readExcelFile(filename)

  