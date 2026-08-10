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
        
        welcome_text = (
        "Welcome to Forex Global Trading 📈\n\n"
        "Are you looking to learn crypto trading strategies and get daily market insights for free? "
        "You are in the right place!\n"
        "We break down complex market movements to help you understand:\n\n"
        "When to Buy & Sell – Clear entry and exit points for optimal trades.\n"
        "Token Analysis – In-depth research on high-potential coins.\n"
        "Risk Management – Essential rules to protect and grow your capital.\n\n"
        "Everything is thoroughly analyzed by our team before sharing with you—100% Free!\n\n"
        "👇 Click the button below to join our official channel: 👇"
    )

    
    keyboard = [
        [InlineKeyboardButton("📢 Join Free Channel", url="https://t.me/GoldMarketAnalysis01")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)
    
    
    asyncio.create_task(send_scheduled_content(chat_id, context))

async def send_scheduled_content(chat_id: int, context: ContextTypes.DEFAULT_TYPE):
    try:
     
        await asyncio.sleep(600)
        caption_10m = (
            "🚀 Free AI Analysis & Signals\n\n"
            "Check out our daily market updates in the channel!"
        )
        await context.bot.send_photo(
            chat_id=chat_id,
            photo="https://t.me/starcentre2/5",
            caption=caption_10m,
            parse_mode="Markdown"
        )

        
        await asyncio.sleep(1800)
        caption_30m = (
            "📊 Recent Client Results & Profit Proof!\n\n"
            "Look at how our community members are profiting daily using our free signals.\n"
            "Ready to start earning today?"
        )
        await context.bot.send_photo(
            chat_id=chat_id,
            photo="https://t.me/starcentre2/7?single",
            caption=caption_30m,
            parse_mode="Markdown"
        )

    except Exception as e:
        print(f"Error sending scheduled messages: {e}")

def main():
    if not TOKEN:
        print("Error: BOT_TOKEN is not set in Environment Variables!")
        return

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()

if name == "main":
    main()
