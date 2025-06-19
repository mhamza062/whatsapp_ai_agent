from fastapi import FastAPI, Request
from config import WHATSAPP_TOKEN, PHONE_NUMBER_ID
from gemini import get_reply_from_gemini
import httpx

app = FastAPI()

@app.get("/webhook")
def verify(request: Request):
    from fastapi.responses import PlainTextResponse
    args = request.query_params
    mode = args.get("hub.mode")
    token = args.get("hub.verify_token")
    challenge = args.get("hub.challenge")

    if mode == "subscribe" and token == "freshly_verify_token":
        return PlainTextResponse(challenge)
    return PlainTextResponse("Invalid")

@app.post("/webhook")
async def receive_message(request: Request):
    body = await request.json()
    try:
        message = body['entry'][0]['changes'][0]['value']['messages'][0]
        user_message = message['text']['body']
        from_number = message['from']

        reply = await get_reply_from_gemini(user_message)

        url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": from_number,
            "type": "text",
            "text": {
                "body": reply
            }
        }

        async with httpx.AsyncClient() as client:
            res = await client.post(url, headers=headers, json=payload)
            print("WhatsApp Status:", res.status_code)
            print("WhatsApp Response:", res.text)

    except Exception as e:
        print("Error:", e)

    return {"status": "received"}
