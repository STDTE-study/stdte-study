from datetime import datetime
from typing import Dict, List
from openpyxl import Workbook
from random import choice, randint


def getRowsWithRandom(data: Dict[str, int], randomStart: int, randomEnd: int) -> int:
  items = list(data.keys())
  rowCount = randint(randomStart, randomEnd)
  rows = []

  for i in range(rowCount):
    item = choice(items)
    price = data[item]
    count = randint(1, 5)
    rows.append([i+1, item, price, count, price*count])

  return rows


def createWorkSheet(fileName: str, sheetName: str, columns: List[str], rows: List[List[any]]) -> None:
  workBook = Workbook()
  workSheet = workBook.active
  workSheet.title = sheetName
  workSheet.append(columns)

  for row in rows:
    workSheet.append(row)
  
  timestamp = datetime.now().timestamp()
  timeToString = str(timestamp).replace('.', '')
  fileName = fileName.split('.xlsx')[0]
  workBook.save(f'.xlsx/{fileName}-{timeToString}.xlsx')


if __name__ == '__main__':
  data = {
    "기계식 키보드": 120000,
    "게이밍 마우스": 40000,
    "32인치 모니터": 350000,
    "마우스 패드": 20000
  }

  fileName = '11번가.xlsx'
  sheetName = '주문목록'
  columns = ['순번', '품명', '가격', '수량', '합계']
  rows = getRowsWithRandom(data, 5, 10)
  createWorkSheet(fileName, sheetName, columns, rows)
