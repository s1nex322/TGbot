from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command,CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
import app.keyboards as kb
from aiogram.fsm.context import FSMContext
import app.state as st
from aiogram.fsm.state import StatesGroup, State
from task import tasks
import random
from worker import ProfanityChecker


API_KEY = "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"
detector = ProfanityChecker(API_KEY)

"""from worker import ProfanityChecker
API_KEY = "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"
detector = ProfanityChecker(API_KEY)

#Пример 1 (правильный ответ)
test_task = 'Напишите код, который ищет сумму от 1 до 10, используя циклы'
test_decision = '''
res = 0
for i in range(1, 11):
    res += i
print(res)
'''

result = detector.check_text(test_task, test_decision)

print(f"Наличие ошибок: {result['has_mistake']}")
print(f"Оценка: {result['mark']}")
print(f"Пояснение: {result['reason']}")
"""
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
        await state.set_state(st.MAIN.TASK)
        await message.answer('Выберите тему, по которой хотите получить задание.', reply_markup=kb.obch)


@rt.message(st.MAIN.EDUC)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "Условия if else":
        await message.answer('Условия *if/else* в Python — это конструкция для принятия решений в программе. Она позволяет выполнять разные блоки кода в зависимости от истинности условий.\n*Основные элементы:*\n*1.if* — проверяет условие, если оно истинно (True), выполняется блок кода после него\n*2.elif (else if)* — проверяет дополнительное условие, если предыдущие условия ложны\n*3.else* — выполняется, если все предыдущие условия ложны', parse_mode='Markdown', reply_markup=kb.obch1)
        await state.set_state(st.ifelse.task)

    if message.text == "Цикл for":
        await message.answer('здесь будет теория по for', reply_markup = kb.obch1)
        await state.set_state(st.topic.topic2)

    if message.text == "Цикл while":
        await message.answer('здесь будет теория по while', reply_markup = kb.obch1)
        await state.set_state(st.topic.topic3)

    if message.text == "Строки":
        await message.answer('здесь будет теория по строкам', reply_markup = kb.obch1)
        await state.set_state(st.topic.topic4)

    if message.text == "Типы данных":
        await message.answer('здесь будет теория по типам данных', reply_markup = kb.obch1)
        await state.set_state(st.topic.topic5)

    if message.text == "ВЕРНУТСЯ В ГЛАВНОЕ МЕНЮ":
        await state.set_state(st.MAIN.MAIN_MENU)
        await message.answer('ГЛАВНОЕ МЕНЮ', reply_markup=kb.main)

@rt.message(st.MAIN.TASK)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "Условия if else":
        await message.answer('Условия *if/else* в Python — это конструкция для принятия решений в программе. Она позволяет выполнять разные блоки кода в зависимости от истинности условий.\n*Основные элементы:*\n*1.if* — проверяет условие, если оно истинно (True), выполняется блок кода после него\n*2.elif (else if)* — проверяет дополнительное условие, если предыдущие условия ложны\n*3.else* — выполняется, если все предыдущие условия ложны', parse_mode='Markdown', reply_markup=kb.obch1)
        await state.set_state(st.ifelse.task)

    if message.text == "Цикл for":
        await message.answer('здесь будет теория по for', reply_markup=kb.obch1)
        await state.set_state(st.topic.topic2)

    if message.text == "Цикл while":
        await message.answer('здесь будет теория по while', reply_markup=kb.obch1)
        await state.set_state(st.topic.topic3)

    if message.text == "Строки":
        await message.answer('здесь будет теория по строкам', reply_markup=kb.obch1)
        await state.set_state(st.topic.topic4)

    if message.text == "Типы данных":
        await message.answer('здесь будет теория по типам данных', reply_markup=kb.obch1)
        await state.set_state(st.topic.topic5)

    if message.text == "ВЕРНУТСЯ В ГЛАВНОЕ МЕНЮ":
        await state.set_state(st.MAIN.MAIN_MENU)
        await message.answer('ГЛАВНОЕ МЕНЮ', reply_markup=kb.main)


