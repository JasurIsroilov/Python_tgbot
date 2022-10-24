from aiogram import types


def calc_val() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='👉РАССЧИТАТЬ СТОИМОСТЬ')
    markup.add(btn1)
    return markup


def bld_type_kb() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Новостройка')
    btn2 = types.KeyboardButton(text='Вторичка')
    btn3 = types.KeyboardButton(text='Дом')
    btn4 = types.KeyboardButton(text='Отмена')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    return markup


def room_amount_kb() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Одна комната')
    btn2 = types.KeyboardButton(text='Две комнаты')
    btn3 = types.KeyboardButton(text='Три и более')
    btn4 = types.KeyboardButton(text='Отмена')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    return markup


def rpr_type_kb() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Эконом')
    btn2 = types.KeyboardButton(text='Комфорт')
    btn3 = types.KeyboardButton(text='Бизнес')
    btn4 = types.KeyboardButton(text='Отмена')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    return markup


def one_more_time_kb() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='👉Рассчитать еще раз!')
    markup.add(btn1)
    return markup


def otm_kb() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Отмена')
    markup.add(btn1)
    return markup


def gift_kb() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Концепция интерьера в подарок')
    btn3 = types.KeyboardButton(text='Натяжной потолок в подарок')
    btn2 = types.KeyboardButton(text='Межкомнатные двери в подарок')
    btn4 = types.KeyboardButton(text='Черновые материалы в подарок')
    btn5 = types.KeyboardButton(text='Отмена')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    return markup
