from django.shortcuts import render, redirect
from .models import CaptureEvent
from .analyzer import ScheduleAnalyzer
from google.api_core import exceptions  # 예외 처리를 위해 추가

def upload_page(request):
    return render(request, 'posters/upload.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('poster_image'):
        # 1. 파일 저장 (이미지만 먼저 DB에 기록)
        uploaded_file = request.FILES['poster_image']
        event = CaptureEvent.objects.create(image=uploaded_file)
        
        analyzer = ScheduleAnalyzer()
        
        try:
            # 2. AI 분석 실행 (에러 발생 가능성이 높은 구간)
            result = analyzer.analyze_image(event.image.path)
            
            # 3. 분석 결과 DB 업데이트
            event.event_name = result.get('event_name', '알 수 없는 행사')
            event.description = result.get('description', '')
            # 날짜 변환 로직이 추가될 자리입니다.
            event.save()
            
            # 성공 시 결과 페이지로 이동
            return render(request, 'posters/result.html', {'event': event})
            
        except exceptions.ResourceExhausted:
            # API 쿼터 초과 시 처리
            # 분석에 실패했으므로 생성했던 event 객체를 지우거나 안내만 합니다.
            return render(request, 'posters/upload.html', {
                'error_message': "현재 사용자가 많아 AI 분석이 지연되고 있습니다. 잠시 후 다시 시도해주세요."
            })
        except Exception as e:
            # 기타 예상치 못한 에러 처리
            print(f"Error: {e}")
            return render(request, 'posters/upload.html', {
                'error_message': "분석 중 오류가 발생했습니다."
            })

    return redirect('upload_page')