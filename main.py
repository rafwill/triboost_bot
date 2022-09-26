#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.
# Implemented follow guidelines in PTB (Python Telegram Bot)

"""

Simple Bot to reply to Telegram messages in Triboost telegram chat.
If you have any question please write to @rafwill in Github

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

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes


# Useful variables for bot
TOKEN = "5787135370:AAGq-UF0eqSyO012pMTNJQBGuZU6rMqi9bw"
chat_id = 100153954924
startmessage = (
    "Soy Tribot, tu asistente virtual.\n\n" 
    "Intentaré ayudarte en las preguntas que te haces día"
    " a día. Por ejemplo, me puedes preguntar que entrenamiento" 
    " presencial hay cada dia, donde está la piscina del centro"
    " deportivo Amorós y otras cosas que iras descubriendo"
    " dentro de poco.\n\n"
    "Para saber que puedo hacer, pon en tu teclado /help\n\n"
    "Si descubres que estoy funcionando mal o tienes alguna "
    "sugerencia, puedes ponerte en contacto con @rafwill,"
    " mi hacedor. Si tienes dudas acerca del club escríbenos a "
    " hola@triboost.club. Para todo lo demás...google es"
    " tu amigo."
)
help_text = (
    "Aquí puedes ver los comandos que te ayudaran a interactuar "
    "conmigo, tribot. \n\nComandos:\n\n"
    "/help - Este mensaje\n"
    "/start - Mensaje de Bienvenida\n"
    "/entrenamientodeldia - Elije el día de la semana para "
    " consultar que entrenamientos dirigidos tenemos\n"
    "/localizaciones - Aquí podrás ver todas las localizaciones "
    " donde quedamos para hacer los entrenamientos. Puedes "
    " consultar las direcciones de las piscinas, o del estadio de "
    " Vallehermoso así como los puntos de salida de las grupetas ciclistas\n"
    "/umbrales - Localización del Excel para calcular tus umbrales\n"
    "/noticias - Mensajes importantes\n"
)
#lunes_text =("Los Lunes tenemos los siguientes entrenamientos dirigidos: \n\nNATACIÓN PRADILLO \n2 calles / 12 triboosters \n🕢 15:00h \n📍 Piscina PRADILLO \n\nNATACIÓN OCHOA \n3 calles / 24 triboosters \n🕢 20:00h \n📍 Piscina OCHOA \n\nRUNNING MADRID RIO \n🕢 19:50h \n🏃🏽 20:00 \n📍 CASA DEL RELOJ")

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


#Principal commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    logger.info("user: %s", user)
    chat_id = update.effective_chat.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username
    await context.bot.sendMessage(chat_id, text=f"Hola {username}! {startmessage}")
          
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(help_text)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Lo siento, no entiendo este comando.")

#Secondary commands
async def localizaciones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Aquí podrás ver todas las localizaciones donde quedamos para hacer los entrenamientos. Puedes consultar las direcciones de las piscinas, del estadio de Vallehermoso así como los puntos de salida de las grupetas ciclistas.", reply_markup=ReplyKeyboardMarkup(buttons))

async def umbrales(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Consulta el siguiente Excel para calcular tus umbrales: https://docs.google.com/spreadsheets/d/1DwEN1k5LJ_MhEZYYcES20x1RYpUztg0Ug64zx4Erq80/edit?usp=sharing.")
    
async def entrenamientodeldia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Elije el día de la semana para consultar que entrenamientos dirigidos tenemos.")    
    
async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Mensajes importantes.")   
    

#Test botones
async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")
    
    
def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()
    
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))    
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("localizaciones", localizaciones))
    application.add_handler(CommandHandler("umbrales", umbrales))
    application.add_handler(CommandHandler("entrenamientodeldia", entrenamientodeldia))
    application.add_handler(CommandHandler("noticias", noticias))
    
    
    # Other handlers
    #application.add_handler(MessageHandler(filters.COMMAND, unknown)) # este mensaje choca con los botones
    application.add_handler(CommandHandler("test", test))
    application.add_handler(CallbackQueryHandler(button))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()