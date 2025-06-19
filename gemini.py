import httpx
from config import GEMINI_API_KEY

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

async def get_reply_from_gemini(user_message: str) -> str:
    system_context = "You are a helpful customer support assistant for a skincare brand called Freshly Beauty Products. Respond politely, informatively, and in simple Urdu if possible."

    payload = {
        "contents": [
            {"role": "user", "parts": [user_message]},
            {"role": "system", "parts": [system_context]}
        ]
    }

    params = {"key": GEMINI_API_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.post(GEMINI_URL, params=params, json=payload)
        data = response.json()
        return data['candidates'][0]['content']['parts'][0]['text']