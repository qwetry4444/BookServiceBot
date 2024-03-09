from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery


class RegisterCheck(BaseMiddleware):
    """
    Middleware будет вызываться каждый раз, когда пользователь будет отправлять боту сообщения (или нажимать
    на кнопку в инлайн-клавиатуре).
    """

    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        """ Сама функция для обработки вызова """
        if event.web_app_data:
            return await handler(event, data)
        db = data['db']
        session_maker = data['session_maker']
        user = event.from_user

        # Получаем менеджер сессий из ключевых аргументов, переданных в start_polling()
        if not await db.user.is_user_exists(user_id=event.from_user.id):
            await db.user.new(user_id=event.from_user.id,
                                  username=event.from_user.username)
            await data['bot'].send_message(event.from_user.id, 'Ты успешно зарегистрирован(а)!')

        return await handler(event, data)
