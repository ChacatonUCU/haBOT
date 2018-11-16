from telegram.ext import Updater, CommandHandler
from telegram.ext import Filters, MessageHandler
import time
lstgood = []
lstbad = []
i = 0
def start(bot, update):
    greetings = 'Hello {}\n'.format(update.message.from_user.first_name)
    greetings += "I am ready to start."
    update.message.reply_text(greetings)

def saveanswer(bot, update):
    global i
    if i == 1:
        if len(lstgood) < 3:
            lstgood.append(update.message.text)
        elif len(lstbad) < 3:
            lstbad.append(update.message.text)
        else:
            pass
        if len(lstgood) == 3 and len(lstbad) == 0:
            update.message.reply_text("Now type bad films")
        if len(lstgood) == 3 and len(lstbad) == 3:
            i = 0
            update.message.reply_text("All films are entered!")
    else:
        pass


def testik(bot, update):
    update.message.reply_text("Good films" + str(lstgood))
    update.message.reply_text("Bad films" + str(lstbad))

def advice(bot, update):
    lstgood.clear()
    lstbad.clear()
    global i
    i = 1
    update.message.reply_text("Please enter 3 your favourite films")
    # update.message.reply_text("And now please enter 3 worst films")


updater = Updater('787053848:AAF_lcSiJTT0AAIWKX5KmAwbHfxVcTh_KwM')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('advice', advice))
updater.dispatcher.add_handler(MessageHandler(Filters.text, saveanswer))
updater.dispatcher.add_handler(CommandHandler('test', testik))
updater.start_polling()
updater.idle()