@rt.message(st.ifelse.task)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "Изучить другие темы":
        await message.answer('Выберите тему', reply_markup=kb.obch)
        await state.set_state(st.MAIN.EDUC)

    if message.text == "Отработать материал":
        t_task = random.choice(tasks["if else"])
        await state.update_data(task=t_task)

        await message.answer(t_task, reply_markup=ReplyKeyboardRemove())
        await message.answer("Отправьте свой ответ для проверки")
        await state.set_state(st.ifelse.user_answer)

@rt.message(st.ifelse.user_answer)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(user_answer=message.text)
    data = await state.get_data()

    await message.answer("Подождите, ответ на проверке......")
    result = detector.check_text(data["task"], data["user_answer"])

    #await message.answer(f"Наличие ошибок: {result['has_mistake']}")
    await message.answer(f"Оценка: {result['mark']}/10")
    await message.answer(f"Пояснение: {result['reason']}", reply_markup=kb.obch1)
    await state.set_state(st.ifelse.task)







#await state.update_data(get_name=message.text)

@rt.message(st.topic.topic2)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "Изучить другие темы":
        await message.answer('Выберите тему', reply_markup=kb.obch)
        await state.set_state(st.MAIN.EDUC)

    if message.text ==  "Отработать материал":
        await message.answer(random.choice(tasks["for"]), reply_markup=ReplyKeyboardRemove())
        await message.answer("Отправьте свой ответ для проверки")
        await state.set_state(st.checker.check_for)


@rt.message(st.topic.topic3)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "Изучить другие темы":
        await message.answer('Выберите тему', reply_markup=kb.obch)
        await state.set_state(st.MAIN.EDUC)

    if message.text == "Отработать материал":
        await message.answer(random.choice(tasks["while"]), reply_markup=ReplyKeyboardRemove())
        await message.answer("Отправьте свой ответ для проверки")
        await state.set_state(st.checker.check_while)


@rt.message(st.topic.topic4)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "Изучить другие темы":
        await message.answer('Выберите тему', reply_markup=kb.obch)
        await state.set_state(st.MAIN.EDUC)

    if message.text == "Отработать материал":
        await message.answer(random.choice(tasks["datatypes"]), reply_markup=ReplyKeyboardRemove())
        await message.answer("Отправьте свой ответ для проверки")
        await state.set_state(st.checker.check_datatypes)


@rt.message(st.topic.topic5)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "Изучить другие темы":
        await message.answer('Выберите тему', reply_markup=kb.obch)
        await state.set_state(st.MAIN.EDUC)

    if message.text == "Отработать материал":
        await message.answer(random.choice(tasks["strings"]), reply_markup=ReplyKeyboardRemove())
        await message.answer("Отправьте свой ответ для проверки")
        await state.set_state(st.checker.check_strings)

"""
@rt.message(st.checker.check_ifelse)
async def cmd_start(message: Message, state: FSMContext):


@rt.message(st.checker.check_for)
async def cmd_start(message: Message, state: FSMContext):


@rt.message(st.checker.check_while)
async def cmd_start(message: Message, state: FSMContext):


@rt.message(st.checker.check_datatypes)
async def cmd_start(message: Message, state: FSMContext):

@rt.message(st.checker.check_strings)
async def cmd_start(message: Message, state: FSMContext):




@rt.message(F.text == "ВЕРНУТСЯ В ГЛАВНОЕ МЕНЮ")
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('ГЛАВНОЕ МЕНЮ', reply_markup=kb.main)
    await state.set_state(st.MAIN.MAIN_MENU)

@rt.message((F.text == "Обучение") | (F.text == "Изучить другие темы" ))
async def cmd_start(message: Message):
    await message.answer('Выберите тему', reply_markup=kb.obch)
"""
"""
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
"""