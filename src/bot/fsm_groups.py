from aiogram.fsm.state import StatesGroup, State


class SearchStates(StatesGroup):
    search_by_title = State()
    search_by_key = State()
