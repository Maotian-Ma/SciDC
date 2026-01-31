from openai import OpenAI
import json
from config import API_KEY, API_BASE_URL
client = OpenAI(
    api_key = API_KEY,
    base_url = API_BASE_URL,
        # 如果你的API key不在环境变量中，可以在这里指定
    # api_key="your-api-key-here"
)

def asking_api(content, model='claude-3-5-sonnet-20241022', cont_dics=None):
    try:
        if cont_dics is not None:
            messages = cont_dics
        else:
            messages = [
                {"role": "user", "content": content}
            ]

        # 使用新的API调用方式
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=2048,
            stop=None,
        )
        # 新的响应对象结构
        response_content = response.choices[0].message.content
    except Exception as e:
        print(e)
        response_content = ''

    print(response_content)
    return response_content
