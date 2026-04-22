from posters.analyzer import ScheduleAnalyzer

#엔진 가동
analyzer = ScheduleAnalyzer()

#Test
result = analyzer.analyzeImage("testImage.png")

print("\n=== AI 엔진 추출 결과 ===")
print(f"행사명: {result['eventName']}")
print(f"기간: {result['startDate']} ~ {result['endDate']}")
print(f"메모: {result['description']}")

