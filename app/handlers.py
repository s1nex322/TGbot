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
from config import API_KEY
from task import theory



detector = ProfanityChecker(API_KEY)

"""from worker import ProfanityChecker
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
        await message.answer(theory['if else'], reply_markup=kb.obch1)
        await state.update_data(topic='if else')
        await state.set_state(st.task_class.task)

    if message.text == "Цикл for":
        await message.answer(theory['for'], reply_markup=kb.obch1)
        await state.update_data(topic='for')
        await state.set_state(st.task_class.task)

    if message.text == "Цикл while":
        await message.answer(theory['while'], reply_markup=kb.obch1)
        await state.update_data(topic='while')
        await state.set_state(st.task_class.task)

    if message.text == "Строки":
        await message.answer(theory['strings'], reply_markup=kb.obch1)
        await state.update_data(topic='strings')
        await state.set_state(st.task_class.task)

    if message.text == "Типы данных":
        await message.answer(theory['datatypes'], reply_markup=kb.obch1)
        await state.update_data(topic='datatypes')
        await state.set_state(st.task_class.task)

    if message.text == "ВЕРНУТСЯ В ГЛАВНОЕ МЕНЮ":
        await state.set_state(st.MAIN.MAIN_MENU)
        await message.answer('ГЛАВНОЕ МЕНЮ', reply_markup=kb.main)

@rt.message(st.MAIN.TASK)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "Условия if else":
        await state.update_data(topic='if else')
        n = len(tasks["if else"])
        await message.answer("Выберите задание", reply_markup=kb.number_keyboard(n))
        await state.set_state(st.task_class.task1)

    if message.text == "Цикл for":
        await state.update_data(topic='for')
        n = len(tasks["for"])
        await message.answer("Выберите задание", reply_markup=kb.number_keyboard(n))
        await state.set_state(st.task_class.task1)

    if message.text == "Цикл while":
        await state.update_data(topic='while')
        n = len(tasks["while"])
        await message.answer("Выберите задание", reply_markup=kb.number_keyboard(n))
        await state.set_state(st.task_class.task1)

    if message.text == "Строки":
        await state.update_data(topic='strings')
        n = len(tasks["strings"])
        await message.answer("Выберите задание", reply_markup=kb.number_keyboard(n))
        await state.set_state(st.task_class.task1)

    if message.text == "Типы данных":
        await state.update_data(topic='datatypes')
        n = len(tasks["datatypes"])
        await message.answer("Выберите задание", reply_markup=kb.number_keyboard(n))
        await state.set_state(st.task_class.task1)

    if message.text == "ВЕРНУТСЯ В ГЛАВНОЕ МЕНЮ":
        await state.set_state(st.MAIN.MAIN_MENU)
        await message.answer('ГЛАВНОЕ МЕНЮ', reply_markup=kb.main)

@rt.message(st.task_class.task)
async def cmd_start1(message: Message, state: FSMContext):
    if message.text == "Отработать материал":
        data = await state.get_data()
        n = len(tasks[data['topic']])
        await message.answer("Выберите задание", reply_markup=kb.number_keyboard(n))
        await state.set_state(st.task_class.task1)

    if message.text == "Изучить другие темы":
        await message.answer('Выберите тему', reply_markup=kb.obch)
        await state.set_state(st.MAIN.EDUC)

@rt.message(st.task_class.task1)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "🎲 случайное задание":
        data = await state.get_data()
        t_task = random.choice(tasks[data['topic']])
        await state.update_data(task=t_task)
        await message.answer(t_task, reply_markup=ReplyKeyboardRemove())
        await message.answer("Отправьте свой ответ для проверки")

        await state.update_data(flag="task")
        await state.set_state(st.task_class.user_answer)


    if message.text == "❌ назад":
        await message.answer('Выберите тему, по которой хотите получить задание.', reply_markup=kb.obch)
        await state.set_state(st.MAIN.TASK)

    else:
        data = await state.get_data()
        t_task = tasks[data["topic"]][int(message.text) - 1]
        await state.update_data(task=t_task)
        await message.answer(t_task, reply_markup=ReplyKeyboardRemove())
        await message.answer("Отправьте свой ответ для проверки")


        await state.update_data(flag="task")
        await state.set_state(st.task_class.user_answer)


@rt.message(st.task_class.user_answer)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(user_answer=message.text)
    data = await state.get_data()

    await message.answer("Подождите, ответ на проверке......")
    result = detector.check_text(data["task"], data["user_answer"])

    #await message.answer(f"Наличие ошибок: {result['has_mistake']}")
    await message.answer(f"Оценка: {result['mark']}/10")
    await message.answer(f"Пояснение: {result['reason']}")

    if data["flag"] == 'task':
        await message.answer("Выберите действие", reply_markup=kb.obch2)
        await state.set_state(st.Navigation.Main_Task)

    if data["flag"] == 'educ':
        await message.answer("Выберите действие", reply_markup=kb.obch1)
        await state.set_state(st.task_class.task)

@rt.message(st.Navigation.Main_Task)
async def cmd_start(message: Message, state: FSMContext):
    if message.text == "Выбрать другое задание":
        data = await state.get_data()
        n = len(tasks[data["topic"]])
        await message.answer("Выберите задание", reply_markup=kb.number_keyboard(n))
        await state.set_state(st.task_class.task1)


    if message.text == "Вернуться в главное меню":
        await state.set_state(st.MAIN.MAIN_MENU)
        await message.answer('ГЛАВНОЕ МЕНЮ', reply_markup=kb.main)








#await state.update_data(get_name=message.text)


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