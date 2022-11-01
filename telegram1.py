# # ###Сфайт онлайн магазин----диалог---
# import telebot
# from telebot import types
# from config import token

# bot = telebot.TeleBot(token)
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplkeyboardMarkup(resize_keyboard =True)
#     item1 = types.KeyboardButton('Зимные куртки женские')
#     item2 = types.KeyboardButton('Зимные куртки мужские')
#     item3= types.KeyboardButton('Зимные куртки дедские')
#     item4= types.KeyboardButton('Другие')
# # bot.polling(none_stop=True)
#     markup.add(item1, item2,item3,item4)
#     bot.send_message(message.chat.id, 'Привет , {message.from_user.first_name}', reply_markup = markup)
# bot.polling(non_stop = True)
# # @bot.message_handler(content_types=['text'])
# def bot_message(message):
#     if message.chat.type == 'private':
#         if message.text == 'Зимные куртки женские':
#              bot.send_message(message.chat.id, 'Короткие' + 'Длинные')  # v mesto + or budet 
#              if message.text == 'photo':
#                 photo = open('5189267.jpg', 'rb')
#                 bot.send_message(message.chat.id, photo)
#     elif message.text ==  'Зимные куртки мужские':
#           bot.send_message(message.chat.id, 'Короткие' + 'Длинные')     
#     else:
#          bot.send_photo(message.chat.id, 'wow klassno', parse_mode='html') 
# bot.polling(none_stop=True) 
# # @bot.message_handler()
# def get_user_text(message):
#     if message.text == 'Привет':
#         bot.send_message(message.chat.id, '<b>ИИИИ тебе привет</b>', parse_mode='html')
#     elif message.text == 'фото':
#         photo = open('1122.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#    3 else:
#         bot.send_photo(message.chat.id, 'Ясно', parse_mode='html')

# @bot.message_handler()
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'Hi', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('5189267.jpg', 'rb')
#         bot.send_message(message.chat.id, photo) 
#     else:
#          bot.send_photo(message.chat.id, 'wow klassno', parse_mode='html')

# bot.polling(none_stop=True)

##########
# import telebot
# from config import token
# from telebot import types

# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
# def start(message):

#  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#  item1 = types.KeyboardButton('Выбрать модель...')
#  item2 = types.KeyboardButton('Тест-Драйв')
#  markup.add(item1, item2)
#  bot.send_message(message.chat.id, 'Добрый день!. Рады приветсвовать вас в нашем автосалоне "Audi"', reply_markup=markup)
#  bot.send_message(message.chat.id, 'С чем вам помочь?', reply_markup=markup)
# @bot.message_handler(content_types = ['text'])
# def bot_message(message):
#     if message.chat.type == 'private':
#         if message.text == 'Выбрать модель...':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#             bot.send_message(message.chat.id, 'Пожалуйста, выберите категорию автомобиля.' )
#             n1 = types.KeyboardButton('Audi A3 Sedan year 2021')
#             n2 = types.KeyboardButton('Audi Q7')
#             n3 = types.KeyboardButton('Audi A5')
#             markup.add(n1, n2, n3)
#             bot.send_message(message.chat.id, 'Выбрать модель...', reply_markup=markup)

#         elif message.text == 'Audi A3 Sedan year 2021':
#             bot.send_message(message.chat.id, 'Audi A3 Sedan 2021 создан, чтобы дарить удовольствие от езды, удивлять, привлекать внимание окружающих. Каждая деталь стильного, динамичного и маневренного автомобиля указывает на его принадлежность к премиум-классу. Инновационные решения гарантируют комфорт управления и беспрецедентную безопасность.')
#             photo = open('111.jpeg', 'rb')
#             photo2 = open('222.jpeg', 'rb')
#             photo3 = open('333.jpeg', 'rb')
#             bot.send_photo(message.chat.id, photo)
#             bot.send_photo(message.chat.id, photo2)
#             bot.send_photo(message.chat.id, photo3)
#         elif message.text == 'Audi Q7':
#             bot.send_message(message.chat.id, 'Новый Audi Q7 2020 года создан разрушать \
#                 границы путешествий, дарить полную свободу комфорта. Автомобиль каждой деталью излучает\
#                 мощь и динамику, при этом поражает изысканной элегантностью. Он прекрасен не только снаружи, \
#                 но и внутри, обеспечивая максимум условий для наслаждения любым мгновением поездки.\
#                 1 Бездорожье является его стихией, о чем свидетельствует большой дорожный просвет в сочетании с полным приводом.\
#                 В то же время, благодаря расширенному набору опциональных настроек, внедорожник отлично приспособлен к городским условиям.\
#                 Узнайте больше о возможностях и новых технологиях.')
#             photo = open('', 'rb')
#             photo2 = open('', 'rb')
#             photo3 = open('', 'rb')
#             bot.send_photo(message.chat.id, photo)
#             bot.send_photo(message.chat.id, photo2)
#             bot.send_photo(message.chat.id, photo3)
# bot.polling(none_stop=True)
# import telebot
# from config import token
# from telebot import types

# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
# def start(message):

