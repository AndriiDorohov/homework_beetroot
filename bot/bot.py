from os import getenv

from aiogram import Bot, Dispatcher, executor
from aiogram.types import (
    InlineQueryResultArticle,
    Message,
    InlineQuery,
    InputTextMessageContent,
    input_message_content,
)
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def start_command_handler(message: Message):
    await message.answer("Hello my friend")


@dp.message_handler(commands="photo")
async def send_photo(message: Message):
    with open("photo/bot.png", "rb") as photo:
        await bot.send_photo(message.chat.id, photo=photo, caption="Here you go)")


@dp.inline_handler
async def inline_echo(inline_query: InlineQuery):
    text = inline_query.query or "echo"
    input_content = InputTextMessageContent(text)
    result = hashlibib.md5(text.encode()).hexdigest()
    item = InlineQueryResultArticle(
        id=result, title=f"Result {text}", input_message_content=input_content
    )
    await bot.answer_inline_query(inline_query.id, result=[item], caсhe_time=1)


@dp.message_handler()
async def echo(message: Message):
    # await bot.send_message(message.chat.id, message.text)
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
