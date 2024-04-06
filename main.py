import telebot

bot = telebot.TeleBot('YOUR TOKEN')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Введите Uzs сумму для конвертации в EUR, USD и RUB:')


@bot.message_handler(func=lambda message: True)
def convert_currency(message):
    try:
        amount = float(message.text)
        eur = round(amount / 12700, 2)
        usd = round(amount / 12450, 2)
        rub = round(amount / 190, 2)
        response = f"EUR: {eur}\nUSD: {usd}\nRUB: {rub}"
        bot.send_message(message.chat.id, response)
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка: неверный формат ввода или недостаточно данных")


