import openai
from config import Config

client = openai.AsyncOpenAI(api_key=Config.OPENAI_API_KEY)

async def get_ai_response(text: str):
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content

async def transcribe_voice(file_bytes):
    # Pass file_bytes to Whisper API
    pass
