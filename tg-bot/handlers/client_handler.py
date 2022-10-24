from aiogram import Dispatcher
from bot_conf import bot
from keyboards.client_kb import *
from handlers.temp import *
from conf import Lead
from aiogram.dispatcher import FSMContext


async def cmd_start(message: types.message) -> None:
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, reply_msg['hello'].format(message.from_user.first_name),
                               parse_mode='HTML')

        await bot.send_message(message.from_user.id, reply_msg['youget'],
                               parse_mode='HTML', reply_markup=calc_val())


async def kill_state(message: types.message, state: FSMContext) -> None:
    if message.chat.type == 'private':
        await state.finish()
        await bot.send_message(message.from_user.id, reply_msg['hello'].format(message.from_user.first_name),
                               parse_mode='HTML')

        await bot.send_message(message.from_user.id, reply_msg['youget'],
                               parse_mode='HTML', reply_markup=calc_val())


async def get_bld(message: types.Message, state: FSMContext) -> None:
    if message.chat.type == 'private':
        if message.text in txt['bld']:
            async with state.proxy() as data:
                data['bld_type'] = message.text
            await Lead.next()
            await bot.send_message(message.from_user.id, reply_msg['room_am'],
                                   parse_mode='HTML', reply_markup=room_amount_kb())
        elif message.text in txt['cancel']:
            await state.finish()
            await bot.send_message(message.from_user.id, reply_msg['hello'].format(message.from_user.first_name),
                                   parse_mode='HTML')

            await bot.send_message(message.from_user.id, reply_msg['youget'],
                                   parse_mode='HTML', reply_markup=calc_val())
        else:
            await bot.send_message(message.from_user.id, reply_msg['pnx'],
                                   parse_mode='HTML', reply_markup=bld_type_kb())


async def get_room(message: types.Message, state: FSMContext) -> None:
    if message.chat.type == 'private':
        if message.text in txt['room']:
            async with state.proxy() as data:
                data['room_am'] = message.text
            await Lead.next()
            await bot.send_message(message.from_user.id, reply_msg['rpr_type'],
                                   parse_mode='HTML', reply_markup=rpr_type_kb())
        elif message.text in txt['cancel']:
            await state.finish()
            await bot.send_message(message.from_user.id, reply_msg['hello'].format(message.from_user.first_name),
                                   parse_mode='HTML')

            await bot.send_message(message.from_user.id, reply_msg['youget'],
                                   parse_mode='HTML', reply_markup=calc_val())
        else:
            await bot.send_message(message.from_user.id, reply_msg['pnx'],
                                   parse_mode='HTML', reply_markup=room_amount_kb())


async def get_rpr(message: types.Message, state: FSMContext) -> None:
    if message.chat.type == 'private':
        if message.text in txt['rpr']:
            async with state.proxy() as data:
                data['rpr_type'] = message.text
            await Lead.next()
            await bot.send_message(message.from_user.id, reply_msg['area'],
                                   parse_mode='HTML', reply_markup=otm_kb())
        elif message.text in txt['cancel']:
            await state.finish()
            await bot.send_message(message.from_user.id, reply_msg['hello'].format(message.from_user.first_name),
                                   parse_mode='HTML')

            await bot.send_message(message.from_user.id, reply_msg['youget'],
                                   parse_mode='HTML', reply_markup=calc_val())
        else:
            await bot.send_message(message.from_user.id, reply_msg['pnx'],
                                   parse_mode='HTML', reply_markup=rpr_type_kb())


async def get_area(message: types.Message, state: FSMContext) -> None:
    if message.chat.type == 'private':
        if message.text in txt['cancel']:
            await state.finish()
            await bot.send_message(message.from_user.id, reply_msg['hello'].format(message.from_user.first_name),
                                   parse_mode='HTML')
            await bot.send_message(message.from_user.id, reply_msg['youget'],
                                   parse_mode='HTML', reply_markup=calc_val())
            return

        async with state.proxy() as data:
            data['area'] = message.text
        await Lead.next()
        await bot.send_message(message.from_user.id, reply_msg['gifts'],
                               parse_mode='HTML', reply_markup=gift_kb())


async def get_gift(message: types.Message, state: FSMContext) -> None:
    if message.chat.type == 'private':
        if message.text in txt['gift']:
            async with state.proxy() as data:
                data['gift_name'] = message.text
            await Lead.next()
            await bot.send_message(message.from_user.id, reply_msg['which_num'],
                                   parse_mode='HTML', reply_markup=otm_kb())
        elif message.text in txt['cancel']:
            await state.finish()
            await bot.send_message(message.from_user.id, reply_msg['hello'].format(message.from_user.first_name),
                                   parse_mode='HTML')

            await bot.send_message(message.from_user.id, reply_msg['youget'],
                                   parse_mode='HTML', reply_markup=calc_val())
        else:
            await bot.send_message(message.from_user.id, reply_msg['pnx'],
                                   parse_mode='HTML', reply_markup=gift_kb())


async def get_pnumber(message: types.Message, state: FSMContext) -> None:
    if message.chat.type == 'private':
        if message.text in txt['cancel']:
            await state.finish()
            await bot.send_message(message.from_user.id, reply_msg['hello'].format(message.from_user.first_name),
                                   parse_mode='HTML')

            await bot.send_message(message.from_user.id, reply_msg['youget'],
                                   parse_mode='HTML', reply_markup=calc_val())
            return

        if not await Lead.check_num(message.text):
            await bot.send_message(message.from_user.id, reply_msg['unc_num'],
                                   parse_mode='HTML', reply_markup=otm_kb())
            return

        async with state.proxy() as data:
            data['p_number'] = message.text
            data['cl_name'] = message.from_user.first_name
        await Lead.send(await state.get_data())
        await state.finish()
        await bot.send_message(message.from_user.id, reply_msg['urls'],
                               parse_mode='HTML', reply_markup=one_more_time_kb())


async def msg_hlr(message: types.message) -> None:
    if message.chat.type == 'private':

        if message.text in txt['calc']:
            await bot.send_message(message.from_user.id, reply_msg['where_obj'],
                                   parse_mode='HTML', reply_markup=bld_type_kb())
            await Lead.bld_type.set()

        elif (message.text in txt['rst']) or (message.text in txt['cancel']):
            await bot.send_message(message.from_user.id, reply_msg['hello'].format(message.from_user.first_name),
                                   parse_mode='HTML')
            await bot.send_message(message.from_user.id, reply_msg['youget'],
                                   parse_mode='HTML', reply_markup=calc_val())

        else:
            await bot.send_message(message.from_user.id, reply_msg['pnx'],
                                   parse_mode='HTML', reply_markup=calc_val())


def client_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(kill_state, commands=['start'], state='*')
    dp.register_message_handler(get_bld, content_types=['text'], state=Lead.bld_type)
    dp.register_message_handler(get_room, content_types=['text'], state=Lead.room_am)
    dp.register_message_handler(get_rpr, content_types=['text'], state=Lead.rpr_type)
    dp.register_message_handler(get_area, content_types=['text'], state=Lead.area)
    dp.register_message_handler(get_gift, content_types=['text'], state=Lead.gift_name)
    dp.register_message_handler(get_pnumber, content_types=['text'], state=Lead.p_number)
    dp.register_message_handler(msg_hlr, content_types=['text'])
