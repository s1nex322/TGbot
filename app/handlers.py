from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command,CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
import app.keyboards as kb

rt = Router()


@rt.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)


@rt.message(F.text == "ВЕРНУТСЯ В ГЛАВНОЕ МЕНЮ")
async def cmd_start(message: Message):
    await message.answer('ГЛАВНОЕ МЕНЮ', reply_markup=kb.main)


@rt.message((F.text == "Обучение") | (F.text == "Изучить другие темы" ))
async def cmd_start(message: Message):
    await message.answer('Выберите тему', reply_markup=kb.obch)


@rt.message((F.text == "Задания") | (F.text == "Отработать материал" ))
async def cmd_start(message: Message):
    await message.answer('здесь будут задания')


@rt.message(F.text == "Условия if else")
async def cmd_start(message: Message):
    await message.answer('Условия *if/else* в Python — это конструкция для принятия решений в программе. Она позволяет выполнять разные блоки кода в зависимости от истинности условий.\n*Основные элементы:*\n*1.if* — проверяет условие, если оно истинно (True), выполняется блок кода после него\n*2.elif (else if)* — проверяет дополнительное условие, если предыдущие условия ложны\n*3.else* — выполняется, если все предыдущие условия ложны', parse_mode='Markdown', reply_markup=kb.obch1)


@rt.message(F.text == "Цикл for")
async def cmd_start(message: Message):
    await message.answer('2', reply_markup=ReplyKeyboardRemove())


@rt.message(F.text == "Цикл while")
async def cmd_start(message: Message):
    await message.answer('3', reply_markup=ReplyKeyboardRemove())


@rt.message(F.text == "Типы данных")
async def cmd_start(message: Message):
    await message.answer('4', reply_markup=ReplyKeyboardRemove())


@rt.message(F.text == "Строки")
async def cmd_start(message: Message):
    await message.answer('5', reply_markup=ReplyKeyboardRemove())