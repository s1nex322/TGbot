from aiogram.fsm.state import StatesGroup, State

class Main(StatesGroup):
    MAIN_MENU = State()
    EDUC = State()

class task(StatesGroup):
    task1 = State()
    task2 = State()
    task3 = State()
    task4 = State()
    task5 = State()

class topic(StatesGroup):
    topic1 = State()
    topic1_part2 = State()
    topic2 = State()
    topic3 = State()
    topic4 = State()
    topic5 = State()