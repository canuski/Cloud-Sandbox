#!/usr/bin/python3
import telegram 
import telegram.constants 
import os
# rom dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()

TELEGRAM_BOT_TOKEN = '6730417267:AAHoVCAAI1kywQLDuW-2pHPxrnPLIfv3G0c'
TELEGRAM_CHAT_ID = '-1002102767348'

async def send_telegram_msg(msg):
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    
    # Default formatting
    formatted_msg = f"<b>Virus Scan Results:</b>\n<b>📄File is empty📄</b>\n\n{msg}\n\n" 
    if "FOUND" in msg:
        formatted_msg = f"<b>Virus Scan Results:</b>\n<b>⚠️VIRUS ALERT!⚠️</b>\n\n{msg}\n\n <b>🚨Take imediate action🚨</b>" 
    elif "OK" in msg:
        formatted_msg = f"<b>Virus Scan Results:</b>\n<b>✅File is OK!✅</b>\n\n{msg}\n\n" 
    
    await bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=formatted_msg, parse_mode=telegram.constants.ParseMode.HTML)