#  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#  item1 = types.KeyboardButton('Выбрать католог...')
#  item2 = types.KeyboardButton('Тест-Драйв')
#  markup.add(item1, item2)
#  bot.send_message(message.chat.id, 'Добрый день!. Рады приветсвовать вас в нашем онлайн магазин "Shop.kg"', reply_markup=markup)
#  bot.send_message(message.chat.id, 'С чем вам помочь?', reply_markup=markup)
# @bot.message_handler(content_types = ['text'])
# def bot_message(message):
#     if message.chat.type == 'private':
#         if message.text == 'Выбрать католог...':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#             bot.send_message(message.chat.id, 'Пожалуйста, выберите катологи одежды.' )
#             n1 = types.KeyboardButton('Женские одежды')
#             n2 = types.KeyboardButton('Мужские одежды')
#             n3 = types.KeyboardButton('Дедские одежды')
#             markup.add(n1, n2, n3)
#             bot.send_message(message.chat.id, 'Выбрать католог...', reply_markup=markup)

#         elif message.text == 'Женские одежды':
#             photo = open('123.jpg', 'rb', '2300 som')
#             photo2 = open('128.jpg', 'rb', '2800 som')
#             photo3 = open('129.jpg', 'rb', '3000 som')
#             bot.send_photo(message.chat.id, photo)
#             # bot.send_message(message.chat.id, '1. Цена = 15000', reply_markup=markup)
#             bot.send_photo(message.chat.id, photo2)
#             bot.send_photo(message.chat.id, photo3)
#         elif message.text == 'Мужские одежды': 
#             photo = open('345.jpg', 'rb')
#             photo2 = open('10.jpg', 'rb')
#             photo3 = open('098.jpg', 'rb')
#             bot.send_photo(message.chat.id, photo, '1500 сом')
#             bot.send_photo(message.chat.id, photo2, '2500 сом' )
#             bot.send_photo(message.chat.id, photo3, '3000 сом')
#         elif message.text ==  'Дедские одежды':
#             photo = open('byby.jpg', 'rb')
#             # photo2 = open('bybe2.jpg', 'rb')
#             photo3 = open('bybe3.jpg', 'rb')
#             bot.send_photo(message.chat.id, photo, '1500 сом')
#             bot.send_photo(message.chat.id, photo3, '1300 сом')
#             bot.send_message(message.chat.id, 'Какую одежду выбрали?)' )
#     if message.text ==  'Дедские одежды, photo3':
#             n1 = types.KeyboardButton('Женские одежды')
#             n2 = types.KeyboardButton('Мужские одежды')
#             n3 = types.KeyboardButton('Дедские одежды')
#             markup.add(n1, n2, n3)
#             bot.send_message(message.chat.id, 'Вы уверенны? Может еще раз посмотрите?...', reply_markup=markup)
        

#     # bot.send_message(message.chat.id, 'Вот эту?)' ) 

# bot.polling(none_stop=True)
########
import telebot
from config import token
from telebot import types

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('Хотите выбирать кофе?.')
    item2 = types.KeyboardButton('Да хочу кофе')
    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Хотите выбирать кофе?', reply_markup=markup)
@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
            if message.text == 'Да хочу кофе' :
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                n1 = types.KeyboardButton('Экспрессо')
                n2 = types.KeyboardButton('Американо')
                n3 = types.KeyboardButton('Капучино')
                n4 = types.KeyboardButton('Лате')
                markup.add(n1, n2, n3, n4)
                bot.send_message(message.chat.id, 'Выбрайте кофе', reply_markup=markup)
            elif message.text == 'Экспрессо': 
                photo = open('4.jpg', 'rb')
                photo2 = open('03.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, '76 som')
                bot.send_photo(message.chat.id, photo2,  '96 som')
                # bot.send_message(message.chat.id, 'Да пожалуйста', reply_markup=markup)
                # bot.send_message(message.chat.id, 'Нет извините', reply_markup=markup)
            elif message.text == 'Американо': 
                photo = open('amerik02.jpg', 'rb')
                photo2 = open('amerik03.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, '0,2, 68 som')
                bot.send_photo(message.chat.id, photo2,'0.3, 84 som')
                # bot.send_message(message.chat.id, 'Да пожалуйста', reply_markup=markup)
                # bot.send_message(message.chat.id, 'Нет извините', reply_markup=markup)
            elif message.text == 'Капучино': 
                photo2 = open('kapi03.jpg', 'rb')
                photo3 = open('kapi05.jpg', 'rb')
                bot.send_photo(message.chat.id, photo2, '0.3, 84 som')
                bot.send_photo(message.chat.id, photo3, '0.5, 110 som') 
                # bot.send_message(message.chat.id, 'Да пожалуйста', reply_markup=markup)
                # bot.send_message(message.chat.id, 'Нет извините', reply_markup=markup)
            elif message.text == 'Лате': 
                photo = open('late235.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, '45 som, 68 som, 120  som')
               
#                 bot.send_message(message.chat.id, 'Да пожалуйста', reply_markup=markup)
#                 bot.send_message(message.chat.id, 'Нет извините', reply_markup=markup)
bot.polling(none_stop=True)
