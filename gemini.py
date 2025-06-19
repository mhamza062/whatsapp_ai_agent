import httpx
from config import GEMINI_API_KEY

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"


async def get_reply_from_gemini(user_message: str) -> str:
    system_context = f"""
You are a helpful customer support assistant for a skincare brand called Freshly Beauty Products.

Respond politely, informatively, and in simple Urdu if possible.

Right now we only have 5 products in stock:
- Freshly Beauty Cream (Rs. 300)
- Freshly Hair Removing Cream (Rs. 180)
- Freshly Multani Mitti (Rs. 80)
- Freshly Rose Water (Rs. 100)
- Freshly Black Mask (Rs. 200)

Our delivery charges: Rs. 250  
Delivery time: 2–3 days  
Return policy: 7-day return  
Payment: Cash on delivery  
Contact: 03211234567  
Website: freshly.com.pk  
Instagram: @freshlybeautyproducts  
Facebook: @freshlybeautyproducts  

User message: "{user_message}"

Reply with relevant information only. Don't assume anything outside this context.
"""

    payload = {"contents": [{"parts": [{"text": system_context}]}]}

    params = {"key": GEMINI_API_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.post(GEMINI_URL, params=params, json=payload)
        data = response.json()
        print("Gemini Response:", data)
        return data['candidates'][0]['content']['parts'][0]['text']
