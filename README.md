# 🤖 WhatsApp AI Assistant using FastAPI, Gemini & WhatsApp Cloud API

This is a production-style AI Assistant built for WhatsApp Business, capable of auto-replying to user messages using Google Gemini (Gemini 1.5 Flash) and deployed via FastAPI.

The project is fully integrated with the official WhatsApp Cloud API (Meta) and provides dynamic, human-like responses based on business logic.

---

## 📌 Features

- ✅ Receives WhatsApp messages in real-time using Webhooks  
- ✅ Uses Google Gemini AI to generate intelligent replies  
- ✅ Responds politely in simple Urdu based on predefined product info  
- ✅ Built with FastAPI and easily deployable  
- ✅ Tested and working with Meta’s Sandbox test number  
- ✅ Replit-ready setup with .env secrets  

---

## 🧠 Use Case

A customer support chatbot for a skincare brand called Freshly Beauty Products, that can:

- Tell prices of available products  
- Share delivery info, return policy, contact, website  
- Handle FAQs in natural Urdu replies  
- Gracefully reject unsupported queries  

---

## 🚀 Tech Stack

| Layer       | Tech                          |
|-------------|-------------------------------|
| 💬 Messaging | WhatsApp Cloud API (Meta)     |
| 🧠 AI Engine | Google Gemini (gemini-1.5-flash) |
| 🧰 Backend   | FastAPI                       |
| 📡 Webhook   | HTTP POST (Webhook URL)       |
| 🌐 Hosting   | Replit                        |
| 🔒 Secrets   | Replit Secrets / .env         |

---

## 🗂 Project Structure

📁 whatsapp-ai-assistant/  
├── main.py           → Webhook logic (GET + POST)  
├── gemini.py         → Gemini AI response logic  
├── config.py         → Loads tokens from env  
├── requirements.txt  → Python dependencies  
├── .replit / replit.nix → Replit config  
└── README.md         → You're here  

---

## 📄 Setup Instructions

1. Clone the repo:
   git clone https://github.com/your-username/whatsapp-ai-assistant.git  
   cd whatsapp-ai-assistant  

2. Create .env file or use Replit Secrets:

WHATSAPP_TOKEN=your_meta_token_here  
PHONE_NUMBER_ID=your_whatsapp_phone_number_id  
GEMINI_API_KEY=your_google_gemini_api_key  

3. Install dependencies:
   pip install -r requirements.txt  

4. Run FastAPI server:
   uvicorn main:app --host 0.0.0.0 --port 8000  

---

## 🌐 Webhook Setup (Meta WhatsApp Cloud API)

1. Go to https://developers.facebook.com/  
2. Create an app → Add WhatsApp product  
3. Use the webhook URL and token during setup:  
   - https://your-replit-url/webhook  
   - Verify token: freshly_verify_token  
4. Add webhook field: messages  
5. Send a message to your test number  
6. Bot will auto-reply using Gemini  

---

## 💡 Example AI Prompt

You are a helpful customer support assistant for a skincare brand called Freshly Beauty Products. Respond politely, informatively, and in simple Urdu...

(Product list, delivery info, return policy, etc.)

---

## 📸 Demo Screenshot

(Add WhatsApp screenshot or console output here later)

---

## 🧾 License

MIT — Free to use, modify, and distribute.

---

## ✨ Credits

Built with ❤️ by [Your Name](https://github.com/mhamza062)  
Skincare brand: https://freshly.com.pk
