import aiohttp
import re
from zeon.conf import api
from aiogram.dispatcher.filters.state import State, StatesGroup


BOT_TOKEN = ''
symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+']


class Lead(StatesGroup):
    bld_type = State()
    room_am = State()
    rpr_type = State()
    area = State()
    gift_name = State()
    p_number = State()
    cl_name = State()

    @staticmethod
    async def send(data: dict) -> None:
        tmp = {
            'phone': data['p_number'],
            'name': data['cl_name'],
            'site_id': api['site_id'],
            'title': f'Тип объекта: {data["bld_type"]}, '
                     f'Количество комнат: {data["room_am"]}, '
                     f'Вид ремонта: {data["rpr_type"]}, '
                     f'Площадь объекта: {data["area"]}, '
                     f'Подарок: {data["gift_name"]}'
        }
        async with aiohttp.ClientSession() as session:
            await session.post(f'{api["url"]}', json=tmp,
                               headers={'Authorization': f'Bearer {api["api_token"]}'})

    @staticmethod
    async def check_num(num: str) -> bool:
        n = re.sub(r'\s+', '', num, flags=re.UNICODE)
        n = n.strip('+')
        if len(n) != 11:
            return False
        for sym in n:
            if sym not in symbols:
                return False
        return True
