from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command,CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
import app.keyboards as kb
from aiogram.fsm.context import FSMContext
import app.state as st
from aiogram.fsm.state import StatesGroup, State

rt = Router()

@rt.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Привет!')

    await state.set_state(st.MAIN.MAIN_MENU)
    await message.answer('ГЛАВНОЕ МЕНЮ', reply_markup=kb.main)


@rt.message(st.MAIN.MAIN_MENU)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "Обучение":
        await message.answer('Выберите тему', reply_markup=kb.obch)
        await state.set_state(st.MAIN.EDUC)

    if message.text == "Задания":
        await message.answer('здесь будут задания')


@rt.message(st.MAIN.EDUC)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "Условия if else":
        await message.answer('здесь будет теория по if else')
        await state.set_state(st.topic.topic1)

    if message.text == "Цикл for":
        await message.answer('здесь будет теория по for')

#остальные темы


@rt.message(st.topic.topic1)
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Материал по 1й теме") #здесь то что должно быть в обучении

    await state.set_state(st.topic.topic1_part2)
    await message.answer("Выберите следующее действие", reply_markup = kb.obch1)



@rt.message(st.topic.topic1_part2)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "Изучить другие темы":
        await message.answer('Выберите тему', reply_markup=kb.obch)
        await state.set_state(st.MAIN.EDUC)

    if message.text == "Отработать материал":
        await message.answer("Задания по теме", reply_markup=ReplyKeyboardRemove())



@rt.message(F.text == "ВЕРНУТСЯ В ГЛАВНОЕ МЕНЮ")
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('ГЛАВНОЕ МЕНЮ', reply_markup=kb.main)
    await state.set_state(st.MAIN.MAIN_MENU)

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