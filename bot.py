from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
from main import download_mp3

load_dotenv()
BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
BOT_USERNAME = '@youtube_to_mp3_downloadBot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Send your youtube video)')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Just copy the link (URL) of the video and send it here!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is custom command')


# Responses

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    if "youtu" not in url:
        await update.message.reply_text("Send a valid YouTube link")
        return

    await update.message.reply_text("⏳ Downloading MP3...")

    loop = asyncio.get_running_loop()

    mp3_path = await loop.run_in_executor(
        None,
        download_mp3,
        url
    )

    with open(mp3_path, "rb") as audio:
        await update.message.reply_audio(
            audio=audio,
            caption="🎵 Here is your MP3"
    )


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


print("Starting bot...")
app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_error_handler(error)

print("Polling...")
app.run_polling(poll_interval=3)

    