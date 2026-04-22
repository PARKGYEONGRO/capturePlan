from django.db import models

class CaptureEvent(models.Model):
    # 사진이 실제로 저장될 경로 (media/posters/년/월/일/파일명)
    image = models.ImageField(upload_to='posters/%Y/%m/%d/')
    
    # Gemini가 분석해서 채워줄 데이터들
    image = models.ImageField(upload_to='posters/%Y/%m/%d/')
    event_name = models.CharField(max_length=200, blank=True, verbose_name="행사명")
    start_date = models.DateField(null=True, blank=True, verbose_name="시작일")
    end_date = models.DateField(null=True, blank=True, verbose_name="종료일")
    description = models.TextField(blank=True, verbose_name="상세 내용")
    created_at = models.DateTimeField(auto_now_add=True)

    # 원본 텍스트 전체 저장 (나중에 디버깅용)
    raw_text = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name if self.event_name else f"Event {self.id}"