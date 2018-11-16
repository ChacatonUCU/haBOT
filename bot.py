from telegram.ext import Updater, CommandHandler


def start(bot, update):
    greetings = 'Hello {}\n'.format(update.message.from_user.first_name)
    greetings += "Are you ready to start?"
    update.message.reply_text(greetings)


# def hello(bot, update):
#     update.message.reply_text(
#         'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('787053848:AAF_lcSiJTT0AAIWKX5KmAwbHfxVcTh_KwM')

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
