import logging
from telegram.ext import Updater, CommandHandler, MessageHandler
import datetime

logging.basicConfig(level=logging.INFO)

TOKEN = '7318751887:AAH4KWmRcBGdxy2946VvZ3NqmsDW4SwtFSk'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to the XAU/USD trading signals bot!')

def send_signal(update, context):
    # Implement your trading strategy here
    # For example, you can use a technical indicator to generate a buy signal
    if rsi_14 > 70:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Buy signal: XAU/USD is overbought! ({current_time})')
    elif rsi_14 < 30:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Sell signal: XAU/USD is oversold! ({current_time})')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, send_signal))

    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
