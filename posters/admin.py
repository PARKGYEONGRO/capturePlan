from django.contrib import admin

from django.contrib import admin
from .models import CaptureEvent

@admin.register(CaptureEvent)
class CaptureEventAdmin(admin.ModelAdmin):
    # 어드민 목록에서 보여줄 필드들 (실무형 설정)
    list_display = ('event_name', 'start_date', 'end_date', 'created_at')
    # 클릭해서 상세 페이지로 들어갈 필드
    list_display_links = ('event_name',)
    # 오른쪽 사이드바 필터 (날짜별로 보기 편함)
    list_filter = ('start_date', 'created_at')
    # 검색 기능 (행사명으로 검색 가능)
    search_fields = ('event_name', 'description')