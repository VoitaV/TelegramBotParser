# import random
import telebot
import config
# from bs4 import BeautifulSoup as bs
import requests
import top500

telebot.apihelper.ENABLE_MIDDLEWARE = True
bot = telebot.TeleBot(config.token)
name = ''

url_500_1 = 'https://en.kinorium.com/collections/kinorium/300/?order=sequence&page='
url_500_2 = '&perpage=100&show_viewed=1'
teg_500 = 'i'
class_500 = 'movie-title__text filmList__item-title-link-popup link-info-movie-type-film'
teg_genre_500 = 'p'
class_genre_500 = 'filmList__extra-info'

url_pop_1 = 'https://en.kinorium.com/collections/kinorium/1098/?order=sequence&page='
url_pop_2 = '&perpage=100&show_viewed=1'
teg_pop = 'i'
class_pop = 'movie-title__text filmList__item-title-link-popup link-info-movie-type-film'
teg_genre_pop = 'p'
class_genre_pop = 'filmList__extra-info'

url_anim_1 = 'https://en.kinorium.com/collections/kinorium/315/?order=sequence&page='
url_anim_2 = '&perpage=20&show_viewed=1'
teg_anim = 'i'
class_anim = 'movie-title__text filmList__item-title-link-popup link-info-movie-type-film'
teg_genre_anim = 'p'
class_genre_anim = 'filmList__extra-info'

url_horror_1 = 'https://en.kinorium.com/collections/kinorium/321/?order=sequence&page='
url_horror_2 = '&perpage=20&show_viewed=1'
teg_horror = 'i'
class_horror = 'movie-title__text filmList__item-title-link-popup link-info-movie-type-film'
teg_genre_horror = 'p'
class_genre_horror = 'filmList__extra-info'

url_comedy_1 = 'https://en.kinorium.com/collections/kinorium/311/?order=sequence&page='
url_comedy_2 = '&perpage=50&show_viewed=1'
teg_comedy = 'i'
class_comedy = 'movie-title__text filmList__item-title-link-popup link-info-movie-type-film'
teg_genre_comedy = 'p'
class_genre_comedy = 'filmList__extra-info'

url_fant_1 = 'https://en.kinorium.com/collections/kinorium/323/?order=sequence&page='
url_fant_2 = '&perpage=100&show_viewed=1'
teg_fant = 'i'
class_fant = 'movie-title__text filmList__item-title-link-popup link-info-movie-type-film'
teg_genre_fant = 'p'
class_genre_fant = 'filmList__extra-info'


@bot.message_handler(commands=['start'])
def start_com(message):
    poem = 'Welcome to my bot!\nWhat is your name?'
    bot.send_message(message.chat.id, poem)
    bot.register_next_step_handler(message, reg_name)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, f'Nice to meet you, {name}!\nTo begin write /launch\n'
                                      f'If you need any help - write /help')


@bot.message_handler(commands=['help'])
def help_com(message):
    help_text = '''
    To begin - write command /launch
    If you need help - write /help
    To restart - write command /start
    While working with this bot - use buttons
    '''
    bot.send_message(message.chat.id, help_text)

def keyboard_launch():
    keyb_markup = telebot.types.ReplyKeyboardMarkup()
    button_genre = telebot.types.KeyboardButton('Movie genres')
    button_rand_popular = telebot.types.KeyboardButton('Random popular movie')
    button_rand_500best = telebot.types.KeyboardButton('Random movie from 500 best')
    keyb_markup.row(button_genre)
    keyb_markup.row(button_rand_popular)
    keyb_markup.row(button_rand_500best)
    return keyb_markup

def keyboard_genre():
    keyb_genre_reply = telebot.types.InlineKeyboardMarkup()
    key_comedy = telebot.types.InlineKeyboardButton(text='Comedy', callback_data='comedy')
    key_mult = telebot.types.InlineKeyboardButton(text='Animation', callback_data='mult')
    key_fantasy = telebot.types.InlineKeyboardButton(text='Fantasy', callback_data='fantasy')
    key_horror = telebot.types.InlineKeyboardButton(text='Horror', callback_data='horror')
    keyb_genre_reply.add(key_comedy, key_mult, key_fantasy, key_horror)
    return keyb_genre_reply

@bot.message_handler(commands=['launch'])
def launch_com(message):
    bot.send_message(message.chat.id, 'Lets go!', reply_markup=keyboard_launch())

@bot.message_handler(content_types=['text'])
def genre_reply(message):
    if message.text == 'Movie genres':
        bot.send_message(message.chat.id, 'Choose one genre', reply_markup=keyboard_genre())
    if message.text == 'Random popular movie':
        bot.send_message(message.chat.id, top500.spisok_500(url_pop_1, url_pop_2, teg_pop, class_pop,
                                                            teg_genre_pop, class_genre_pop))
    if message.text == 'Random movie from 500 best':
        bot.send_message(message.chat.id, top500.spisok_500(url_500_1, url_500_2, teg_500, class_500,
                                                            teg_genre_500, class_genre_500,))


@bot.callback_query_handler(func=lambda call: True)
def genre_reply_button(call):
    if call.data == 'fantasy':
        bot.send_message(call.message.chat.id, 'You chose fantasy')
        bot.send_message(call.message.chat.id, top500.spisok_500(url_fant_1, url_fant_2, teg_fant, class_fant,
                                                            teg_genre_fant, class_genre_fant))
    if call.data == 'mult':
        bot.send_message(call.message.chat.id, 'You chose animation')
        bot.send_message(call.message.chat.id, top500.spisok_500(url_anim_1, url_anim_2, teg_anim, class_anim,
                                                            teg_genre_anim, class_genre_anim))
    if call.data == 'comedy':
        bot.send_message(call.message.chat.id, 'You chose comedy')
        bot.send_message(call.message.chat.id, top500.spisok_500(url_comedy_1, url_comedy_2, teg_comedy, class_comedy,
                                                         teg_genre_comedy, class_genre_comedy))
    if call.data == 'horror':
        bot.send_message(call.message.chat.id, 'You chose horror')
        bot.send_message(call.message.chat.id, top500.spisok_500(url_horror_1, url_horror_2, teg_horror, class_horror,
                                                         teg_genre_horror, class_genre_horror))


@bot.middleware_handler(update_types=['message'])
def get_post_views(bot_instance, message):
    url = f"https://api.telegram.org/bot{config.token}/getChatMembersCount"
    params = {
        "chat_id": message.chat.id,
        "message_id": message.id
    }
    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code == 200:
        return print(str(data), data["result"], message.chat.id, message.id)
    else:
        return None




bot.infinity_polling()
