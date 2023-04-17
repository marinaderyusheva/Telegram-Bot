import telebot
import webbrowser
from telebot import types
import sqlite3
bot = telebot.TeleBot('6128166293:AAEB6OzAhR3YgXpp0wK1QLZIZBYXytCKdEA')
name = None


# обработчик фото, аудио и документов
@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message, f'Классное фото, {message.from_user.first_name}!')
@bot.message_handler(content_types=['audio'])
def audio(message):
    bot.reply_to(message, f'Обязательное передам это аудио разработчикам, {message.from_user.first_name}!')
@bot.message_handler(content_types=['document'])
def document(message):
    bot.reply_to(message, f'Обязательное передам этот файл разработчикам, {message.from_user.first_name}!')

# команда для вывода сайта в меню
@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://youtube.com')


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Задать вопрос', callback_data='ask')
    btn3 = types.InlineKeyboardButton('Регистрация', callback_data='register')
    markup.row(btn2, btn3)
    btn4 = types.InlineKeyboardButton('Часто задаваемые вопросы', callback_data='help')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)

# обработчик кнопок
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    match callback.data:
        case 'site':
            webbrowser.open('https://youtube.com')
        case 'ask':
            bot.send_message(callback.message.chat.id, 'С радостью отвечу на интересующие тебя вопросы!')
        case 'register':
            bot.send_message(callback.message.chat.id, f'Давай зарегистрируем тебя в нашей системе!')
        case 'help':
            markup = types.InlineKeyboardMarkup()
            qstn1 = types.InlineKeyboardButton('Для чего эта платформа?', callback_data='qstn1')
            markup.row(qstn1)
            qstn2 = types.InlineKeyboardButton('Направления работы', callback_data='qstn2')
            markup.row(qstn2)
            qstn3 = types.InlineKeyboardButton('За какое время я найду работу?', callback_data='qstn3')
            markup.row(qstn3)
            qstn4 = types.InlineKeyboardButton('Компании, с которыми мы работаем', callback_data='qstn4')
            markup.row(qstn4)
            qstn5 = types.InlineKeyboardButton('Платная ли платформа?', callback_data='qstn5')
            markup.row(qstn5)
            bot.send_message(callback.message.chat.id, 'Часто задаваемые вопросы', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    match callback.data:
        case 'qstn1':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site')
            btn3 = types.InlineKeyboardButton('Регистрация', callback_data='register')
            markup.row(btn1, btn3)
            bot.send_message(callback.message.chat.id, 'EASYJOB - платформа, предоставляющая легкий поиск вакансий и работников в вашу команду🤓 '
                                 'Мы работаем по 3 направлениям: маркетинг, дизайн и программирование. '
                                 'Если тебе это подходит, то предлагаем присоединиться к нашей большой семье!', reply_markup=markup)
        case 'qstn2':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Программирование', callback_data='about_sphere1')
            btn2 = types.InlineKeyboardButton('Дизайн', callback_data='about_sphere2')
            btn3 = types.InlineKeyboardButton('Маркетинг', callback_data='about_sphere3')
            markup.row(btn1, btn2, btn3)
            bot.send_message(callback.message.chat.id, 'Мы работаем по 3 направлениям: маркетинг, дизайн и программирование. О каких тебе было бы интересно узнать больше?', reply_markup=markup)
        case 'qstn3':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site')
            markup.row(btn1)
            bot.send_message(callback.message.chat.id, 'Найти работу на нашей платформе можно за 15 минут!', reply_markup=markup)
        case 'qstn4':
            bot.send_message(callback.message.chat.id, 'Помимо частных работодателей мы сотрудничаем также с крупными компаниями, как: ASUS, Ашан, Sofoil и многие другие')
        case 'qstn5':
            bot.send_message(callback.message.chat.id, 'Платформа для фрилансеров и работодателей бесплатная. Мы получаем деньги с рекламы, расположенной на сайте.')

# обработка обычного текста
@bot.message_handler()
def info(message):
    match message.text.lower():
        case 'привет':
            bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
        case 'id':
            bot.reply_to(message, f'Ваш ID: {message.from_user.id}')
        case 'сайт':
            bot.reply_to(message, 'https://youtube.com')
        case ('Как зарегистрироваться' | 'регистрация'):
            bot.reply_to(message, 'Давай зарегистрируем тебя')
        case ('для чего эта платформа?' | 'для чего эта платформа' | 'зачем мне эта платформа' | 'что можно делать'):
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site')
            btn3 = types.InlineKeyboardButton('Регистрация', callback_data='register')
            markup.row(btn1, btn3)
            bot.reply_to(message,'EASYJOB - платформа, предоставляющая легкий поиск вакансий и работников в вашу команду🤓 '
                                 'Мы работаем по 3 направлениям: маркетинг, дизайн и программирование. '
                                 'Если тебе это подходит, то предлагаем присоединиться к нашей большой семье!',
                         reply_markup=markup)
        # обработчик ошибки
        case _:
            bot.send_message(message.chat.id, 'Попробуй еще раз')


# программа работает постоянно
bot.polling(none_stop=True)


'''
@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Задать вопрос")
    markup.add(item1)
    bot.send_message(message.chat, id, 'Выберите, что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Задать вопрос':
        bot.send_message(message.chat.id, "https://youtube.com")


'''

'''
# декоратор для кнопок под текстом
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardMarkup('Задать вопрос')
    # создаем ряд для кнопки
    #markup.add(btn1)
    #btn2 = types.KeyboardButton('Зарегистрироваться')
    #btn3 = types.KeyboardButton('Перейти на сайт')
    #markup.add(btn2)
    #markup.add(btn3)
    # отправляем пользователю фото с методом открытия rb - read
    # file = open('./logo.jpg', 'rb')
    # bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    # регистрируем функцию, которая срабатывает при нажатии
    bot.register_next_step_handler(message, on_click)


# функция, срабатывающая при нажатии на кнопки и введет текст кнопок
def on_click(message):
    if message.text == 'Задать вопрос':
        bot.send_message(message.chat.id, 'Буду рад ответить на ваш вопрос')
    elif message.text == 'Зарегистрироваться':
        bot.send_message(message.chat.id, register(message))
    elif message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, site(message))


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://youtube.com')

# декоратор для обработки файлов - фото
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    # создание inline кнопки(около сообщения)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://youtube.com')
    # создаем ряд для кнопки
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)

@bot.message_handler(commands=['register'])
def register(message):
    # подключаемся к бд
    conn = sqlite3.connect('bottg.sql')
    cur = conn.cursor()
    #выполняем SQL команду
    cur.execute('CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50), pass varchar(50))')
    #запись в бд
    conn.commit()
    #закрываем связь с бд
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Давай зарегистрируем тебя! Введите свое имя:')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль:')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    # регистрируем пользователя
    conn = sqlite3.connect('bottg.sql')
    cur = conn.cursor()
    # выполняем SQL команду
    cur.execute("INSERT INTO users (name, pass) VALUES ('%s','%s')" %(name, password))
    # запись в бд
    conn.commit()
    # закрываем связь с бд
    cur.close()
    conn.close()
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Список пользователей', callback_data='user'))
    bot.send_message(message.chat.id, 'Регистрация прошла успешно!', reply_markup=markup)


# декоратор обработки кнопки Список пользователей
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('bottg.sql')
    cur = conn.cursor()
    # выполняем SQL команду
    cur.execute("SELECT * FROM users")
    # функция, возвращающая все записи из бд
    users = cur.fetchall()
    # создаем новую переменную, куда поместим список из элементов бд
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}'
    # закрываем связь с бд
    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)



# обработчик функций callback_data
# func=lambda -анонимная функция
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id)


# меню



# декоратор функции start
@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


# декоратор обычного текста от пользователя
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
        # ответ на предыдущее сообщение
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Ваш ID: {message.from_user.id}')

'''
