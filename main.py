import asyncio
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    chat_id = update.effective_chat.id

    welcome_text = (
        f"Hello {user_first_name}! 👋\n\n"
        "Welcome to Forex Global Trading 📈\n\n"
        
        ("Are you looking to learn crypto trading strategies and get daily market insights for free? You are in the right place!
We break down complex market movements to help you understand:

When to Buy & Sell – Clear entry and exit points for optimal trades.
Token Analysis – In-depth research on high-potential coins.
Risk Management – Essential rules to protect and grow your capital.
Everything is thoroughly analyzed by our team before sharing with you—100% Free!

👇 Click the button below to join our official channel: 👇")

    keyboard = [
        [InlineKeyboardButton("📢 Join Free channel", url="https://t.me/GoldMarketAnalysis01")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="HTML")
    asyncio.create_task(send_scheduled_content(chat_id, context))

async def send_scheduled_content(chat_id: int, context: ContextTypes.DEFAULT_TYPE):
    try:
        await asyncio.sleep(600)
        caption_10m = "🚀 **Free AI Analysis & Signals**\n\nCheck out our daily market updates in the channel!"
        await context.bot.send_photo(
            chat_id=chat_id,
            photo="https://t.me/starcentre2/5",
            caption=caption_10m,
            parse_mode="Markdown"
        )

        await asyncio.sleep(3000)
        caption_1h = "📊 **Recent Client Results & Profit Proof!**\n\nReady to start earning today? Join our community now."
        await context.bot.send_photo(
            chat_id=chat_id,
            photo="https://t.me/starcentre2/7?single",
            caption=caption_1h,
            parse_mode="Markdown"
        )
    except Exception as e:
        print(f"Error sending messages: {e}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
    
