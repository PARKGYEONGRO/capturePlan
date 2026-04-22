import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class ScheduleAnalyzer:
    def __init__(self):
        #킹 갓 무료 Gemini 1.5 Setting
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel('models/gemini-2.5-flash')
    

    def analyze_image(self, imagePath): #AI에게 이미지 전송하고, 원하는 규격(JSON)으로 응답 받는 함수

        imagePath = 'testImages\posterTestImage.PNG'

        #이미지에서 텍스트 추출
        #Load Image
        from PIL import Image
        img = Image.open(imagePath)

        prompt = '''
                여긴 ai한테 명령 내릴 프롬프트, ex) 이미지에서 행사 일정 정보 추출해서 JSON형식으로 변환~
                '''

        response = self.model.generate_content([prompt, img])

        #테스트 하기 위해 가공 데이터 반환
        extractedData = {
            "event_name": "Gemini 테스트 행사",
            "start_date": "2026-05-01",
            "end_date": None,
            "description": response.text[:100], # 응답 내용 일부
            "raw_text": response.text
        }

        return self.validateLogic(extractedData)
    
    def validateLogic(self, data): #Logic 검증, Logic 추가할거면 여기에
        
        #연도 없으면 현재 연도 추가 Logic
        if not data["start_date"]:
            data["description"] += "(날짜 확인 필요)"
        return data