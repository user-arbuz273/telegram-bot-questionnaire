
import time
import telebot
from telebot import types
from functools import partial

bot = telebot.TeleBot('7068193488:AAH3FE-pFr1Vh0KlvPM3zMnrlGoBXqnRhKw')

class User:
    def __init__(self):
        self.name = ''
        self.answers = []

users = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,  "Здравствуйте! Я очень рада, что Вы осознанно подходите к своему здоровью. Пожалуйста, заполните анкету максимально честно и подробно, чтобы я могла персонализировано провести первую консультацию и знать какого направления придерживаться в выборе стратегии.")
    #time.sleep(1)
    bot.send_message(message.chat.id, 'Пусть наше знакомство станет началом позитивных изменений в Вашей жизни, с удовольствием поддержу Вас в этом.')
    #time.sleep(1)
    send_mess = bot.send_message(message.chat.id, "Представьтесь пожалуйста (ФИО)")
    bot.register_next_step_handler(send_mess,lastnamefirstname)

@bot.message_handler(commands=['text'])

def lastnamefirstname(message):

    user_id = message.from_user.id
    users[user_id] = User()

    users[user_id].name = message.text
    choice(message)
def choice(message):
    user_id = message.from_user.id

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    start_btn = types.KeyboardButton('Начать')
    later_btn = types.KeyboardButton('Позже')
    markup.add(start_btn, later_btn)

    send_mess = bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=markup)
    bot.register_next_step_handler(send_mess,lambda message: beginning(message,user_id))

def beginning(message,user_id):
    if message.text.lower() == "позже":
        bot.send_message(message.chat.id, "Обязательно зайдите позже, чтобы продолжить.",reply_markup=types.ReplyKeyboardRemove())
        #time.sleep(1)
        bot.register_next_step_handler(bot.send_message(message.chat.id,"Напиши 'Продолжить', когда будешь готов."), handle_later)
    elif message.text.lower() == "начать":
        bot.send_message(message.chat.id, "Ура, начнем !",reply_markup=types.ReplyKeyboardRemove())
        #time.sleep(1)
        bot.send_message(message.chat.id, 'Первый вопрос !\nВведите электронную почту')
        bot.register_next_step_handler(message,question1,user_id)

#@bot.message_handler(commands=['question'])
def question1(message,user_id):

    user = users[user_id]
    user.answers.append(message.text)

    bot.send_message(message.chat.id, 'Введите дату рождения')
    bot.register_next_step_handler(message,question2,user_id)

def question2(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Ваша цель работы со мной? В чем заключается основная проблема, с которой Вы обратились? '), question3, user_id)

def question3(message,user_id):

    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Какого результата Вы хотите достичь? '), question4,user_id)

def question4(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'На какую помощь от меня Вы рассчитываете?'), question5,user_id)

