from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6799250953:AAF3WsUC9gFfO_R6USYG42rxzzNCyw_r3nQ'
# Replace 'YOUR_CHANNEL_ID' with your actual channel ID
CHANNEL_ID = '@billabombay'

def start(update: Update, context: CallbackContext) -> None:
    # Handle the /start command
    update.message.reply_text('Welcome! I am your channel bot.')

def goodbye_user(update: Update, context: CallbackContext) -> None:
    # Check if the update indicates a user leaving the channel
    if update.message.left_chat_member:
        user = update.message.left_chat_member
        context.bot.send_message(chat_id=user.id, text='Goodbye! We will miss you.')

def main():
    # Create the Updater with your bot token
    updater = Updater(token=BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))

    # Register message handler
    dp.add_handler(MessageHandler(Filters.status_update.left_chat_member, goodbye_user))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
