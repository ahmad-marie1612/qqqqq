
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import telegram
from telebot import types
token="7644799463:AAFqhfTFKPdRhlBVunM9BqKIqvilHAZB8ZU"
bot= telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'أهلا بكم في بوت أحمد مرعي الأول')
    id=message.chat.id
    firstname=message.from_user.first_name
    lastname=message.from_user.last_name
    username=message.from_user.username
    if username ==None:
        username='-----'
    else:
        username=message.from_user.username
    if lastname !=None:
        fullname=f'{firstname} {lastname}'
    else:
        fullname=f'{firstname}'
    bot.send_message(6182798160,
    f'''  
◀◀◀◀◀◀ NEW ▶▶▶▶▶▶
⏺ Hi {firstname}
⏺ ID : {id}
⏺ First Name : {firstname}
⏺ Last Name : {lastname}
⏺ Full Name : {fullname}
⏺ User Name : @{username}
◀◀◀◀◀◀ END ▶▶▶▶▶▶
        ''')
bot.polling()
