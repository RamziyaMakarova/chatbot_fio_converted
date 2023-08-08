import time
import logging
from aiogram import Bot, Dispatcher, executor, types

TOKEN = '6045201299:AAGgT6aR7avmn3BCCMmt8HV5N8aHu78S3SI'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(filename='bot.log', level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def transliteration(fio_parts):
    translit_dict = {
        "А": "A","а": "a","Б": "B","б": "b","В": "V","в": "v","Г": "G","г": "g","Д": "D","д": "d","Е": "E","е": "e",
        "Ё": "E","ё": "e","Ж": "ZH","ж": "zh","З": "Z","з": "z","И": "I","и": "i","Й": "I","й": "i","К": "K","к": "k",
        "Л": "L","л": "l","М": "M","м": "m","Н": "N","н": "n","О": "O","о": "o","П": "P","п": "p","Р": "R","р": "r",
        "С": "S","с": "s","Т": "T","т": "t","У": "U","у": "u","Ф": "F","ф": "f","Х": "KH","х": "kh","Ц": "TS","ц": "ts",
        "Ч": "CH","ч": "ch","Ш": "SH","ш": "sh","Щ": "SHCH","щ": "shch","Ы": "Y","ы": "y","Ъ": "IE","ъ": "ie", "Ь": "", "ь": "","Э": "E",
        "э": "e","Ю": "YU","ю": "yu","Я": "YA","я": "ya"}

    transliterated_parts = []
    for word in fio_parts:
        transliterated_word = ""
        for char in word:
            transliterated_word += translit_dict.get(char, char).upper()
        transliterated_parts.append(transliterated_word)

    return " ".join(transliterated_parts)
            

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_ID = message.from_user.id
    user_fullname = message.from_user.full_name
    logging.info(f'{user_ID=} {user_fullname=} {time.asctime()}')
    await message.reply("Привет! Отправь мне свои полные ФИО (пример - Иванов Иван Иванович) на русском языке, и я сделаю их правильную транслитерацию на латинницу!")

@dp.message_handler()
async def convert_fio(message: types.Message):
    logging.info(f'Получено сообщение от пользователя: {message.text}')

    fio = message.text
    fio_parts = fio.split(' ')
    translit_fio = transliteration(fio_parts)

    logging.info(f'Ваше ФИО в международном формате: {translit_fio}')
    await message.reply(f'Ваше ФИО в международном формате: {translit_fio}')

if __name__ == '__main__':
    executor.start_polling(dp)