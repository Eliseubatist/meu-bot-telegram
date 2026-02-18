import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bot Online!")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    await update.message.reply_text(f"Você disse: {texto}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

app.run_polling()
