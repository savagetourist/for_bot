import config
import telebot

bot = telebot.Telebot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, messaage.text)

if __name__ == '__main__':
    bot.polling(none_stop=true)

python3 bot.py