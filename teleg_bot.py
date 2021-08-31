import time
import telebot
from helphub_api_wrappers import *
import os

teleg_token=os.environ['TELEG_TOKEN']

tokens={}
bot = telebot.TeleBot(teleg_token)

@bot.message_handler(commands=['auth'])
def auth(message):

    if(len(message.text.split()) != 3):
        bot.reply_to(message, "Неверный формат строки")
        return
    
    auth=do_auth(message.text.split()[1],message.text.split()[2])
    if not auth: 
         bot.reply_to(message, "Ошибка сервиса")
         return

    if("token" not in auth): 
        bot.reply_to(message, "Неверный логин/пароль")
        return

    tokens[message.from_user.username]=auth['token']
    bot.reply_to(message, "Вход выполнен")
        

@bot.message_handler(commands=['requests'])
def send_requests(message):
    if (message.from_user.username not in tokens):
        bot.reply_to(message, "Вход не выполнен. Выполните вход")
        return

    reqs=get_reqs(tokens[message.from_user.username])
    if not reqs:
        bot.reply_to(message, "Ошибка сервиса")
        return

    for req in reqs:
        bot.send_message(message.chat.id,"Заголовок: "+req['title']+"\nТекст: "+req['comment']+"\nСтатус: "+req['state']+"\nТелефон модератора: "+req['creator_phone'])

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "Выполните вход с помощью /auth <username> <password>.\n./requests для получения списка заявок")

while True:
    try:
      bot.polling(none_stop=True)
    except: 
      time.sleep(5)