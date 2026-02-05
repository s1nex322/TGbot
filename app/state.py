from aiogram.fsm.state import StatesGroup, State

class MAIN(StatesGroup):
    MAIN_MENU = State()
    EDUC = State()
    TASK = State()

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

class checker(StatesGroup):
    check_ifelse = State()
    check_for = State()
    check_while = State()
    check_datatypes = State()
    check_strings = State()

class ifelse(StatesGroup):
    task = State()
    user_answer = State()
