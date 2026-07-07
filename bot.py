import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import Config
from handlers import start, help_cmd, handle_message, handle_voice

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def run_bot():
    app = ApplicationBuilder().token(Config.TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))

    if Config.WEBHOOK_URL:
        await app.initialize()
        await app.bot.set_webhook(url=f"{Config.WEBHOOK_URL}/webhook")
        # Start webhook server logic here...
    else:
        print("Starting in Polling Mode...")
        await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_bot())
