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

obch2 = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="Выбрать другое задание")],
    [KeyboardButton(text="Вернуться в главное меню")]
])

tasks = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="Условия if else")],
    [KeyboardButton(text="Цикл for")],
    [KeyboardButton(text="Цикл while")],
    [KeyboardButton(text="Типы данных")],
    [KeyboardButton(text="Строки")],
    [KeyboardButton(text="ВЕРНУТСЯ В ГЛАВНОЕ МЕНЮ")]
])


def number_keyboard(n: int) -> ReplyKeyboardMarkup:
    """Простая клавиатура с числами и Random"""

    # Создаем список кнопок с числами
    number_buttons = []
    for i in range(1, n + 1):
        number_buttons.append(KeyboardButton(text=str(i)))

    # Разбиваем на строки (по 5 кнопок в строке)
    rows = []
    row_width = min(5, n)
    for i in range(0, len(number_buttons), row_width):
        rows.append(number_buttons[i:i + row_width])

    # Добавляем строку с Random и Назад
    rows.append([
        KeyboardButton(text="🎲 Random"),
        KeyboardButton(text="❌ назад")
    ])

    # Создаем клавиатуру
    keyboard = ReplyKeyboardMarkup(
        keyboard=rows,
        resize_keyboard=True
    )

    return keyboard