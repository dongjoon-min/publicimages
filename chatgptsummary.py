import os
from openai import OpenAI

from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수 읽기
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# 요약할 텍스트
text_to_summarize = """
OpenAI는 인공지능 연구소로, AI의 안전하고 유익한 개발을 목표로 합니다. 
최근에는 GPT-3와 같은 강력한 언어 모델을 개발하여, 다양한 자연어 처리 작업에서 뛰어난 성능을 보여주고 있습니다. 
이 모델은 텍스트 생성, 번역, 요약, 질문 응답 등 다양한 응용 프로그램에 활용될 수 있습니다.
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes text."},
        {"role": "user", "content": f"Summarize the following text:\n\n{text_to_summarize}"}
    ]
)
    

# 요약 결과 및 토큰 사용량 가져오기
summary = response['choices'][0]['message']['content']
tokens_used = response['usage']['total_tokens']
prompt_tokens = response['usage']['prompt_tokens']
completion_tokens = response['usage']['completion_tokens']

# 비용 계산
input_cost_per_1k_tokens = 0.005  # 입력 토큰당 비용 ($0.005 per 1,000 tokens)
output_cost_per_1k_tokens = 0.015  # 출력 토큰당 비용 ($0.015 per 1,000 tokens)

cost = (prompt_tokens / 1000) * input_cost_per_1k_tokens + (completion_tokens / 1000) * output_cost_per_1k_tokens

print(f"Summary: {summary}")
print(f"Tokens used: {tokens_used}")
print(f"Cost: ${cost:.5f}")
