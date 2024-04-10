import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('6992423949:AAH4RayH93oKlkDnlBc-UpASqqg-mncfguc')

@bot.message_handler(commands=['start'])
def start_message(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f'{user_name}, привет! Я чат бот и я очень рад с тобой пообщаться!')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMsZhGaHyfLfgp-U1dcXgI-dtJdVFgAAg0AA8A2TxOk-eH01HiNUzQE')
    bot.send_message(message.chat.id,  "Я буду напоминать тебе о предстоящих ежедневных событиях.")
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    bot.reply_to(message, 'Я работаю благодаря Python.')
    list = ["**Python интерпретируемый язык программирования – код на нем выполняется построчно, в режиме реального "
            "времени. Это свойство позволяет быстро исправлять и проверять код без необходимости компиляции.",
            "**Python был разработан Гвидо ван Россумом в конце 80-х - начале 90-х годов в Национальном "
            "исследовательском институте математики и компьютерных наук в Нидерландах.",
            "**Python является производным от многих других языков, включая ABC, Modula-3, C, C ++, Algol-68, SmallTalk",
            "**Python поддерживает объектно-ориентированное программирование (ООП), что позволяет разрабатывать код "
            "в виде объектов, которые взаимодействуют друг с другом. Это делает код более модульным "
            "и повторно используемым.",
            "**Python является языком с динамической типизацией, то есть тип переменной определяется автоматически, "
            "во время выполнения кода. Это упрощает процесс программирования и делает его гибким при работе "
            "с данными различного типа."
    ]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Лови факт о Python: \n {random_fact}')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Вот общие команды, которые вы можете использовать:\n"
                             "/start - начать работу с ботом\n"
                             "/help - получить это сообщение помощи\n"
                             "/fact - получить отдельные сведения о языке программирования Python\n"
                             "Если вам нужна дополнительная помощь, пожалуйста, свяжитесь с поддержкой.")
def send_reminders(chat_id):
    reminder1 = "17:29:00"
    reminder2 = "17:31:00"
    reminder3 = "17:32:00"
    print(reminder1)
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(now)
        if now == reminder1:
            bot.send_message(chat_id, "Оперативка через 5 минут!")
            time.sleep(2)

        if now == reminder2:
            bot.send_message(chat_id, "Выпей стакан воды. Через 15 минут - время идти на обед.")
            time.sleep(2)

        if now == reminder3:
            bot.send_message(chat_id, "Время подвести итоги дня. Через 30 минут - окончание работы.")
            time.sleep(61)

        time.sleep(1)




bot.polling(none_stop=True)
