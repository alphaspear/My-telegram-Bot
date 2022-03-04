from distutils.util import subst_vars
import subprocess
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi ' + update.message.from_user['first_name'])

def get_ip(update, context):
    """Sends IP address to the user"""
    cmd = "asasas"
    output = subprocess.getstatusoutput(cmd)
    update.message.reply_text(output)
     
def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def process_commands(update, context):    
    """Process the user message."""
    command=update.message.text
    print(command)
    print(type(command))
    output = str(subprocess.getstatusoutput(command))
    update.message.reply_text(output.rstrip(','))

def main():
    updater = Updater("1960148809:AAEOLVulnMwGqkV1cX4sbHpefiWPVUexTvI", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, process_commands))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

