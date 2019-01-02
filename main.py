import telebot
from telebot import apihelper
apihelper.proxy = {'https':'socks5://198.50.217.202:1080'}

bot = telebot.TeleBot("703169405:AAENYrZP3Jt2gE4GVH5zLrcV99sirNzmpe0")


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, """"Команды бота:
/start - Запуск бота
/help - Помощь по командам
/catalog - Каталог в котором можно будет выбрать между категориями 'Животные' и 'Фрукты'
/settings - Выбор режима
/location - Местоположение магазина""")

@bot.message_handler(commands=['settings'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row(u'\U0001F934Оператор', u'\U0001F468Пользователь', u'\U0001F519Назад')
    send = bot.send_message(message.from_user.id,
                            'Выберите режим, если "Оператор", то вы сможете настроить бота, а если "Пользователь", то будете обычным пользователем как и все. ',
                            reply_markup=user_markup)
    bot.register_next_step_handler(send, four)
    bot.register_next_step_handler(send, seven)
@bot.message_handler(commands=['location'])
def handle_text(message):
    bot.send_location(message.from_user.id, 57.997564, 56.265458)
    send = bot.send_message(message.from_user.id, 'Город Пермь, улица Чернышевсткого 28')

@bot.message_handler(commands=['catalog'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row(u'\U0001F43EЖивотные', u'\U0001F349Фрукты', u'\U0001F519Назад')
    send = bot.send_message(message.from_user.id, "Выберите категорию товара!", reply_markup=user_markup)
    bot.register_next_step_handler(send, six)
    bot.register_next_step_handler(send, four)
    bot.register_next_step_handler(send, eight)

@bot.message_handler(commands=['start'])
def one(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row(u'\U0001F4D3Каталог', u'\U00002699Режим')
    user_markup.row(u'\U0001F5FAНаше местоположение')
    send = bot.send_message(message.from_user.id, """Добро пожаловать в магазин Sat.
Здесь вы найдете множество красивых и экзотических животных, а также экзотические фрукты!""", reply_markup=user_markup)
   # bot.register_next_step_handler(send,two)
    #bot.register_next_step_handler(send, one)

@bot.message_handler(content_types=['text'])
def two(message):
    if message.text == u'\U0001F4D3Каталог':
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row(u'\U0001F43EЖивотные', u'\U0001F349Фрукты', u'\U0001F519Назад')
        send = bot.send_message(message.from_user.id, "Выберите категорию товара!", reply_markup=user_markup)
        bot.register_next_step_handler(send, six)
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, eight)
    elif message.text == u'\U00002699Режим':
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row(u'\U0001F934Оператор', u'\U0001F468Пользователь', u'\U0001F519Назад')
        send = bot.send_message(message.from_user.id, 'Выберите режим, если "Оператор", то вы сможете настроить бота, а если "Пользователь", то будете обычным пользователем как и все. ', reply_markup=user_markup)
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, seven)
    elif message.text == u'\U0001F5FAНаше местоположение':
        bot.send_location(message.from_user.id, 57.997564, 56.265458)
        send = bot.send_message(message.from_user.id, 'Город Пермь, улица Чернышевсткого 28')
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, two)

    #elif message.text != u'\U0001F519Назад' and message.text != u'\U0001F43EЖивотные' and message.text != u'\U0001F349Фрукты' and message.text != '/start' and message.text != u'\U0001F934Оператор' and message.text != u'\U0001F468Пользователь' and message.text != '/location' and message.text != '/catalog' and message.text != '/help' and message.text != '/settings':
       # send = bot.send_message(message.chat.id, "ERROR")
@bot.message_handler(content_types=['text'])
def seven(message):
    if message.text == u'\U0001F934Оператор':
        send = bot.send_message(message.from_user.id, 'Ха-Ха, размечтались, идите настраивать меня сюда - @BotFather, но для этого Вам нужен специальный токен, без которого Вы не сможите настроить меня!')
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, seven)
    elif message.text == u'\U0001F468Пользователь':
        send = bot.send_message(message.from_user.id, u'\U0001F926Вы и так пользователь...')
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, seven)

@bot.message_handler(content_types=['text'])
def four(message):
    if message.text == u'\U0001F519Назад':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row(u'\U0001F4D3Каталог', u'\U00002699Режим')
        user_markup.row(u'\U0001F5FAНаше местоположение')
        send = bot.send_message(message.from_user.id, u'\U0001F4DCГлавное меню', reply_markup=user_markup)
        bot.register_next_step_handler(send, two)
        bot.register_next_step_handler(send, four)
    elif message.text != u'\U0001F43EЖивотные' and message.text != u'\U0001F349Фрукты' and message.text != '/start' and message.text != u'\U0001F934Оператор' and message.text != u'\U0001F468Пользователь' and message.text != u'\U0001F4D3Каталог' and message.text != u'\U00002699Режим' and message.text != u'\U0001F5FAНаше местоположение' and message.text != '/location' and message.text != '/catalog' and message.text != '/help' and message.text != '/settings':
        send = bot.send_message(message.chat.id, "ERROR")
        bot.register_next_step_handler(send, six)
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, seven)
        bot.register_next_step_handler(send, eight)
        bot.register_next_step_handler(send, two)
    elif message.text == '/start':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row(u'\U0001F4D3Каталог', u'\U00002699Режим')
        user_markup.row(u'\U0001F5FAНаше местоположение')
        send = bot.send_message(message.from_user.id, """Добро пожаловать в магазин Sat.
Здесь вы найдете множество красивых и экзотических животных, а также экзотические фрукты!""",
                                reply_markup=user_markup)
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, two)
    elif message.text == '/help':
        send = bot.send_message(message.chat.id, "Проверка. Скоро тут будут описание команд!")
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, two)
    elif message.text == '/catalog':
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row(u'\U0001F43EЖивотные', u'\U0001F349Фрукты', u'\U0001F519Назад')
        send = bot.send_message(message.from_user.id, "Выберите категорию товара!", reply_markup=user_markup)
        bot.register_next_step_handler(send, six)
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, eight)
        bot.register_next_step_handler(send, two)
    elif message.text == '/location':
        bot.send_location(message.from_user.id, 57.997564, 56.265458)
        send = bot.send_message(message.from_user.id, 'Город Пермь, улица Чернышевсткого 28')
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, two)
    elif message.text == '/settings':
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row(u'\U0001F934Оператор', u'\U0001F468Пользователь', u'\U0001F519Назад')
        send = bot.send_message(message.from_user.id,
                                'Выберите режим, если "Оператор", то вы сможете настроить бота, а если "Пользователь", то будете обычным пользователем как и все. ',
                                reply_markup=user_markup)
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, seven)
        bot.register_next_step_handler(send, two)
