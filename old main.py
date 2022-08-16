from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import  InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , KeyboardButton
import asyncio
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile
logging.basicConfig(level=logging.INFO)
bot=Bot(token="5257387537:AAFqA-m4salCEV0SAcbJgmqW9uCh4WkGXWU")
dp=Dispatcher(bot, storage=MemoryStorage())
def decode(emoji, name):
    emoji = emoji.encode('utf-16',"surrogatepass").decode('utf-16', "surrogatepass")
    return str(emoji+' '+name)
rb1 = KeyboardButton(decode('\ud83d\udcb5','Цены на рекламу'))
rb2 = KeyboardButton('Статистика группы')
rb3 = KeyboardButton(decode('\ud83d\udcf2','Контакты'))
start_rb= ReplyKeyboardMarkup(resize_keyboard=True).row(rb1).row(rb2).row(rb3)
Inl_rb1 = InlineKeyboardButton('Чат Telegram',url='https://t.me/AGMoon1982')
Inl_rb2 = InlineKeyboardButton('Чат WhatsApp',url='https://wa.me/+79639024849')
Inl_start_rb = InlineKeyboardMarkup().row(Inl_rb1).row(Inl_rb2)
@dp.message_handler(commands=['start'])
async def starter(message:types.Message):
    start_photo = InputFile('hi.jpg')
    await message.answer(f"Здравствуйте! {message['from']['first_name']}\n"
                         f"Вас приветствует бот сообщества \n"
                         f"Мамы и Папы Затона")
    await bot.send_photo(chat_id=message.chat.id, photo=start_photo, reply_markup=start_rb)
@dp.message_handler(Text(equals=[decode('\ud83d\udcb5','Цены на рекламу')]))
async def starter(message:types.Message):
    await message.answer('Цены на рекламу в паблике "Мамы затона":\n\n'
                         '1 незакрепленнный пост 130 руб.\n'
                         '4 незакрепленнных поста (1 раз в неделю) 440 руб.\n'
                         '8 незакрепленных постов (2 раза в неделю) 800 руб.\n\n'
                         '1 закреп на сутки 200 руб.\n'
                         '3 закрепа на сутки 450 руб.\n'
                         '5 закрепов на сутки 550 руб.\n\n'
                         'Пост включает в себя текст рекламодателя, 1 ссылку, до 10 фото/видео.')
@dp.message_handler(Text(equals='Статистика группы'))
async def starter(message:types.Message):
    await message.answer('Статистика группы ВК : https://vk.com/stats?gid=19265924')
@dp.message_handler(Text(equals=[decode('\ud83d\udcf2','Контакты')]))
async def starter(message:types.Message):
    await message.answer('Группа ВК: https://vk.com/public19265924\n\n'
                         'Instagram: https://instagram.com/mamy_i_papy_zatona?utm_medium=copy_link\n\n'
                         'Администратор: Айгуль',reply_markup=Inl_start_rb)
@dp.message_handler()
async def starter(message:types.Message):
    await message.answer('Я вас не понял , для старта напишите команду "/start"')
if __name__== "__main__":
    loop = asyncio.get_event_loop()
    executor.start_polling(dp)