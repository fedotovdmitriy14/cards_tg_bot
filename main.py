import os
import random
import pip
pip.main(['install', 'pytelegrambotapi'])
pip.main(['install', 'telebot'])
import telebot


bot = telebot.TeleBot('7126010209:AAE_XO_d2rM-lfpfQxcFGC_YhyZlMFPu2V8')


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_save = telebot.types.InlineKeyboardButton(
        text="Вытащить карту")
    keyboard.add(button_save)
    bot.send_message(chat_id,
                     'Добро пожаловать в метафорические карты',
                     reply_markup=keyboard)


@bot.message_handler(
    func=lambda message: message.text == 'Вытащить карту')
def pick_card(message):
    random_picture_number = random.randint(1, 35)
    picture_path = f"{random_picture_number}.jpeg"
    if os.path.exists(picture_path):
        with open(picture_path, 'rb') as picture:
            bot.send_photo(message.chat.id, picture)
    else:
        bot.send_message(message.chat.id, "Нет подходящих карт")


if __name__ == '__main__':
    bot.polling(non_stop=True, interval=0)
