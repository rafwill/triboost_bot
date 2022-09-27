#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position


# ===================================================================
# Author: Rafael Fernández Sánchez
# Email: rafwill2@gmail.com
# Github: @rafwill
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rafael Fernández. Any
# explicit usage of this script or its contents is granted
# according to the public domain under the CC0 license.
#
# Implemented follow guidelines in PTB (Python Telegram Bot)
#
# Simple Bot to reply to Telegram messages in Triboost telegram chat.
# ===================================================================


from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, Updater, CallbackContext
from text import *
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

import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Useful variables for bot
TOKEN = "5787135370:AAGq-UF0eqSyO012pMTNJQBGuZU6rMqi9bw"
chat_id = 100153954924


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

async def umbrales(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Consulta el siguiente Excel para calcular tus umbrales: https://docs.google.com/spreadsheets/d/1DwEN1k5LJ_MhEZYYcES20x1RYpUztg0Ug64zx4Erq80/edit?usp=sharing.")
       
async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Mensajes importantes.")   

async def entrenamientodeldia(update: Update, context: CallbackContext) -> None:

    keyboard = [
     [
        InlineKeyboardButton("Lunes", callback_data='1'),
        InlineKeyboardButton("Martes", callback_data='2'),
        InlineKeyboardButton("Miércoles", callback_data='3'),
        InlineKeyboardButton("Jueves", callback_data='4'),
        InlineKeyboardButton("Viernes", callback_data='5'),
        InlineKeyboardButton("Sábado", callback_data='6'),
     ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Elije el día de la semana para consultar que entrenamientos dirigidos tenemos", reply_markup=reply_markup)
    
async def localizaciones(update: Update, context: CallbackContext) -> None:

    keyboard = [
     [
        InlineKeyboardButton("Carrera", callback_data='7'),
        InlineKeyboardButton("Piscina", callback_data='8'),
        InlineKeyboardButton("Ciclismo", callback_data='9'),
     ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Aquí podrás ver todas las localizaciones donde quedamos para hacer los entrenamientos. Puedes consultar las direcciones de las piscinas, del estadio de Vallehermoso así como los puntos de salida de las grupetas ciclistas", reply_markup=reply_markup)


async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    # This will define which button the user tapped on (from what you assigned to "callback_data". As I assigned them "1" and "2"):
    choice = query.data
    
    # Now u can define what choice ("callback_data") do what like this:
    if choice == '1':
        await update.callback_query.edit_message_text(lunes_text)
    if choice == '2':
        await update.callback_query.edit_message_text(martes_text)
    if choice == '3':
        await update.callback_query.edit_message_text(miercoles_text)
    if choice == '4':
        await update.callback_query.edit_message_text(jueves_text)
    if choice == '5':
        await update.callback_query.edit_message_text(viernes_text)
    if choice == '6':
        await update.callback_query.edit_message_text(sabado_text)
    if choice == '7':
        await update.callback_query.edit_message_text(localizacionescarrera)
    if choice == '8':
        await update.callback_query.edit_message_text(localizacionespiscina)
    if choice == '9':
        await update.callback_query.edit_message_text(localizacionesciclismo)
       
      
    
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
    application.add_handler(CallbackQueryHandler(button))
    

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()