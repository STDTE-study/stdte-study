from typing import Dict, List


def validateMarks(marks: List[int]) -> Dict[int, str]:
  return {i+1: '합격' if mark >= 60 else '불합격' for i, mark in enumerate(marks)}


def printResults(results: Dict[int, str]) -> None:
  for seq, result in results.items():
    print(f'{seq}번 학생은 {result}입니다.')


if __name__ == '__main__':
  marks = [30, 40, 90, 54, 100]
  results = validateMarks(marks)
  printResults(results)
