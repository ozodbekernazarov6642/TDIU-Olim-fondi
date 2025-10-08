from aiogram.dispatcher.filters.state import StatesGroup, State


class AppealStates(StatesGroup):
    writing = State()


class SendFile(StatesGroup):
    student_list = State()
    theme = State()
    send_file = State()
