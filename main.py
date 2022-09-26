#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""

Simple Bot to reply to Telegram messages in Triboost telegram chat.

"""


import logging

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

from telegram import Update
from telegram.ext import filters, MessageHandler, Application, CommandHandler, ContextTypes

# Useful variables for bot
TOKEN = "5787135370:AAGq-UF0eqSyO012pMTNJQBGuZU6rMqi9bw"
chat_id = 100153954924

startmessage = (
    "Aquí puedes ver los comandos que te ayudaran a interactuar "
    "conmigo, tribot. Si tienes cualquier duda acerca de mi "
    " funcionamiento puedes ponerte en contacto con @rafwill."
    " Si tienes dudas acerca del club escribenos a "
    " hola@triboost.club. Para todo lo demás...google es"
    " tu amigo. \n\nComandos:\n\n"
)


help_text = (
    "Aquí puedes ver los comandos que te ayudaran a interactuar "
    "conmigo, tribot. Si tienes cualquier duda acerca de mi "
    " funcionamiento puedes ponerte en contacto con @rafwill."
    " Si tienes dudas acerca del club escribenos a "
    " hola@triboost.club. Para todo lo demás...google es"
    " tu amigo. \n\nComandos:\n\n"
    "/start - Mensaje de Bienvenida\n"
    "/entrenamientodeldia - Elije el día de la semana para "
    " consultar que entrenamientos dirigidos tenemos\n"
    "/localizaciones - Aquí podrás ver todas las localizaciones "
    " donde quedamos para hacer los entrenamientos. Puedes "
    " consultar las direcciones de las piscinas, del estadio de "
    " Vallehermoso así como los puntos de salida de las grupetas ciclistas\n"
    "/umbrales - Localización del Excel para calcular tus umbrales\n"
    "/noticias - Mensajes importantes\n"
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    logger.info("user: %s", user)
    #knows chat_id
    chat_id = update.effective_chat.id
    #print(chat_id)
    #await update.message.reply_html(
    #    rf"Hola {user.mention_html()}!", 
        #reply_markup=ForceReply(selective=True),e
    #)
    first_name = update.effective_user.first_name
    username = update.effective_user.username
    await context.bot.sendMessage(chat_id, text=f"Bienvenido {username}. {startmessage}")
    #await context.bot.sendMessage(chat_id, text=f'Bienvenido {username}.'+f'{startmessage}')
    #await context.bot.sendMessage(chat_id, text=f'{startmessage}', parse_mode='Markdown')
    #context.bot.sendMessage(chat_id = update.message.chat_id, text = f"{utente.Username} è ora {getPermessi()[str(utente.Autorizzazione)]}")
    
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(help_text)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Lo siento, no entiendo este comando.")


    
if __name__ == '__main__':
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()
    
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))    
    application.add_handler(CommandHandler("help", help_command))
    
    
    # Other handlers
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()
