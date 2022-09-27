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
lunes_text = ("Los Lunes tenemos los siguientes entrenamientos dirigidos: \n\nNATACIÓN PRADILLO \n2 calles / 12 triboosters \n🕢 15:00h \n📍 Piscina PRADILLO \n\nNATACIÓN OCHOA \n3 calles / 24 triboosters \n🕢 20:00h \n📍 Piscina OCHOA \n\nRUNNING MADRID RIO \n🕢 19:50h \n🏃🏽 20:00 \n📍 CASA DEL RELOJ")
martes_text = ("Los Martes tenemos los siguientes entrenamientos dirigidos: \n\nRUNNING MADRID RIO \n🕢 19:50h \n🏃🏽 20:00 \n📍 CASA DEL RELOJ \n\nNATACIÓN OCHOA \n3 calles / 24 triboosters \n🕢 20:00h \n📍 Piscina OCHOA ")
miercoles_text = ("Los Miércoles tenemos los siguientes entrenamientos dirigidos: \n\nNATACIÓN PRADILLO\n2 calles / 12 triboosters\n🕢 15:00h \n📍 Piscina PRADILLO\n\nNATACIÓN OCHOA \n3 calles / 24 triboosters\n🕢 20:00h\n📍 Piscina OCHOA ")
jueves_text = ("Los Jueves tenemos los siguientes entrenamientos dirigidos: \n\nESTADIO VALLEHERMOSO \n🕢 14:20h \n🏃🏽 14:30h \n📍 VALLEHERMOSO \nRUNNING MADRID RIO \n🕢 19:50h \n🏃🏽 20:00 \n📍 CASA DEL RELOJ \n\nNATACIÓN OCHOA \n3 calles / 24 triboosters \n🕢 20:00h \n📍 Piscina OCHOA ")
viernes_text = ("Los Viernes tenemos los siguientes entrenamientos dirigidos: \n\nNATACIÓN OCHOA \n2 calles / 16 triboosters + 1 calle libre para tiradas libres \n🕢 15:00 nadando cual🦈 \n📍 Piscina OCHOA")
sabado_text = ("Los Sábados tenemos los siguientes entrenamientos dirigidos: \n\nNATACIÓN AMORÓS \n4 calles / 32 triboosters \n🕢 8:00h nadando cual🦈 \n📍 Piscina AMORÓS ")

localizacionescarrera = ("🏃🏽 Localizaciones de actividades de carrera 🏃‍♀️ \n\n📍 CASA DEL RELOJ:\nhttps://goo.gl/maps/sUyxqrjaM4ViMxtR6 \n📍 VALLEHERMOSO:\nhttps://goo.gl/maps/jcbSQxC7xs5DzqNr7")
localizacionespiscina = ("🤿 Localizaciones de las piscinas 🛁 \n\n📍 OCHOA:\nhttps://goo.gl/maps/2zEQi7fVjpsXEsWe6 \n📍 PRADILLO:\nhttps://goo.gl/maps/wM2h4yni69mS1AMw6 \n📍 AMORÓS:\nhttps://g.page/centrodeportivoamoros?share")
localizacionesciclismo = ("🚴‍♂️ Puntos de quedadas ciclistas 🚴‍♀️ \n\n📍 Parking Triboost:\nhttps://goo.gl/maps/nggsGR5TyWvAcG7H6 \n📍 Parking Perales del Rio:\nhttps://goo.gl/maps/t93teGGmatdfEfcA6 \n📍 Parking Colonia Jardín:\nhttps://goo.gl/maps/MM9UWbAVLQg1tQMh6 \n📍 Parking Soto del Real:\nhttps://goo.gl/maps/JHePtF6V7outSmVY7 \n📍 Parking Polígono Amazon:\nhttps://goo.gl/maps/UUK4oQDiDdpoaNBaA \n📍 Parking San Martín de la Vega:\nhttps://goo.gl/maps/jwQHsUZL4mVadyaW9")
