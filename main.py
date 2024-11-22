import os
import ptbot


def main():
    tg_token = os.getenv('TG_TOKEN')
    tg_id = os.getenv('TG_CHAT_ID')
    bot = ptbot.Bot(tg_token)
    bot.send_message(tg_id, "Бот запущен")


if __name__ == '__main__':
    main()