def question5(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Что Вы уже пробовали, чтобы добиться результата в отношении Вашего вопроса? Что Вам помогло, а что не дало никаких результатов?'), question6,user_id)

def question6(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Есть ли у Вас какие-либо зависимости (включая кофе, сладкое, сигареты и т.д.)?'), question7,user_id)

def question7(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Ваш текущий вес (в кг) и рост (в см)'), question8,user_id)

def question8(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)

    estimation1 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('1')
    btn2 = types.KeyboardButton('2')
    btn3 = types.KeyboardButton('3')
    btn4 = types.KeyboardButton('4')
    btn5 = types.KeyboardButton('5')
    btn6 = types.KeyboardButton('6')
    btn7 = types.KeyboardButton('7')
    btn8 = types.KeyboardButton('8')
    btn9 = types.KeyboardButton('9')
    btn10 = types.KeyboardButton('10')
    estimation1.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)

    send_mess = bot.send_message(message.chat.id, 'Оцените свой опыт в вопросах здорового питания по шкале от 1 до 10 (нет опыта – 1, следую принципам здорового питания регулярно-10)?', reply_markup=estimation1)

    bot.register_next_step_handler(send_mess, question9,user_id)

def question9(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Есть ли у Вас какие-либо диагностированные болезни, травмы? (опишите)',reply_markup=types.ReplyKeyboardRemove() ), question10,user_id)

    #bot.send_message(message.chat.id, f'{answers}')

def question10(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Имеется ли аллергия или непереносимость? Как они выражаются?'), question11,user_id)

def question11(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Принимаете ли Вы какие-то лекарства? (перечислите)'), question12,user_id)

def question12(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Употребляете ли Вы витамины/нутрицевтики/бады? (напишите какие именно)'), question13,user_id)
def question13(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Сколько раз в день Вы едите?'), question14,user_id)

def question14(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Какой интервал времени между приемами пищи?'), question15,user_id)
def question15(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'За сколько часов до сна последний прием пищи?'), question16,user_id)

def question16(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Если взять всю еду в день как 100%, сколько из неё % еды домашнего приготовления?'), question17,user_id)

def question17(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Занимаетесь ли Вы спортом или имеете другие физические нагрузки (какие, как часто)?'), question18,user_id)

def question18(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Сколько часов Вы спите? Какое у вас качество сна?'), question19,user_id)

def question19(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Как Вы расслабляетесь? Пользуетесь ли какими-то практиками?'), question21,user_id)


def question21(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)

    estimation2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('1')
    btn2 = types.KeyboardButton('2')
    btn3 = types.KeyboardButton('3')
    btn4 = types.KeyboardButton('4')
    btn5 = types.KeyboardButton('5')
    btn6 = types.KeyboardButton('6')
    btn7 = types.KeyboardButton('7')
    btn8 = types.KeyboardButton('8')
    btn9 = types.KeyboardButton('9')
    btn10 = types.KeyboardButton('10')
    estimation2.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)

    send_mess = bot.send_message(message.chat.id,'По шкале от 1 до 10, где 1 самое низкое, а 10 самое высокое, оцените пожалуйста Ваше умение мотивировать самого себя в плане питания, соблюдения режима дня и регулярности тренировочного процесса?',reply_markup=estimation2)

    bot.register_next_step_handler(send_mess, question22,user_id)

def question22(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)

    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Как Вы считаете, что лучше мотивирует людей - негативная или позитивная мотивация?',reply_markup=types.ReplyKeyboardRemove()), question23,user_id)

def question23(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)

    user.answers.append("\nCHECK-UP")

    yesno = types.ReplyKeyboardMarkup( resize_keyboard=True)
    yes_btn = types.KeyboardButton('Да')
    no_btn = types.KeyboardButton('Нет')

    yesno.add(yes_btn, no_btn)

    bot.send_message(message.chat.id,"А теперь проведём чек-ап некоторых сигнальных симптомов.")
    bot.send_message(message.chat.id, "Ответьте, пожалуйста, беспокоят ли Вас...")
    bot.register_next_step_handler(bot.send_message(message.chat.id, '\nБоли или дискомфорт в области желудка во время или после еды ', reply_markup=yesno), question24,user_id)

def question24(message,user_id):
    text = 'Боли или дискомфорт в области желудка во время или после еды : '
    if message.text == "Да":
        user = users[user_id]
        user.answers.append(text + message.text)

    elif message.text == "Нет ":
        user = users[user_id]
        user.answers.append(text + message.text)
    #else:
       # save(message,user_id)
    send = 'Изжога : '
    bot.register_next_step_handler( bot.send_message(message.chat.id, 'Изжога'), question25, user_id,send)


def question25(message,user_id,send):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send + message.text)

    send = 'Отрыжка : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Отрыжка'), question26, user_id,send)
def question26(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send = 'Тошнота : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Тошнота'), question27, user_id,send)

def question27(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send = 'Вздутие : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Вздутие'), question28, user_id,send)
def question28(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send = 'Запоры (опоржнение кишечника реже 1 раза в сутки) : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Запоры (опоржнение кишечника реже 1 раза в сутки)'), question30, user_id,send)

def question30(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Диарея : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Диарея'), question31, user_id,send_mess)
def question31(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Горечь во рту : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Горечь во рту'), question32, user_id,send_mess)

def question32(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Ощущение тяжести после еды : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Ощущение тяжести после еды'), question33, user_id,send_mess)

def question33(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Непереносимость жирной пищи : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Непереносимость жирной пищи'), question34, user_id,send_mess)

def question34(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Непереносимость мясной пищи : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Непереносимость мясной пищи'), question35, user_id,send_mess)

def question35(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess =  'Налет на языке : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Налет на языке'), question36, user_id,send_mess)

def question36(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Неприятный запах изо рта или от тела : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Неприятный запах изо рта или от тела'), question37, user_id,send_mess)

def question37(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Боль в суставах или мышцах без причин : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Боль в суставах или мышцах без причин'), question38, user_id,send_mess)

def question38(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess =  'Слабость или утомление : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Слабость или утомление'), question39, user_id,send_mess)

def question39(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Вялость и апатия : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Вялость и апатия'), question40, user_id,send_mess)

def question40(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Ограничение двигательной активности : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Ограничение двигательной активности'), question41, user_id,send_mess)

def question41(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess =  'Повышенное потоотделение : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Повышенное потоотделение'), question42, user_id,send_mess)

def question42(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess =  'Отеки : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Отеки'), question43, user_id,send_mess)

def question43(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Тревожность, панические атаки, депрессия : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Тревожность, панические атаки, депрессия'), question44, user_id,send_mess)

def question44(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess =  'Выпадение волос : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Выпадение волос'), question45, user_id,send_mess)

def question45(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Воспалительные элементы (высыпания) на лице и/или теле : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Воспалительные элементы (высыпания) на лице и/или теле'), question46, user_id,send_mess)

def question46(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Капилярные, сосудистые сеточки на коже, "красные щечки" : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Капилярные, сосудистые сеточки на коже, "красные щечки"'), question47, user_id,send_mess)

def question47(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess =  'Пигментные пятна : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Пигментные пятна'), question48, user_id,send_mess)

def question48(message,user_id,send_mess):

    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Папилломы или красные точки на теле : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Папилломы или красные точки на теле'), question49, user_id, send_mess)

def question49(message,user_id,send_mess):
    user = users[user_id]
    if message.text == "Да":

        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":

        user.answers.append(send_mess + message.text)



    sex = types.ReplyKeyboardMarkup(resize_keyboard=True)
    wom_btn = types.KeyboardButton('Женщина')
    men_btn = types.KeyboardButton('Мужчина')

    sex.add(wom_btn, men_btn)

    #send_mess = bot.send_message(message.chat.id, 'Сейчас начнутся вопросы для женщин, поэтому мужчины могут пропустить.\nВыбирите пол', reply_markup= sex)
    bot.send_message(message.chat.id, 'Сейчас будет несколько вопросов , касающихся женского здоровья')
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Если Вы мужчина, нажмите одноименную кнопку и пропустите данные вопросы ', reply_markup= sex), women, user_id)



def women(message,user_id):
    user = users[user_id]
    if message.text == "Мужчина":
        end(message,user_id)
    if message.text == "Женщина":
        user.answers.append("Женщины")
        yesno = types.ReplyKeyboardMarkup(resize_keyboard=True)
        yes_btn = types.KeyboardButton('Да')
        no_btn = types.KeyboardButton('Нет')

        yesno.add(yes_btn, no_btn)
        bot.send_message(message.chat.id, 'Что из нижеперечисленного у Вас наблюдается?')
        send_mess = 'Болезненные месячные : '

        bot.register_next_step_handler(bot.send_message(message.chat.id, 'Болезненные месячные',reply_markup= yesno), wom_quest1, user_id,send_mess)


def wom_quest1(message,user_id,send_mess):
    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess =  'Нарушения цикла : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Нарушения цикла'), wom_quest2, user_id,send_mess)

def wom_quest2(message,user_id,send_mess):
    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'ПМС : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'ПМС'), wom_quest3, user_id,send_mess)

def wom_quest3(message,user_id,send_mess):
    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Вагинальные инфекции : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Вагинальные инфекции'), wom_quest4, user_id,send_mess)

def wom_quest4(message,user_id,send_mess):
    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess =  'Грибки, дрожжи : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Грибки, дрожжи'), wom_quest5, user_id,send_mess)

def wom_quest5(message,user_id,send_mess):
    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess =  'Проблемы с зачатием : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Проблемы с зачатием'), wom_quest6, user_id,send_mess)

def wom_quest6(message,user_id,send_mess):
    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    if message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    send_mess = 'Проблемы с вынашиванием : '
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Проблемы с вынашиванием'), end1, user_id,send_mess)

def end(message,user_id):
    user = users[user_id]
    user.answers.append(message.text)
    bot.send_message(message.chat.id,'Благодарю Вас за честные ответы и уделенное время!',reply_markup=types.ReplyKeyboardRemove())
    finish(message,user_id)

def end1(message,user_id,send_mess):
    if message.text == "Да":
        user = users[user_id]
        user.answers.append(send_mess + message.text)

    elif message.text == "Нет ":
        user = users[user_id]
        user.answers.append(send_mess + message.text)


    bot.send_message(message.chat.id,'Благодарю Вас за честные ответы и уделенное время!',reply_markup=types.ReplyKeyboardRemove())
    finish(message,user_id)
def finish(message, user_id):
    user = users[user_id]
    user_name = message.from_user.username
    chat_id = '-4139128842'
    result = '\n'.join([x.strip() for x in user.answers if x.strip()])
    bot.send_message(chat_id, f'{user.name} @{user_name}')
    bot.send_message(chat_id, result)

def handle_later(message):

    while message.text.lower() != "продолжить":
        time.sleep(1)
        bot.send_message(message.chat.id, "Ожидается ввод 'Продолжить'. Попробуй еще раз.")
        bot.register_next_step_handler(message, handle_later)
        return
    choice(message)



if __name__ == "__main__":
    bot.polling(none_stop=True)







