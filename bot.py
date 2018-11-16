from telegram.ext import Updater, CommandHandler


def start(bot, update):
    greetings = 'Hello {}\n'.format(update.message.from_user.first_name)
    greetings += "I am ready to start."
    update.message.reply_text(greetings)


def advice(bot, update):
    def film_append_helper(lst):
        iterator,used = 0,[]
        while iterator < 3:
            # text = messages
            if not text.startwith("/"):
                lst_best.append(text)
                iterator += 1
                used.append(text)
                print(lst)

    
    lst_best, lst_worst = [], []
    update.message.reply_text("Please enter 3 your favourite films")
    film_append_helper(lst_best)
    update.message.reply_text("And now please enter 3 worst films")
    film_append_helper(lst_worst)
    print(lst_best)
    print(lst_worst)

# def hello(bot, update):
#     update.message.reply_text(
#         'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('787053848:AAF_lcSiJTT0AAIWKX5KmAwbHfxVcTh_KwM')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('advice', advice))

updater.start_polling()
updater.idle()
