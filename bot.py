"""
It is draft file
"""

from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('787053848:AAF_lcSiJTT0AAIWKX5KmAwbHfxVcTh_KwM')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
