from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="Обучение")],
    [KeyboardButton(text="Задания")]
])

obch = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="Условия if else")],
    [KeyboardButton(text="Цикл for")],
    [KeyboardButton(text="Цикл while")],
    [KeyboardButton(text="Типы данных")],
    [KeyboardButton(text="Строки")],
    [KeyboardButton(text="ВЕРНУТСЯ В ГЛАВНОЕ МЕНЮ")]
])

obch1 = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="Изучить другие темы")],
    [KeyboardButton(text="Отработать материал")]
])

tasks = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="Условия if else")],
    [KeyboardButton(text="Цикл for")],
    [KeyboardButton(text="Цикл while")],
    [KeyboardButton(text="Типы данных")],
    [KeyboardButton(text="Строки")],
    [KeyboardButton(text="ВЕРНУТСЯ В ГЛАВНОЕ МЕНЮ")]
])