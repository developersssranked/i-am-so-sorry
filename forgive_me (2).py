import telebot
from telebot import types

bot = telebot.TeleBot("5499870186:AAE2aT3J0pQ8em5xcYnaZRHWOgTKKrDLCq0")

x = ["Я искренне сожалею о своем поступке", "Я не в силах исправить ошибку изменить прошлое", "Мне невыносимо думать, что я причинил тебе боль ,заставил переживать",
     "Очень надеюсь, что ты сменишь гнев на милость, простишь меня и позволишь доказать, как ты важна для меня"]
# random_index = random.randrange(len(x))


@bot.message_handler(commands=["start"])
def help(hep):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mrk.add(types.KeyboardButton("нажми"))
    mes = bot.send_message(
        hep.chat.id, "милион извенений для тебя", reply_markup=mrk)
    bot.register_next_step_handler(mes, sor1)


@bot.message_handler(content_types=["text"])
def sor1(mes):
    if mes.text == "нажми":

        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mrk.add(types.KeyboardButton("нажми"))
        mess = bot.send_message(
            mes.chat.id, "Я искренне сожалею о своем поступке", reply_markup=mrk)
        bot.register_next_step_handler(mess, sor2)


def sor2(mes):
    if mes.text == "нажми":

        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mrk.add(types.KeyboardButton("нажми"))
        mess = bot.send_message(
            mes.chat.id,   "Я не в силах исправить ошибку изменить прошлое", reply_markup=mrk)
        bot.register_next_step_handler(mess, sor3)


def sor3(mes):
    if mes.text == "нажми":

        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mrk.add(types.KeyboardButton("нажми"))
        mess = bot.send_message(
            mes.chat.id,   "Мне невыносимо думать, что я причинил тебе боль ,заставил переживать", reply_markup=mrk)
        bot.register_next_step_handler(mess, sor4)


def sor4(mes):
    if mes.text == "нажми":

        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mrk.add(types.KeyboardButton("нажми"))
        mess = bot.send_message(
            mes.chat.id,   "Очень надеюсь, что ты сменишь гнев на милость, простишь меня и позволишь доказать, как ты важна для меня", reply_markup=mrk)
        bot.register_next_step_handler(mess, meet)


def meet(mes):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("нажми")
    markup.add(btn1)
    bot.send_message(mes.chat.id, "Немножко хотелось бы рассказать об истории нашего знакомства. Может быть когда тебе будет грустно или скучно ты будешь заходить в этого бота и вспоминать обо мне. ")
    bot.send_message(mes.chat.id, "Одним прекрасным днем вы с Аделей пошли проверять работы у нашего любимого Александра Владимирировича. Потом ты решила подойти ко мне и <<включить режим тигрицы>>. Я очень удивился, и честно сначала вообще не хотел говорить с тобой, но ты как то предрасполагаешь к общению. Я дико смущался. Потом ты попросила провести тебя до дома и я не понимаю почему, но согласился. Погуляв с тобой около 3-х часов я устал, но это была приятная усталость, мне действительно понравилось с тобой общаться.")
    mess = bot.send_message(
        mes.chat.id, "Напиши то, как ты видишь наше знакомство")
    bot.register_next_step_handler(mess, compl)


def compl(mes):
    bot.send_message(1135014446, mes.text)  # добавь сюда переход
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mrk.add(types.KeyboardButton("нажми"))
    mess = bot.send_message(
        mes.chat.id, "Фотографии не передают всю твою красоту", reply_markup=mrk)
    bot.register_next_step_handler(mess, compl1)


def compl1(mes):
    if mes.text == "нажми":  # добавь сюда переход
        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mrk.add(types.KeyboardButton("нажми"))
        mess = bot.send_message(
            mes.chat.id, "Ты неизведанный океан, неоткрытый материк, уникальная планета, яркая звезда!", reply_markup=mrk)
        bot.register_next_step_handler(mess, compl2)


def compl2(mes):
    if mes.text == "нажми":  # добавь сюда переход
        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mrk.add(types.KeyboardButton("нажми"))
        mess = bot.send_message(
            mes.chat.id, "Как хорошо, что мы встретились! Ты подарила мне новые цели и немного изменила мой взгляд на жизнь!", reply_markup=mrk)
        bot.register_next_step_handler(mess, compl2)


def compl2(mes):
    if mes.text == "нажми":  # добавь сюда переход
        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mrk.add(types.KeyboardButton("нажми"))
        mess = bot.send_message(
            mes.chat.id, "Ты другая, это притягивает меня к тебе", reply_markup=mrk)
        bot.register_next_step_handler(mess, ques)


def ques(mes):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    btn3 = types.KeyboardButton("3")
    btn4 = types.KeyboardButton("4")
    btn5 = types.KeyboardButton("5")
    btn6 = types.KeyboardButton("6")
    btn7 = types.KeyboardButton("7")
    btn8 = types.KeyboardButton("8")
    btn9 = types.KeyboardButton("9")
    btn10 = types.KeyboardButton("10")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    mess = bot.send_message(
        mes.chat.id, "Я не знаю, повлиялил ли на тебя слова, сказанные мною вчера, но я бы хотел спросить какого мнения ты обо мне сейчас? выбери цифру от 1 до 10", reply_markup=markup)
    bot.register_next_step_handler(mess, returning)


def returning(mes):
    bot.send_message(1135014446, mes.text)


bot.polling(none_stop=True)