def six(message1):
    if message1.text == u'\U0001F43EЖивотные':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text="Капибара", callback_data="Капибара")
        but_2 = telebot.types.InlineKeyboardButton(text="Фенек", callback_data="Фенек")
        #but_3 = telebot.types.InlineKeyboardButton(text="Дегу", callback_data="Дегу")
        but_3 = telebot.types.InlineKeyboardButton(text="Гиацинтовый ара", callback_data="Гиацинтовый ара")
        but_4 = telebot.types.InlineKeyboardButton(text="Аксолотль", callback_data="Аксолотль")
        #but_6 = telebot.types.InlineKeyboardButton(text="Валлаби", callback_data="Валлаби")
        but_5 = telebot.types.InlineKeyboardButton(text="Сахарная сумчатая летяга", callback_data="Сахарная сумчатая летяга")
        #but_8 = telebot.types.InlineKeyboardButton(text="Тарантул", callback_data="Тарантул")
        but_6 = telebot.types.InlineKeyboardButton(text="Беличья обезьяна", callback_data="Беличья обезьяна")
        but_7 = telebot.types.InlineKeyboardButton(text="Сервал", callback_data="Сервал")
        #but_11 = telebot.types.InlineKeyboardButton(text="Бородатый дракон", callback_data="Бородатый дракон")
        #but_12 = telebot.types.InlineKeyboardButton(text="Карликовый ослик", callback_data="Карликовый ослик")
        #but_13 = telebot.types.InlineKeyboardButton(text="Мадагаскарские шипящие тараканы", callback_data="Мадагаскарские шипящие тараканы")
        but_8 = telebot.types.InlineKeyboardButton(text="Пятнистая генетта", callback_data="Пятнистая генетта")
        but_9 = telebot.types.InlineKeyboardButton(text="Као мани", callback_data="Као мани")
        user_markup.add(but_1)
        user_markup.add(but_2)
        user_markup.add(but_3)
        user_markup.add(but_4)
        user_markup.add(but_5)
        user_markup.add(but_6)
        user_markup.add(but_7)
        user_markup.add(but_8)
        user_markup.add(but_9)
        #user_markup1 = telebot.types.ReplyKeyboardMarkup(True, False)
       # user_markup1.row('<<Назад')
        send = bot.send_message(message1.chat.id, "Список:", reply_markup=user_markup)
        #bot.send_message(message1.chat.id, '', reply_markup=user_markup1)
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, six)
        bot.register_next_step_handler(send, eight)
def eight(message1):
    if message1.text == u'\U0001F349Фрукты':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text="Дыня Yubari", callback_data="Дыня Yubari")
        but_2 = telebot.types.InlineKeyboardButton(text="Черный арбуз Densuke", callback_data="Черный арбуз Densuke")
        but_3 = telebot.types.InlineKeyboardButton(text="Виноград Ruby Roman", callback_data="Виноград Ruby Roman")
        but_4 = telebot.types.InlineKeyboardButton(text="Манго «яйцо солнца»", callback_data="Манго «яйцо солнца»")
        but_5 = telebot.types.InlineKeyboardButton(text="Квадратный арбуз", callback_data="Квадратный арбуз")
        but_6 = telebot.types.InlineKeyboardButton(text="Клубника из фруктового бутика", callback_data="Клубника из фруктового бутика")
        but_7 = telebot.types.InlineKeyboardButton(text="Яблоки Sekai Ichi", callback_data="Яблоки Sekai Ichi")
        but_8 = telebot.types.InlineKeyboardButton(text="Декопон", callback_data="Декопон")
        but_9 = telebot.types.InlineKeyboardButton(text="Груши в форме Будды", callback_data="Груши в форме Будды")
        but_10 = telebot.types.InlineKeyboardButton(text="Бананы Gokusen", callback_data="Бананы Gokusen")
        user_markup.add(but_1)
        user_markup.add(but_2)
        user_markup.add(but_3)
        user_markup.add(but_4)
        user_markup.add(but_5)
        user_markup.add(but_6)
        user_markup.add(but_7)
        user_markup.add(but_8)
        user_markup.add(but_9)
        user_markup.add(but_10)
        #user_markup1 = telebot.types.ReplyKeyboardMarkup(True, False)
       # user_markup1.row('<<Назад')
        send = bot.send_message(message1.chat.id, "Список:", reply_markup=user_markup)
        #bot.send_message(message1.chat.id, '', reply_markup=user_markup1)
        bot.register_next_step_handler(send, four)
        bot.register_next_step_handler(send, six)
        bot.register_next_step_handler(send, eight)

