import os
import ptbot

from decouple import config
from pytimeparse import parse


TG_TOKEN = config('TELEGRAM_TOKEN')
TG_ID = config('TG_CHAT_ID')
START_TIMER = "Запускаю таймер..."
STOP_TIMER = "Время вышло!"


def render_progressbar(
        total, iteration, prefix='',
        suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(text, bot):
    message = bot.send_message(TG_ID, START_TIMER)
    pars_timer = parse(text)
    bot.create_countdown(
        pars_timer, notify_progress,
        chat_id=TG_ID, message_id=message, timer=pars_timer, bot=bot)

    bot.create_timer(parse(text), notify_timer, chat_id=TG_ID, bot=bot)


def notify_progress(secs_left, chat_id, message_id, timer, bot):
    bot.update_message(
        chat_id, message_id,
        "Осталось {} секунд!\n {}".format(
            secs_left,
            render_progressbar(timer, timer-secs_left)))


def notify_timer(chat_id, bot):
    bot.send_message(chat_id, STOP_TIMER)


def main():
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(reply, bot)
    bot.run_bot()


if __name__ == '__main__':
    main()
