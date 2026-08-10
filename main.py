import asyncio
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# Render Web Service-এর Port Timeout আটকানোর জন্য ওয়েব সার্ভার
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def start_health_check_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    welcome_text = """Welcome to Forex Global Trading 📈

Are you looking to learn crypto trading strategies and get daily market insights for free? You are in the right place!
We break down complex market movements to help you understand:

When to Buy & Sell – Clear entry and exit points for optimal trades.
Token Analysis – In-depth research on high-potential coins.
Risk Management – Essential rules to protect and grow your capital.
Everything is thoroughly analyzed by our team before sharing with you—100% Free!

👇 Click the button below to join our official channel: 👇"""

    keyboard = [
        [InlineKeyboardButton("📢 Join Free Channel", url="https://t.me/GoldMarketAnalysis01")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)
    asyncio.create_task(send_scheduled_content(chat_id, context))

async def send_scheduled_content(chat_id: int, context: ContextTypes.DEFAULT_TYPE):
    try:
        # ১০ মিনিট (৬০০ সেকেন্ড)
        await asyncio.sleep(600)
        caption_10m = "🚀 Free AI Analysis & Signals\n\nCheck out our daily market updates in the channel!"
        await context.bot.send_photo(
            chat_id=chat_id,
            photo="https://t.me/starcentre2/5",
            caption=caption_10m
        )

        # ৩০ মিনিট (১৮০০ সেকেন্ড)
        await asyncio.sleep(1800)
        caption_30m = "📊 Recent Client Results & Profit Proof!\n\nLook at how our community members are profiting daily using our free signals.\nReady to start earning today?"
        await context.bot.send_photo(
            chat_id=chat_id,
            photo="https://t.me/starcentre2/7?single",
            caption=caption_30m
        )

    except Exception as e:
        print(f"Error: {e}")

def main():
    if not TOKEN:
        print("Error: BOT_TOKEN Environment Variable is missing!")
        return

    # পোর্ট সার্ভার ব্যাকগ্রাউন্ডে চালু করা
    threading.Thread(target=start_health_check_server, daemon=True).start()

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
    