@bot.callback_query_handler(func=lambda c:True)
def three(c):
    if c.data == 'Капибара':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики", url="https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BF%D0%B8%D0%B1%D0%B0%D1%80%D0%B0")
        but_3 = telebot.types.InlineKeyboardButton(text="Капибара в неволе", callback_data="Капибара в неволе")
        user_markup.add(but_1, but_2)
        user_markup.add(but_3)
        bot.send_message(c.message.chat.id,
                         text = """<a href="https://pp.userapi.com/c844521/v844521765/169192/9nqfliHwEyE.jpg">&#8203;</a>Капибара

Цена: 120 000 - 260 000 руб.

Капибара — самый большой грызун в мире. Является родственником морских свинок и обитает в Южной Америке. 
Это чрезвычайно нежные животные, которые любят, чтобы их баловали. 
В зависимости от того, где ты живешь, тебе, возможно, потребуется разрешение на то, чтобы стать хозяином такого красавца. 
Ну и в любом случае необходимо позаботиться, чтобы у водосвинки (второе название капибар) было много места, где она могла бы бегать.

Длина тела взрослой особи может достигать 1,0-1,35 м. Высота в холке 0,5-0,6 м. Вес самцов колеблется от 34 до 63 кг. Самки чуть крупнее, могут весить до 65,5 кг. Продолжительность жизни в неволе до 12 лет.""",
                         parse_mode="HTML", reply_markup=user_markup)
        #bot.send_photo(274077151, 'https://pp.userapi.com/c844521/v844521765/169192/9nqfliHwEyE.jpg')
        #user_markup1 = telebot.types.ReplyKeyboardMarkup(True, False)
        #user_markup1.row('<<Назад')
        #bot.send_message(c.message.chat.id, "Если вам интересно, что это за животное, перейдите в Вики. Также вы можете его купить или вернуться назад.", reply_markup=user_markup1)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Фенек':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики", url="https://ru.wikipedia.org/wiki/%D0%A4%D0%B5%D0%BD%D0%B5%D0%BA")
        but_3 = telebot.types.InlineKeyboardButton(text="Фенек в неволе", callback_data="Фенек в неволе")
        user_markup.add(but_1, but_2)
        user_markup.add(but_3)
        bot.send_message(c.message.chat.id, text = """<a href="https://pp.userapi.com/c844216/v844216730/165143/MC3F_hu36FQ.jpg">&#8203;</a>Фенек
        
Цена: 100 000 - 250 000 руб.

Взрослый фенек достигает размеров чихуахуа. Вес фенека не превышает 1,5 кг. 
Это чрезвычайно дружелюбные создания с огромным количеством энергии (помимо время сна, конечно). 
Для их содержания нужно подготовить огромную клетку или отдельную комнату, засыпанную песком, чтобы животное могло рыть. 
Ну и лучше узнать у властей разрешают ли местные законы завести такого питомца...

Длина тела лисички 30-40 см, высота в холке – 18-22 см, длина хвоста – до 30 см, средний вес – 1,5 кг. Средняя продолжительность жизни в неволе 10 - 12 лет.""", parse_mode="HTML", reply_markup=user_markup)
        user_markup1 = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup1.row('<<Назад')
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Гиацинтовый ара':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики", url="https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%B0%D1%86%D0%B8%D0%BD%D1%82%D0%BE%D0%B2%D1%8B%D0%B9_%D0%B0%D1%80%D0%B0")
        but_3 = telebot.types.InlineKeyboardButton(text="Гиацинтовый ара в неволе", callback_data="Гиацинтовый ара в неволе")
        user_markup.add(but_1, but_2)
        user_markup.add(but_3)
        bot.send_message(c.message.chat.id, text = """<a href="https://pp.userapi.com/c844721/v844721730/16f044/OC7s9km9fX4.jpg">&#8203;</a>Гиацинтовый ара

Цена: 1 - 2,3 млн. руб.

Найти их довольно трудно, учитывая тот факт, что в дикой природе они вымирают из-за вырубки лесов в Бразилии и других странах Южной Америки. 
Это очень ласковые птицы, которые являются самыми крупными летающими попугаями, да к тому же самыми синими.

Длина 80-130 см, вес 1,5-2,5 кг. Продолжительность жизни до 65-90 лет.""", parse_mode="HTML", reply_markup=user_markup)
        #user_markup1 = telebot.types.ReplyKeyboardMarkup(True, False)
        #user_markup1.row('<<Назад')
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Аксолотль':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики", url="https://ru.wikipedia.org/wiki/%D0%90%D0%BA%D1%81%D0%BE%D0%BB%D0%BE%D1%82%D0%BB%D1%8C")
        but_3 = telebot.types.InlineKeyboardButton(text="Аксолотль в неволе", callback_data="Аксолотль в неволе")
        user_markup.add(but_1, but_2)
        user_markup.add(but_3)
        bot.send_message(c.message.chat.id, text = """<a href="https://pp.userapi.com/c844721/v844721730/16f057/GZNUZEEcYpA.jpg">&#8203;</a>Аксолотль

Цена: 1400 - 2500 руб.

Аксолотли известны еще как «ходячие рыбы», что странно, потому что они не рыбы, а амфибии. 
Они уникальны тем, что у них не вырастают легкие, как у других амфибий, и аксолотли всю жизнь проводят под водой.

Длина 20 – 25 см. Тип террариума: вода. Продолжительность жизни в неволе до 15 лет.""", parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Сахарная сумчатая летяга':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики", url="https://ru.wikipedia.org/wiki/%D0%A1%D0%B0%D1%85%D0%B0%D1%80%D0%BD%D0%B0%D1%8F_%D1%81%D1%83%D0%BC%D1%87%D0%B0%D1%82%D0%B0%D1%8F_%D0%BB%D0%B5%D1%82%D1%8F%D0%B3%D0%B0")
        but_3 = telebot.types.InlineKeyboardButton(text="Сахарная сумчатая летяга в неволе", callback_data="Сахарная сумчатая летяга в неволе")
        user_markup.add(but_1, but_2)
        user_markup.add(but_3)
        bot.send_message(c.message.chat.id, text = """<a href="https://pp.userapi.com/c844721/v844721730/16f098/Mrul_r2AU0w.jpg">&#8203;</a>Сахарная сумчатая летяга

Цена: 6 000 - 10 000 руб.

Эти крошечные животные получили свое название за свою любовь к сладким фруктам и за умение планировать, как это делают белки-летяги. 
Эти крохи сильно привязываются к своим хозяевам и другим обитателям дома, где они живут. 
Летяги абсолютно неагрессивные, хорошо реагируют на интонацию голоса и обучаются простым командам. 

Длина животного до 30 см, из которых более половины приходится на хвост. Масса взрослого самца 115—160 г, самки — 100—135 г. Продолжительность жизни в неволе до 15 лет. """, parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Беличья обезьяна':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики", url="https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%8B%D0%BA%D0%BD%D0%BE%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F_%D0%B1%D0%B5%D0%BB%D0%B8%D1%87%D1%8C%D1%8F_%D0%BE%D0%B1%D0%B5%D0%B7%D1%8C%D1%8F%D0%BD%D0%B0")
        but_3 = telebot.types.InlineKeyboardButton(text="Беличья обезьяна в неволе", callback_data="Беличья обезьяна в неволе")
        user_markup.add(but_1, but_2)
        user_markup.add(but_3)
        bot.send_message(c.message.chat.id, text = """<a href="https://pp.userapi.com/c844721/v844721730/16f0b2/jQHoyLPA038.jpg">&#8203;</a>Беличья обезьяна

Цена: 90 000 - 230 000 руб.

Милое небольшое животное, которое всё же требует определенных условий. 
Чрезвычайно дружелюбные животные. 
Ушки и мордочка таких животных покрыты белыми волосками, которые напоминают некий грим.

Длина тела достигает 25—36 см, хвост — до 40 см. Масса тела — до 1,1 кг. Продолжительность жизни в неволе 9 лет.""", parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Сервал':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики", url="https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%80%D0%B2%D0%B0%D0%BB")
        but_3 = telebot.types.InlineKeyboardButton(text="Сервал в неволе", callback_data="Сервал в неволе")
        user_markup.add(but_1, but_2)
        user_markup.add(but_3)
        bot.send_message(c.message.chat.id, text = """<a href="https://pp.userapi.com/c844721/v844721730/16f0bb/H4NRRcG2jQ8.jpg">&#8203;</a>Сервал

Цена: 300 000-600 000 руб.

Сервалы могут быть чрезвычайно преданными людям, но их нельзя воспринимать, как домашних кошек. 
Им нужно много пространства, для того чтобы они могли бегать, плавать, взбираться по скалам и прочее. 
Так, что если у тебя есть свой участок, то ты можешь завести себе такого котика.

Длина его тела 90—135 см, высота в плечах до 40—65 см; весит сервал 8—18 кг. Продолжительность жизни в неволе до 20 лет.""", parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Пятнистая генетта':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики", url="https://ru.wikipedia.org/wiki/%D0%9F%D1%8F%D1%82%D0%BD%D0%B8%D1%81%D1%82%D0%B0%D1%8F_%D0%B3%D0%B5%D0%BD%D0%B5%D1%82%D1%82%D0%B0")
        but_3 = telebot.types.InlineKeyboardButton(text="Пятнистая генетта в неволе", callback_data="Пятнистая генетта в неволе")
        user_markup.add(but_1, but_2)
        user_markup.add(but_3)
        bot.send_message(c.message.chat.id, text = """<a href="https://pp.userapi.com/c844721/v844721730/16f0df/T7KsPHPi2wI.jpg">&#8203;</a>Пятнистая генетта

Цена: 100 000 - 250 000 руб.

Приобретая генетту, вы должны пообещать, что никогда ее не бросите, — эти звери очень привязываются к дому. 
А если решитесь завести, то придется научиться считывать настроение вашего питомца: если она в добром расположении духа, то вы можете ее погладить, поиграть, а она подарит вам ласковое мурчание, а вот если она встала не с той лапы, то лучше ее не трогать — животное будет вести себя очень агрессивно.

Длина тела 42-58 см. Длина хвоста 39-53 см. Продолжительность жизни в неволе 30 лет.""", parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Као мани':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики", url="https://ru.wikipedia.org/wiki/Khao_Manee")
        but_3 = telebot.types.InlineKeyboardButton(text="Као мани в неволе", callback_data="Као мани в неволе")
        user_markup.add(but_1, but_2)
        user_markup.add(but_3)
        bot.send_message(c.message.chat.id, text = """<a href="https://pp.userapi.com/c844721/v844721730/16f0e8/U4xKeZpeexk.jpg">&#8203;</a>Као мани

Цена: 90 000 - 700 000  руб.

Предки Као мани были питомцами королевских особ. 
Речь о породе као-мани. Это очень умные, легко обучаемые, нежные кошки с белоснежной окраской и бездонными глазами. 
Несмотря на богатую родословную, они совершенно неприхотливы, готовы приспособиться к любым условиям.

Среднего телосложения (высота — 25-30 см), мускулистая (кошка: 2,5-3,6 кг, кот: 3,6-5 кг), с большими ушами, сердцевидной головой и овальными голубыми, янтарными, зелёными или разноцветными глазами.""", parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == "Купить":
        #bot.send_message(c.message.chat.id, u'\U0001F4B8\U0001F9FEКУПЛЕНО! Спасибо за покупку!')
        bot.answer_callback_query(c.id, text=u'\U0001F4B8\U0001F9FEКУПЛЕНО! Спасибо за покупку!', show_alert=True, url=None, cache_time=None)


    elif c.data == "Капибара в неволе":
        bot.send_message(c.message.chat.id, """Капибара очень легко одомашнивается и приручается. Она быстро и легко привыкает к человеку. Ее даже можно научить выполнять различные трюки. Капибару можно выгуливать на поводке. Это чрезвычайно чистоплотные животные.
Для содержания копибар необходим большой вольер для выгула, в котором обязательно бы был огромный куст и чистый водоем. Для зимовки делается теплый домик.
Если Вы хотите держать капибар в качестве домашнего любимца и не собираетесь заниматься их разведением, самцов лучше кастрировать, иначе по достижении половозрелости они могут начать воспринимать хозяина как объект ухаживаний.
В неволе капибару кормят больших размеров гранулами для грызунов, содержащими витамины и минералы, а также фруктами и овощами.
Вдобавок к обычному рациону капибаре необходимо давать нетоксичные предметы для изгрызания, например, ветки ивы или березы, чтобы стачивать постоянно растущие зубы. В неволе капибары живут до 12 лет. Капибаре нужен бассейн, в котором она будет проводить большую часть времени.
Часто капибары кладут голову на колени хозяину, выпрашивая ласку, а потом переворачиваются на спину и "просят" почесать им живот. Во время этого действа они часто засыпают.""")
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == "Фенек в неволе":
        bot.send_message(c.message.chat.id, """В первую очередь необходимо купить просторную клетку для этого зверька, где Вы будите запирать его ночью и в свое отсутствие. Так как по ночам у фенеков просыпаются их природные инстинкты, и они начинают носиться по квартире, рыть норы везде, где можно и нельзя, грызть всё, что попадётся, включая проводку, что может привести к нежелательным последствиям. В комнате, где живёт Фенек, ни в коем случае не должно быть сквозняка, а зимой комната должна хорошо прогреваться. В клетке нужно организовать лисичке спальное место с тёплой лежанкой. Несмотря на то, что эти животные могут долго обходиться без воды (в связи с их природным местом обитания), в свободном доступе должна быть миска со свежей водой. Приручать Фенека необходимо постепенно, так как они довольно пугливые животные. Нужно уделять им максимум внимания, ни в коем случае не кричать. Можно пробовать кормить питомца с рук.
В домашних условиях Фенека можно кормить сырым мясом, живым кормом (мелкие грызуны, ящерицы, саранча и др.), фруктами, овощами. Можно пробовать давать рыбу, яйца, кисломолочные продукты, зерновые. Впоследствии у лисёнка обязательно выработаются свои предпочтения в еде. Обязательно необходимо давать витамины, особенно витамин D3.""")
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == "Гиацинтовый ара в неволе":
        bot.send_message(c.message.chat.id, """Вольер для ар должен быть цельнометаллическим, сварным, с толстыми прутьями (интервал между прутьями 8-10 см, толщина провода 3-4 мм). На дверце лучше поставить навесные замочки: другие запоры они быстро приспосабливаются открывать. Минимальный размер вольера 10х3х2,5 м со смежным укрытием 3х2х2 м. В вольере должно быть установлено не менее двух насестов, размещенных на разных высотах. Один насест должен быть помещен около кормушки и воды, но не над ними. А также веревки, лестницы, бамбуковые кольца, домик для сна, три устойчивые кормушки (стальные или керамические).
Содержание не представляет большой сложности. Едят они: кокос, пшеницу, овес, орехи, почки, чечевицу, неочищенный рис, просо, ячмень. Арахис и бразильский орех, перед скармливанием очищают от кожуры и моют. Из фруктов и ягод: яблоки, апельсины, виноград, папайя, сливы. Из овощей: вареная кукуруза, стручковая фасоль (вареная), зеленый горох, огурцы, брокколи, капуста белокочанная и цветная, морковь, свекла, сладкий картофель (вареный). Из зелени: побеги деревьев, кустарников, проращенное зерно, листья одуванчиков, сельдерей, мангольд, шпинат. Можно давать вареные яйца, или яичницу-болтунью для пополнения белка.
Нельзя кормить: кофе, авокадо, шоколад, петрушка, алкоголь, сахар, молочные продукты (кроме йогурта), соль, жареные продукты.
Кроме основного корма, птице необходимо давать минеральные подкормки и витамины.
Необходимо как можно чаще давать свежие ветки плодовых деревьев, как мелкие, так и довольно толстые – до 7 см в диаметре, в коре которых содержатся необходимые птицам минеральные вещества и витамины.
Уход заключается в поддержании чистоты в вольере. Воду нужно менять ежедневно. У этих птиц, как и у всех крупных попугаев, сильно развит пищевой консерватизм, но, несмотря на их предпочтения, необходимо максимально разнообразить их рацион.
Любят купаться. В вольере время необходимо установить для этих целей водоем, или опрыскивать попугая из пульверизатора.""")
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == "Аксолотль в неволе":
        bot.send_message(c.message.chat.id, """Аксолотль хорошо размножается в неволе, за ним интересно наблюдать. Правда, в летние месяцы иногда возникают проблемы с поддержанием нужной температуры воды. Личинок-аксолотлей можно держать в аквариуме с водой (для двух взрослых 30-40 л) при комнатной температуре. На одну взрослую особь приходится около 7-10 л воды, высота слоя воды - 30 см.  В аквариуме должны быть микрокомпрессор и фильтр, не должно быть острых предметов. Освещать аквариум не требуется, но можно использовать неяркую флуорисцентную лампу.  В качестве грунта можно использовать песок или крупную гальку. Декорировать аквариум можно водными растениями и гладкими крупными камнями.
Вода ключевая или дехлорированная (отстаивают 24 часа и более), хорошо насыщенная кислородом, рН 7-8,2, dH - 6-16'. Раз в неделю воду частично заменяют (до 20%). Качество воды - одно из важных требований в содержании аксолотля. Перегрев для аксолотлей очень опасен, нормальная температура - 18-21 С днем и 16-18 С ночью. Аксолотли спокойно переносят понижение температуры до 12 С, но как и все амфибии плохо переносят перегрев.
Рацион должен быть разнообразным: трубочник (очищенный), мотыль, дождевые черви (свободные от химикатов и пестицидов), люмбрикулюс (Lumbriculus, очищенный), полоски постной телятины или говядины, личинки комаров, сырое говяжье сердце (полоски 0,5 см), водные и наземные улитки, личинки насекомых, "Reptomin" (корм для черепах), размягченный гранулированный корм для лососей или форели, личинки морских креветок (живые или замороженные, учтите, что последние сильно портят воду), можно давать кусочки мяса или сырой рыбы, нарезанные полосками. Взрослых кормят - 2-3 раза в неделю, молодых (растущих) - каждый день. Кормление в период размножения должно быть обильное.
Быстро привыкает к человеку, который его кормит, но иногда аксолотль может попытаться проглотить палец. Это безболезненно, поскольку его зубы не способны прокусить человеческую кожу.
Можно содержать вместе с саламандрами или их личинками. 
С рыбками держать не желательно, поскольку они пытаются грызть жабры аксолотля, да и он сам, время от времени, пытается схватить зазевавшуюся рыбку. 
Если аксолотля плохо кормить, он съест всех обитателей аквариума, даже своих соплеменников, откусывая иногда у них лапы или хвост. 
Голодный аксолотль иногда хватает за ногу или за хвост своего собрата и может даже откусить кусок, вращаясь, как крокодил, и не выпуская кусок из зубов.
Взрослых амфибий можно держать вместе, только они должны быть практически одного размера.
Если вода чистая и рана не заражена грибками, конечность полностью регенерирует (восстанавливается).
В аквариуме аксолотль чаще всего лежит на дне, иногда "виляя хвостом", может висеть в верхних слоях воды, перебирая лапами. Если аксолотля потревожить, он медленно уплывает.
При постоянном кормлении жирной пищей (трубочник, опарыши) развиваются склероз печени, поэтому нельзя перекармливать аксолотлей.
Среди аксолотлей, питающихся дафниями, реже бывают случаи каннибализма. Каннибализм - естественное поведение личинок амбистом.""")
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == "Сахарная сумчатая летяга в неволе":
        bot.send_message(c.message.chat.id, """Содержат этих зверьков в клетках или вольерах.
Несмотря на свой небольшой размер поссумы активные животные, и им необходим простор. Поэтому минимальный размер клетки на одну пару поссумов – 80*80*60см.
Надо всегда помнить, что поссумы в природе живут на деревьях. Поэтому желательно поставить ветви деревьев. Но не все деревья подходят для поссума, среди них могут быть и ядовитые.
 Для стен и потолка подойдет сетка с зазором между прутьями не более 1,5 см, чтобы малыши не выпали из клетки.
Дверь в вольер должна быть закрыта, потому что поссумы очень изобретательны, легко и быстро научатся ее открывать.
На пол клетки кладем опилки.
Миски размещаем на полочках. Открытую поилку лучше разместить в противоположной от еды стороне клетки, тогда вода дольше останется чистой.
Для поссумов нужны домики, которые крепятся в верхней части вольера. 
Самые любимые домики – мягкие, поэтому в жесткие домики необходимо положить. Домиков в клетке может быть несколько, но в период выращивания малышей необходим один домик.
В клетку вешают игрушки, лестницы, туннели, сделанные из 2 труб поливинилхлорида.  Твердые пластмассовые игрушки предпочтительнее. Необходимо колесо для бега в нем.
Игрушки должны периодически меняться на другие, чтобы поддерживать интерес зверьков.
 
Кормление поссумов при содержании в неволе должно быть разнообразным. В качестве основы для пищевого рациона рекомендуем детские безмолочные каши.
В кашу необходимо добавлять натуральный мед. Для взрослых пар мед в сотах. 
Кроме каш поссумы хорошо едят мякоть сладких спелых фруктов.
Для взрослых один раз в неделю рекомендовано белковое питание. Это детское гомогенизированное мясное пюре, вареное яйцо, нежирный творог, крохотный кусочек вареной курицы или индейки. Малышам можно что-то из описанного рациона предлагать ежедневно.
Насекомые – сверчки используются как лакомство или для приручени.

Разведение
У поссумов, живущих в неволе, сезона размножения как такового не существует: они размножаются круглый год. 
Если вы держите самца и самку, рано или поздно они начнут спариваться, даже если это родственники, во избежание генетических дефектов следует убрать детенышей и кастрировать самцов. 
 Если вы планируете получить потомство от сахарных поссумов, разумнее всего подождать до того момента, когда им исполнится как минимум год, в этом случае детеныши рождаются более здоровыми и сильными, а их выкармливание отнимает у матери меньше сил. 
 В период размножения сахарные поссумы могут вести себя довольно грубо; в этот период у них часто появляются царапины и раны от укусов. Осматривайте и обрабатывайте раны.
В период вынашивания малышей очень важно обогащать рацион самки питательными веществами. 
Рекомендуется  повысить содержание белков в рационе поссумов до 50%; также важно, чтобы белок был животного происхождения, но при этом содержание жиров в питании поссумов оставалось низким. 
Куриное мясо, мучные черви, кузнечики и другие источники белка того же уровня - это именно то, что вам нужно. Кормящие самки должны получать также некоторое количество жиров, так как это необходимо для лактации.
 Также крайне важно снизить уровень стресса для самки. Не советуют показывать вашим друзьям, как растут детеныши в сумке; также не рекомендуется постоянно проверять гнездо поссумов. В ходе вынашивания и выкармливания детенышей вашим поссумам необходимо побыть одним.
 Поссумы в период размножения - это, зачастую, не те забавные зверушки, что и поссумы, у которых нет детишек. 
 При наличии малышей вы можете заметить изменения в поведении самки и/или самца. Оба родителя могут начать защищать детенышей.
В одном помете у сахарных поссумов 1-2 детеныша, 2-3 раза в год. 
Период внутриутробного развития у поссумов составляет всего шестнадцать дней; После детеныш забирается в материнскую сумку. 
Здесь детеныш остается в течение десяти недель: за этот срок его развитие практически полностью завершается. Выбравшийся из сумки детеныш не полностью покрыт мехом.
Рекомендуется  держать детенышей с родителями, по крайней мере, до восьми недель после выхода детеныша из сумки матери.""")
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == "Беличья обезьяна в неволе":
        bot.send_message(c.message.chat.id, """Это животное всеми любимо за свой добрый нрав; его охотно держат в домах.
Саймири принадлежит к самым трусливым животным, но во всех действиях своих он выказывает себя настоящей обезьяной. 
Нравом он напоминает ребенка, на которого похож и лицом: «...то же выражение невинности, та же лукавая улыбка, тот же быстрый переход от радости к печали». 
Его лицо служит верным отражением внешних впечатлений и внутренних ощущений. 
В минуты испуга в его больших глазах показываются слезы; горе тоже выражается слезами. 
В неволе саймири жалуется и визжит по самому незначительному поводу. 
Чувствительность и раздражительность его одинаково велики, но он вовсе не своеволен, напротив, так добродушен, что невозможно на него сердиться. 
Саймири внимательно следит за всеми действиями своего господина. 
Когда ему что-то говорят, он пристально всматривается в лицо говорящего, следит глазами за каждым движением его губ, старается к нему приблизиться, садится на его плечо, дотрагивается до его зубов и языка, как будто старается угадать смысл непонятных ему звуков. Пищу саймири берет руками, а иногда и ртом.
Из неприятных для людей привычек у саймири можно выделить такие как: натирать мочой все тело и особенно кончик хвоста, который поэтому всегда мокрый. Также неопрятны и в питании: жмут фрукты, раздирают и давят ногами, натираются соком. Не любят одиночества, чрезвычайно болтливы.
Минимальным размером вольера для содержания одной саймири можно назвать 100х100х50 см. 
Естественно, чем вольер больше, тем комфортнее будет себя чувствовать обезьяна. 
В вольере должно быть достаточно ветвей, по которым саймири может бегать. 
Очень важным условием правильного содержания является температура - не ниже 24 градуса. 
Обитая в тропическом климате, где температуры круглогодично держатся в пределах 26-30, обезьянки легко переохлаждаются и простужаются, поэтому к обогреву комнаты, где живет саймири, следует отнестись внимательно. 
Очень хорошо установить инфракрасную зеркальную лампу, направленную на одну из ветвей - саймири будут с удовольствием греться. Однако, лампа должна находиться вне вольера, так, чтобы быть вне досягаемости длинных и любопытных рук обезьянки. 
При своей сообразительности и любопытстве обезьяна способна причинить себе значительный вред, получив доступ к электроприборам.
Как и большинство обезьян, саймири можно назвать неприхотливыми в еде, что однако не означает неразборчивость или возможность питаться одними сухариками.  
Это должны быть всевозможные овощи и фрукты, соки, нежирный творог и простокваша, йогурт, кусочки нежирного вареного мяса, яйцо (иногда можно дать и сырое перепелиное - будет встречено с восторгом. Листик салата или одуванчика тоже не помешает. Немного вареной рыбы или креветка. А если есть возможность время от времени давать крупного таракана, фобаса или саранчу - будет совсем прекрасно. Рацион должен быть максимально разнообразным, но не выходить за пределы разумного - никаких острых, соленых или консервированных блюд! Никаких пицц и яичниц, конфет и чипсов! Обезьянка все это съест, но - это вредно!""")
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == "Сервал в неволе":
        bot.send_message(c.message.chat.id, """Сервалов достаточно легко содержать в домашних условиях. Для приобретенного в питомнике животного не нужна клетка, и нетрудно прокормить. Основу их стола составляет сырое мясо с костями – говядина или птица – от 0,5 до 1,3 килограмма в день. Обязательны также витамины с кальциевыми добавками. Эта кошка хорошо приучается к туалету с наполнителем и вообще весьма чистоплотна. Единственная привычка, которую сервал не в силах побороть, это пометка территории. Делает он это постоянно, а запах его секрета довольно сильный, поэтому этих кошек рекомендуется стерилизовать или кастрировать.
Есть несколько главных правил воспитания маленького сервала, соблюдая которые, можно вырастить практически идеального питомца. Играя с котенком, не следует «задирать» его рукой или ногой, иначе он всегда будет воспринимать руки-ноги людей, как игрушки, и тогда царапин не избежать. Лучше использовать настоящие игрушки для кошек и собак. Если котенок, заигравшись, все же начал царапаться и кусаться, с ним нужно просто перестать играть, вообще оставить его одного. Несколько таких уроков, и сервал сообразит, что царапаться и кусаться не следует, иначе потеряешь товарища по играм. Сервалов вообще нельзя бить или кричать на них. Строгое «нельзя», подкрепленное выстрелом из водяного пистолета, быстро выработает у кошки рефлекс. Внушение или прекращение общения действуют на умниц-сервалов очень эффективно, они понимают, что делают что-то не так, и вскоре перестают поступать неправильно.""")
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == "Пятнистая генетта в неволе":
        bot.send_message(c.message.chat.id, """Генетты легко приручаются. В Африке их иногда содержат дома для истребления крыс и мышей. В Европе и Америке как домашнего любимца. Непродолжительное время в эпоху раннего Средневековья в Европе генетты были домашними животными, однако в этом качестве их быстро вытеснили кошки.
Иногда в некоторой литературе можно встретить утверждение что генетты плохо пахнут. Возможно это имеются ввиду дикие генетты. В домашних условиях, они абсолютно не пахнут.
Некоторые заводчики генетт, во избежание  подранных обоев и мебели удаляют им когти, подобно тому, как это делают кошкам. Так же генетт иногда кастрируют и стерилизуют.
Генетты очень чистоплотны, и гадят в строго определенном месте. Рекомендую поставить в это место кошачий туалет и они будут гадить только туда.
Генетт можно кормить обычной кошачьей едой, но желательно включать в рацион натуральную пищу: мясо птицы, фрукты.""")
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == "Као мани в неволе":
        bot.send_message(c.message.chat.id, """Уход за као мани подразумевает стандартные процедуры — еженедельное вычесывание, чистка ушей, глаз, зубов и состригание когтей. В питании особых рекомендаций нет. Большинство заводчиков кормят своих кошек полноценными сухими или влажными кормами.""")
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)

    elif c.data == 'Дыня Yubari':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики", url="https://en.wikipedia.org/wiki/Yubari_King")
        user_markup.add(but_1, but_2)
        bot.send_message(c.message.chat.id, text = """<a href="https://pp.userapi.com/c849132/v849132292/f213f/t0ea0AKt6cU.jpg">&#8203;</a>Дыня Yubari

Дыню «юбари» выращивают в теплицах на японском острове Хоккайдо, прикрывая от солнца специальными «шляпками». Это очень сладкая, идеально круглая дыня с кожурой, рисунок которой напоминает трещинки на древнем японском фарфоре.

В среднем «юбари» стоит около $ 300, но две самые дорогие из них были проданы с аукциона за $ 27 000.""", parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Черный арбуз Densuke':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики", url="https://ru.wikipedia.org/wiki/%D0%90%D1%80%D0%B1%D1%83%D0%B7#%D0%94%D0%B5%D0%BD%D1%81%D1%83%D0%BA%D0%B5")
        user_markup.add(but_1, but_2)
        bot.send_message(c.message.chat.id, text = """<a href="https://pp.userapi.com/c849132/v849132292/f215b/O-uVT8JiqhE.jpg">&#8203;</a>Черный арбуз Densuke

Этот арбуз, обладающий «особым типом сладости», растет только на японском острове Хоккайдо. Кожура у него темно-зеленая, почти черная, без полос и пятен, поэтому его называют черным арбузом. Densuke продается в специальных черных коробках, подчеркивающих его цвет. Японцы считают такие арбузы ценным подарком.

В среднем арбуз Densuke стоит $ 250, но самый большой из них был продан с аукциона за $ 6 100.""", parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Виноград Ruby Roman':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики",
                                                   url="https://en.wikipedia.org/wiki/Ruby_Roman")
        user_markup.add(but_1, but_2)
        bot.send_message(c.message.chat.id, text="""<a href="https://pp.userapi.com/c849132/v849132292/f2163/TZDwnMt0o5A.jpg">&#8203;</a>Виноград Ruby Roman

Этот красный виноград, выведенный японскими селекционерами, — самый дорогой в мире. Каждая из ягод — размером с мячик для пинг-понга, а вкус у них необыкновенно сладкий — в них содержится 18 % сахара.

Виноград стоит около $ 65 за ветку, но в 2016 году гроздь весом 700 граммов была продана с аукциона за $ 10 900.""",
                         parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Манго «яйцо солнца»':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики",
                                                   url="https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D0%BD%D0%B3%D0%BE_(%D1%84%D1%80%D1%83%D0%BA%D1%82)")
        user_markup.add(but_1, but_2)
        bot.send_message(c.message.chat.id, text="""<a href="https://pp.userapi.com/c849132/v849132292/f216b/GeTsTWBoMQg.jpg">&#8203;</a>Манго «яйцо солнца»

Манго этого сорта весят не менее 350 граммов и обладают повышенной сладостью. Пара таких манго была продана с аукциона в Японии за $ 3 000.""",
                         parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Квадратный арбуз':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики",
                                                   url="https://en.wikipedia.org/wiki/Square_watermelon")
        user_markup.add(but_1, but_2)
        bot.send_message(c.message.chat.id, text="""<a href="https://pp.userapi.com/c849132/v849132292/f2173/peySp3oRISA.jpg">&#8203;</a>Квадратный арбуз

Эти арбузы создали фермеры японского острова Сикоку. Для придания формы их помещают в специальные контейнеры-кубы. 
Ухаживать за такими арбузами очень сложно, и, достигнув желаемой формы, они не успевают созреть. Поэтому квадратные арбузы покупают в основном в декоративных целях — например, для украшения витрин. Стоят они от $ 200 до $ 800.""",
                         parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Клубника из фруктового бутика':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        user_markup.add(but_1)
        bot.send_message(c.message.chat.id, text="""<a href="https://pp.userapi.com/c849132/v849132292/f218b/WRCi38Xj7fA.jpg">&#8203;</a>Клубника из фруктового бутика

Кажется, что это обычная клубника. Но эти ягоды отобраны из сотен других по принципу идеальной формы. Продаются они в роскошном фруктовом салоне Sembikiya в Токио. Стоят $ 69 за упаковку, в которой 12 штук.""",
                         parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Яблоки Sekai Ichi':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики",
                                                   url="https://en.wikipedia.org/wiki/Sekai_Ichi")
        user_markup.add(but_1, but_2)
        bot.send_message(c.message.chat.id, text="""<a href="https://pp.userapi.com/c849132/v849132292/f217b/Z5Gya9tQQXs.jpg">&#8203;</a>Яблоки Sekai Ichi

Эти яблоки — гордость японских селекционеров. Они могут достигать веса в 2 килограмма! Сады, в которых они выращиваются, опыляют вручную с помощью специальных палочек. Японцы считают эти яблоки большим деликатесом и едят их в основном по праздникам. Каждое из яблок стоит $ 21.""",
                         parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Декопон':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        but_2 = telebot.types.InlineKeyboardButton(text="Вики",
                                                   url="https://en.wikipedia.org/wiki/Dekopon")
        user_markup.add(but_1, but_2)
        bot.send_message(c.message.chat.id, text="""<a href="https://pp.userapi.com/c849132/v849132292/f2183/KWxIW7t9KVs.jpg">&#8203;</a>Декопон

Декопон (Dekopon, или Sumo Fruit) — гибрид мандарина и апельсина, который тоже выведен в Японии. Утверждают, что это самый вкусный цитрус в мире — сладкий, с легкой кислинкой, с тончайшими перегородками между дольками, он больше и сочнее других цитрусовых. Один декопон стоит $ 13.""",
                         parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Груши в форме Будды':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        user_markup.add(but_1)
        bot.send_message(c.message.chat.id, text = """<a href="https://pp.userapi.com/c849132/v849132292/f2193/yoOgWEMZQpQ.jpg">&#8203;</a>Груши в форме Будды

Груши в виде маленьких Будд и младенцев придумали выращивать китайские фермеры. Они закрепляют на плодах прозрачные пластиковые формы, и при созревании груши обретают вид маленькой скульптуры. Легенда, оправдывающая высокую цену каждой груши — $ 9, гласит, что эти плоды дарят бессмертие.""", parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)
    elif c.data == 'Бананы Gokusen':
        user_markup = telebot.types.InlineKeyboardMarkup()
        but_1 = telebot.types.InlineKeyboardButton(text=u'\U0001F4B3Купить', callback_data="Купить")
        user_markup.add(but_1)
        bot.send_message(c.message.chat.id, text = """<a href="https://pp.userapi.com/c849132/v849132292/f219b/gKbcM3QXfjM.jpg">&#8203;</a>Бананы Gokusen

Каждый такой банан упакован в отдельную коробку и имеет серийный номер. Бананы Gokusen растут в экологически чистом районе Филиппин на высоте 500 метров над уровнем моря. Они выведены из 100 сортов и на треть слаще, ароматнее и нежнее обычных бананов. Один такой весит ровно 200 граммов и стоит $ 6. Продаются бананы в строго ограниченном количестве.""", parse_mode="HTML", reply_markup=user_markup)
        bot.answer_callback_query(c.id, text=None, show_alert=False, url=None, cache_time=None)



bot.polling(none_stop=True, interval=0)