from aiogram import types,Router
from aiogram.filters import CommandStart,Command
import random
user_private_router=Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Hello, I*m your personal bot')

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer('MENU: \n1. /menu\n2. /help\n3. /echo\n4. /start\n')  

@user_private_router.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer('HELP:i wont help you') 

@user_private_router.message(Command('echo'))
async def echo_cmd(message: types.Message):
   await message.reply(message.text)



@user_private_router.message()
async def echo(message: types.Message):
    listOf=['hi', 'hello', 'привіт','добрий день']
    text=message.text.lower()
    randomCoice=random.choice(listOf)
    if text in ['hi', 'hello', 'привіт','добрий день']:
        await message.answer(randomCoice)
    elif text in ['by', 'goodbye']:
        await message.answer('By,my friend')
    else:
        await message.answer('i don*t understand, repeat please')
    # await message.answer(message.text)
    # await message.reply(message.text)
    # await message.reply(message.text+str(message.from_user.id))
    