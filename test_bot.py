import asyncio
import logging
import aiosqlite
from aiogram import Bot, Dispatcher, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart
from aiogram.enums import ParseMode
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from db import Job, init

API_TOKEN = "6725364063:AAHppfbYZ0NOz4PdZKbMERcvRbIi35tRAJs"

logging.basicConfig(level=logging.INFO)

form_router = Router()


async def get_messages():
    messages = await Job.all()
    return messages


# States
class SendMessage(StatesGroup):
    waiting_for_text = State()


# Start command
@form_router.channel_post()
async def cmd_start(message: types.Message, state: FSMContext):

    # Отримуємо повідомлення з бази даних
    existing_messages = await get_messages()

    # Використовуємо state.proxy(), щоб передати дані у інші функції
    async with state.set_data() as data:
        data['existing_messages'] = existing_messages
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Post"),
            KeyboardButton(text="Cancel"),
            KeyboardButton(text="Autopost")
        ]])

    await state.set_state(SendMessage.waiting_for_text)
    await message.answer("Welcome! Choose an action:", reply_markup=keyboard)


# Handle user's choice
@form_router.channel_post(SendMessage.waiting_for_text)
async def choose_action(message: types.Message, state: FSMContext):
    if message.text.lower() == "post":
        await message.answer("You chose to post. Please enter your message.")
        await state.set_state(SendMessage.waiting_for_text)
    elif message.text.lower() == "cancel":
        await message.answer("You chose to cancel. Action canceled.")
        await state.clear()
    elif message.text.lower() == "autopost":
        await message.answer("Autopost is enabled for future messages.")
        await state.clear()


# Handle user's post
@form_router.channel_post(SendMessage.waiting_for_text)
async def process_post(message: types.Message, state: FSMContext):
    await message.answer(f"Your post is under review:\n\n{message.text}")

    # You can add logic here to send the message for admin review or handle it as needed.

    await state.clear()


async def main():
    await init()

    # Витягуємо повідомлення
    existing_messages = await get_messages()
    if existing_messages:
        response_text = "Existing messages:\n"
        for message in existing_messages:
            response_text += f"User {message.id}, Chat {message.title}:\n{message.description}\n\n"
        print(response_text)
        bot = Bot(token=API_TOKEN)
        dp = Dispatcher(bot=bot)
        dp.include_router(form_router)

        await dp.start_polling(bot)

    else:
        print("No existing messages.")


if __name__ == '__main__':
    asyncio.run(main())
