import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import executor

BOT_TOKEN = "8736006180:AAFJQ6jHk4zetE107KLSi0SLJx2cQB53fXk"
CHANNEL_LINK = "https://t.me/RATCHEATSHOP"
SUPPORT_LINK = "https://t.me/RATCHEATSHOP1"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
kb_menu = InlineKeyboardMarkup(row_width=2)
kb_menu.add(
    InlineKeyboardButton("Каталог", callback_data="catalog"),
    InlineKeyboardButton("Отзывы / файлы", callback_data="reviews"),
)
kb_menu.add(InlineKeyboardButton("Поддержка", url=SUPPORT_LINK))

kb_catalog = InlineKeyboardMarkup(row_width=1)
kb_catalog.add(InlineKeyboardButton("PUBG MOBILE", callback_data="pubg"))
kb_catalog.add(InlineKeyboardButton("OXIDE MOBILE", callback_data="oxide"))
kb_catalog.add(InlineKeyboardButton("Назад", callback_data="back_menu"))

kb_pubg = InlineKeyboardMarkup(row_width=1)
kb_pubg.add(InlineKeyboardButton("Android", callback_data="pubg_android"))
kb_pubg.add(InlineKeyboardButton("Назад", callback_data="catalog"))

kb_pubg_android = InlineKeyboardMarkup(row_width=2)
kb_pubg_android.add(
    InlineKeyboardButton("ZOLO", callback_data="cheat:zolo"),
    InlineKeyboardButton("WATT MOD", callback_data="cheat:watt"),
    InlineKeyboardButton("MAXIMUS", callback_data="cheat:maximus"),
    InlineKeyboardButton("INFERNO PREMIUM", callback_data="cheat:inferno"),
    InlineKeyboardButton("NASA", callback_data="cheat:nasa"),
    InlineKeyboardButton("JARVIS MOD", callback_data="cheat:jarvis"),
    InlineKeyboardButton("DREAM MOD", callback_data="cheat:dream"),
    InlineKeyboardButton("ALTRON", callback_data="cheat:altron"),
    InlineKeyboardButton("DEXO", callback_data="cheat:dexo"),
    InlineKeyboardButton("ZMOD", callback_data="cheat:zmod"),
)
kb_pubg_android.add(InlineKeyboardButton("Назад", callback_data="pubg"))

kb_oxide = InlineKeyboardMarkup(row_width=2)
kb_oxide.add(
    InlineKeyboardButton("Android", callback_data="oxide_android"),
    InlineKeyboardButton("iOS", callback_data="oxide_ios"),
)
kb_oxide.add(InlineKeyboardButton("Назад", callback_data="catalog"))

kb_oxide_android = InlineKeyboardMarkup(row_width=1)
kb_oxide_android.add(
    InlineKeyboardButton("MAGIC VIP", callback_data="cheat:magic_vip"),
    InlineKeyboardButton("MAGIC LITE", callback_data="cheat:magic_lite"),
)
kb_oxide_android.add(InlineKeyboardButton("Назад", callback_data="oxide"))

kb_oxide_ios = InlineKeyboardMarkup(row_width=1)
kb_oxide_ios.add(
    InlineKeyboardButton("ULTIMA", callback_data="cheat:ultima"),
    InlineKeyboardButton("CERTIFICATE", callback_data="cheat:certificate_oxide"),
)
kb_oxide_ios.add(InlineKeyboardButton("Назад", callback_data="oxide"))
kb_zolo = InlineKeyboardMarkup(row_width=1)
kb_zolo.add(
    InlineKeyboardButton("ZOLO 1 день | 150Р", callback_data="buy_t:ZOLO 1 день:150:zolo"),
    InlineKeyboardButton("ZOLO 3 дня | 200Р", callback_data="buy_t:ZOLO 3 дня:200:zolo"),
    InlineKeyboardButton("ZOLO 7 дней | 300Р", callback_data="buy_t:ZOLO 7 дней:300:zolo"),
    InlineKeyboardButton("ZOLO 14 дней | 500Р", callback_data="buy_t:ZOLO 14 дней:500:zolo"),
    InlineKeyboardButton("ZOLO 30 дней | 750Р", callback_data="buy_t:ZOLO 30 дней:750:zolo"),
    InlineKeyboardButton("ZOLO 60 дней | 950Р", callback_data="buy_t:ZOLO 60 дней:950:zolo"),
)
kb_zolo.add(InlineKeyboardButton("Назад", callback_data="pubg_android"))

kb_watt = InlineKeyboardMarkup(row_width=1)
kb_watt.add(
    InlineKeyboardButton("WATT MOD 1 день | 100Р", callback_data="buy_t:WATT MOD 1 день:100:watt"),
    InlineKeyboardButton("WATT MOD 3 дня | 200Р", callback_data="buy_t:WATT MOD 3 дня:200:watt"),
    InlineKeyboardButton("WATT MOD 7 дней | 350Р", callback_data="buy_t:WATT MOD 7 дней:350:watt"),
    InlineKeyboardButton("WATT MOD 14 дней | 550Р", callback_data="buy_t:WATT MOD 14 дней:550:watt"),
)
kb_watt.add(InlineKeyboardButton("Назад", callback_data="pubg_android"))

kb_maximus = InlineKeyboardMarkup(row_width=1)
kb_maximus.add(
    InlineKeyboardButton("MAXIMUS 1 день | 200Р", callback_data="buy_t:MAXIMUS 1 день:200:maximus"),
    InlineKeyboardButton("MAXIMUS 3 дня | 300Р", callback_data="buy_t:MAXIMUS 3 дня:300:maximus"),
    InlineKeyboardButton("MAXIMUS 7 дней | 550Р", callback_data="buy_t:MAXIMUS 7 дней:550:maximus"),
    InlineKeyboardButton("MAXIMUS 14 дней | 750Р", callback_data="buy_t:MAXIMUS 14 дней:750:maximus"),
    InlineKeyboardButton("MAXIMUS 30 дней | 1050Р", callback_data="buy_t:MAXIMUS 30 дней:1050:maximus"),
    InlineKeyboardButton("MAXIMUS 60 дней | 1650Р", callback_data="buy_t:MAXIMUS 60 дней:1650:maximus"),
)
kb_maximus.add(InlineKeyboardButton("Назад", callback_data="pubg_android"))
kb_inferno = InlineKeyboardMarkup(row_width=1)
kb_inferno.add(
    InlineKeyboardButton("INFERNO 1 день | 220Р", callback_data="buy_t:INFERNO 1 день:220:inferno"),
    InlineKeyboardButton("INFERNO 3 дня | 300Р", callback_data="buy_t:INFERNO 3 дня:300:inferno"),
    InlineKeyboardButton("INFERNO 7 дней | 450Р", callback_data="buy_t:INFERNO 7 дней:450:inferno"),
    InlineKeyboardButton("INFERNO 30 дней | 750Р", callback_data="buy_t:INFERNO 30 дней:750:inferno"),
    InlineKeyboardButton("INFERNO 60 дней | 1650Р", callback_data="buy_t:INFERNO 60 дней:1650:inferno"),
)
kb_inferno.add(InlineKeyboardButton("Назад", callback_data="pubg_android"))

kb_nasa = InlineKeyboardMarkup(row_width=1)
kb_nasa.add(
    InlineKeyboardButton("NASA 1 день | 200Р", callback_data="buy_t:NASA 1 день:200:nasa"),
    InlineKeyboardButton("NASA 3 дня | 250Р", callback_data="buy_t:NASA 3 дня:250:nasa"),
    InlineKeyboardButton("NASA 7 дней | 550Р", callback_data="buy_t:NASA 7 дней:550:nasa"),
    InlineKeyboardButton("NASA 14 дней | 750Р", callback_data="buy_t:NASA 14 дней:750:nasa"),
    InlineKeyboardButton("NASA 30 дней | 1550Р", callback_data="buy_t:NASA 30 дней:1550:nasa"),
)
kb_nasa.add(InlineKeyboardButton("Назад", callback_data="pubg_android"))

kb_jarvis = InlineKeyboardMarkup(row_width=1)
kb_jarvis.add(
    InlineKeyboardButton("JARVIS MOD 1 день | 170Р", callback_data="buy_t:JARVIS MOD 1 день:170:jarvis"),
    InlineKeyboardButton("JARVIS MOD 3 дня | 250Р", callback_data="buy_t:JARVIS MOD 3 дня:250:jarvis"),
    InlineKeyboardButton("JARVIS MOD 7 дней | 300Р", callback_data="buy_t:JARVIS MOD 7 дней:300:jarvis"),
    InlineKeyboardButton("JARVIS MOD 14 дней | 550Р", callback_data="buy_t:JARVIS MOD 14 дней:550:jarvis"),
    InlineKeyboardButton("JARVIS MOD 30 дней | 850Р", callback_data="buy_t:JARVIS MOD 30 дней:850:jarvis"),
    InlineKeyboardButton("JARVIS MOD 60 дней | 1150Р", callback_data="buy_t:JARVIS MOD 60 дней:1150:jarvis"),
)
kb_jarvis.add(InlineKeyboardButton("Назад", callback_data="pubg_android"))
kb_dream = InlineKeyboardMarkup(row_width=1)
kb_dream.add(
    InlineKeyboardButton("DREAM MOD 1 день | 200Р", callback_data="buy_t:DREAM MOD 1 день:200:dream"),
    InlineKeyboardButton("DREAM MOD 3 дня | 300Р", callback_data="buy_t:DREAM MOD 3 дня:300:dream"),
    InlineKeyboardButton("DREAM MOD 7 дней | 500Р", callback_data="buy_t:DREAM MOD 7 дней:500:dream"),
    InlineKeyboardButton("DREAM MOD 14 дней | 600Р", callback_data="buy_t:DREAM MOD 14 дней:600:dream"),
    InlineKeyboardButton("DREAM MOD 30 дней | 750Р", callback_data="buy_t:DREAM MOD 30 дней:750:dream"),
    InlineKeyboardButton("DREAM MOD 60 дней | 1050Р", callback_data="buy_t:DREAM MOD 60 дней:1050:dream"),
)
kb_dream.add(InlineKeyboardButton("Назад", callback_data="pubg_android"))

kb_altron = InlineKeyboardMarkup(row_width=1)
kb_altron.add(
    InlineKeyboardButton("ALTRON 1 день | 170Р", callback_data="buy_t:ALTRON 1 день:170:altron"),
    InlineKeyboardButton("ALTRON 3 дня | 280Р", callback_data="buy_t:ALTRON 3 дня:280:altron"),
    InlineKeyboardButton("ALTRON 7 дней | 450Р", callback_data="buy_t:ALTRON 7 дней:450:altron"),
    InlineKeyboardButton("ALTRON 14 дней | 600Р", callback_data="buy_t:ALTRON 14 дней:600:altron"),
    InlineKeyboardButton("ALTRON 30 дней | 750Р", callback_data="buy_t:ALTRON 30 дней:750:altron"),
    InlineKeyboardButton("ALTRON 60 дней | 1050Р", callback_data="buy_t:ALTRON 60 дней:1050:altron"),
)
kb_altron.add(InlineKeyboardButton("Назад", callback_data="pubg_android"))

kb_dexo = InlineKeyboardMarkup(row_width=1)
kb_dexo.add(
    InlineKeyboardButton("DEXO 1 день | 170Р", callback_data="buy_t:DEXO 1 день:170:dexo"),
    InlineKeyboardButton("DEXO 3 дня | 300Р", callback_data="buy_t:DEXO 3 дня:300:dexo"),
    InlineKeyboardButton("DEXO 7 дней | 450Р", callback_data="buy_t:DEXO 7 дней:450:dexo"),
    InlineKeyboardButton("DEXO 14 дней | 650Р", callback_data="buy_t:DEXO 14 дней:650:dexo"),
    InlineKeyboardButton("DEXO 30 дней | 800Р", callback_data="buy_t:DEXO 30 дней:800:dexo"),
    InlineKeyboardButton("DEXO 60 дней | 1050Р", callback_data="buy_t:DEXO 60 дней:1050:dexo"),
)
kb_dexo.add(InlineKeyboardButton("Назад", callback_data="pubg_android"))

kb_zmod = InlineKeyboardMarkup(row_width=1)
kb_zmod.add(
    InlineKeyboardButton("ZMOD 1 день | 150Р", callback_data="buy_t:ZMOD 1 день:150:zmod"),
    InlineKeyboardButton("ZMOD 3 дня | 300Р", callback_data="buy_t:ZMOD 3 дня:300:zmod"),
    InlineKeyboardButton("ZMOD 7 дней | 500Р", callback_data="buy_t:ZMOD 7 дней:500:zmod"),
    InlineKeyboardButton("ZMOD 14 дней | 610Р", callback_data="buy_t:ZMOD 14 дней:610:zmod"),
    InlineKeyboardButton("ZMOD 30 дней | 750Р", callback_data="buy_t:ZMOD 30 дней:750:zmod"),
    InlineKeyboardButton("ZMOD 60 дней | 1050Р", callback_data="buy_t:ZMOD 60 дней:1050:zmod"),
)
kb_zmod.add(InlineKeyboardButton("Назад", callback_data="pubg_android"))
kb_magic_vip = InlineKeyboardMarkup(row_width=1)
kb_magic_vip.add(
    InlineKeyboardButton("MAGIC VIP 1 день | 150Р", callback_data="buy_t:MAGIC VIP 1 день:150:magic_vip"),
    InlineKeyboardButton("MAGIC VIP 7 дней | 1550Р", callback_data="buy_t:MAGIC VIP 7 дней:1550:magic_vip"),
    InlineKeyboardButton("MAGIC VIP 14 дней | 2550Р", callback_data="buy_t:MAGIC VIP 14 дней:2550:magic_vip"),
)
kb_magic_vip.add(InlineKeyboardButton("Назад", callback_data="oxide_android"))

kb_magic_lite = InlineKeyboardMarkup(row_width=1)
kb_magic_lite.add(
    InlineKeyboardButton("MAGIC LITE 1 день | 250Р", callback_data="buy_t:MAGIC LITE 1 день:250:magic_lite"),
    InlineKeyboardButton("MAGIC LITE 7 дней | 1150Р", callback_data="buy_t:MAGIC LITE 7 дней:1150:magic_lite"),
    InlineKeyboardButton("MAGIC LITE 14 дней | 1650Р", callback_data="buy_t:MAGIC LITE 14 дней:1650:magic_lite"),
)
kb_magic_lite.add(InlineKeyboardButton("Назад", callback_data="oxide_android"))

kb_ultima = InlineKeyboardMarkup(row_width=1)
kb_ultima.add(
    InlineKeyboardButton("ULTIMA 1 день | 300Р", callback_data="buy_t:ULTIMA 1 день:300:ultima"),
    InlineKeyboardButton("ULTIMA 7 дней | 1050Р", callback_data="buy_t:ULTIMA 7 дней:1050:ultima"),
    InlineKeyboardButton("ULTIMA 30 дней | 1650Р", callback_data="buy_t:ULTIMA 30 дней:1650:ultima"),
)
kb_ultima.add(InlineKeyboardButton("Назад", callback_data="oxide_ios"))

kb_certificate_oxide = InlineKeyboardMarkup(row_width=1)
kb_certificate_oxide.add(
    InlineKeyboardButton("G BOX M1 | 550Р", callback_data="buy_t:G BOX M1 OXIDE:550:cert_ox"),
    InlineKeyboardButton("G BOX M3 | 1050Р", callback_data="buy_t:G BOX M3 OXIDE:1050:cert_ox"),
    InlineKeyboardButton("G BOX M6 | 1550Р", callback_data="buy_t:G BOX M6 OXIDE:1550:cert_ox"),
    InlineKeyboardButton("G BOX M10 | 2050Р", callback_data="buy_t:G BOX M10 OXIDE:2050:cert_ox"),
)
kb_certificate_oxide.add(InlineKeyboardButton("Назад", callback_data="oxide_ios"))
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("RATCHEATSHOP\n\nВыберите раздел:", reply_markup=kb_menu)

@dp.callback_query_handler(lambda c: c.data == "back_menu")
async def back_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("RATCHEATSHOP\n\nВыберите раздел:", reply_markup=kb_menu)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "catalog")
async def catalog(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите категорию:", reply_markup=kb_catalog)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "reviews")
async def reviews(callback: types.CallbackQuery):
    await callback.message.answer("Отзывы и файлы: " + CHANNEL_LINK)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "pubg")
async def pubg(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите платформу:", reply_markup=kb_pubg)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "pubg_android")
async def pubg_android(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите продукт:", reply_markup=kb_pubg_android)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "oxide")
async def oxide(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите платформу:", reply_markup=kb_oxide)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "oxide_android")
async def oxide_android(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите продукт:", reply_markup=kb_oxide_android)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "oxide_ios")
async def oxide_ios(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите продукт:", reply_markup=kb_oxide_ios)
    await callback.answer()
  CITATA = (
    "Наводка (150 метро) - данная функция помогает навестись на голову или тело противника 🔮\n\n"
    "👄 Подсветка людей - функция с помощью которой вы сможете видеть своих противников через стены (пример в видео обзоре)\n\n"
    "🎁 СБОРКА ОБЛАДАЕТ СИЛЬНЕЙШИМ УРОВНЕМ БЕЗОПАСНОСТИ 💀\n\n"
    "🐾 Совместим с устройствами Android от 9 до 16, Для устройств 32/64 BIT, Поддерживаемые входы: Twitter, Facebook, гостевой, номер и вход по email, Рут права не требуются.\n\n"
    "🐾 Работает в МЕТРО, Classic и остальных режимах для версий Global, Korea, VNG, Taiwan"
)

@dp.callback_query_handler(lambda c: c.data == "cheat:zolo")
async def zolo(callback: types.CallbackQuery):
    text = "ZOLO\n\n" + CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_zolo)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "cheat:watt")
async def watt(callback: types.CallbackQuery):
    text = "WATT MOD\n\n" + CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_watt)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "cheat:maximus")
async def maximus(callback: types.CallbackQuery):
    text = "MAXIMUS\n\n" + CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_maximus)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "cheat:inferno")
async def inferno(callback: types.CallbackQuery):
    text = "INFERNO PREMIUM\n\n" + CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_inferno)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "cheat:nasa")
async def nasa(callback: types.CallbackQuery):
    text = "NASA\n\n" + CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_nasa)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "cheat:jarvis")
async def jarvis(callback: types.CallbackQuery):
    text = "JARVIS MOD\n\n" + CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_jarvis)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "cheat:dream")
async def dream(callback: types.CallbackQuery):
    text = "DREAM MOD\n\n" + CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_dream)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "cheat:altron")
async def altron(callback: types.CallbackQuery):
    text = "ALTRON\n\n" + CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_altron)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "cheat:dexo")
async def dexo(callback: types.CallbackQuery):
    text = "DEXO\n\n" + CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_dexo)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "cheat:zmod")
async def zmod(callback: types.CallbackQuery):
    text = "ZMOD\n\n" + CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_zmod)
    await callback.answer()
  MAGIC_CITATA = (
    "MAGIC - приватный чит для OXIDE с информативными визуалами, гибкой настройкой и стабильной работой.\n\n"
    "Включает продвинутый ESP с отображением игроков, лута, ресурсов, построек, транспорта.\n\n"
    "Aimbot поддерживает настройку FOV, плавности, дистанции и проверки видимости.\n\n"
    "Совместим с Android от 9 до 16, 32/64 BIT, Рут права не требуются.\n"
    "Работает во всех режимах"
)

ULTIMA_CITATA = (
    "ULTIMA - приватный чит для OXIDE с информативными визуалами, гибкой настройкой и стабильной работой.\n\n"
    "Включает продвинутый ESP с отображением игроков, лута, ресурсов, построек, транспорта.\n\n"
    "Aimbot поддерживает настройку FOV, плавности, дистанции и проверки видимости.\n\n"
    "Данный чит на IOS, зарекомендовал себя с лучшей стороны, регулярные обновления.\n"
    "Работает во всех режимах"
)

@dp.callback_query_handler(lambda c: c.data == "cheat:magic_vip")
async def magic_vip(callback: types.CallbackQuery):
    text = "MAGIC VIP\n\n" + MAGIC_CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_magic_vip)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "cheat:magic_lite")
async def magic_lite(callback: types.CallbackQuery):
    text = "MAGIC LITE\n\n" + MAGIC_CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_magic_lite)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "cheat:ultima")
async def ultima(callback: types.CallbackQuery):
    text = "ULTIMA\n\n" + ULTIMA_CITATA + "\n\n🔔 Статус софта: Безопасен"
    await callback.message.edit_text(text, reply_markup=kb_ultima)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "cheat:certificate_oxide")
async def certificate_oxide(callback: types.CallbackQuery):
    text = (
        "G BOX iOS - Сертификат\n\n"
        "G-BOX - мощный инструмент для подписи и установки IPA-файлов на iOS!\n\n"
        "Если Apple не отзывает - работает до года\n\n"
        "Тарифы:\n"
        "M1 - 500Р\nM3 - 1000Р\nM6 - 1500Р\nM10 - 2000Р\n\n"
        "🔔 Статус софта: Безопасен"
    )
    await callback.message.edit_text(text, reply_markup=kb_certificate_oxide)
    await callback.answer()

def kb_pay():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("@RATCHEATSHOP1", url="https://t.me/RATCHEATSHOP1"))
    kb.add(InlineKeyboardButton("@cdxzo", url="https://t.me/cdxzo"))
    kb.add(InlineKeyboardButton("Назад", callback_data="catalog"))
    return kb

def kb_qty(back_to: str, product_name: str = "", price: str = ""):
    kb = InlineKeyboardMarkup(row_width=5)
    kb.add(*[
        InlineKeyboardButton(str(i), callback_data="buy_fin:" + product_name + ":" + price + ":" + str(i))
        for i in range(1, 11)
    ])
    kb.add(InlineKeyboardButton("Назад", callback_data=back_to))
    return kb

@dp.callback_query_handler(lambda c: c.data.startswith("buy_t:"))
async def buy_tariff(callback: types.CallbackQuery):
    parts = callback.data.split(":")
    product_name = parts[1]
    price = parts[2]
    back = parts[3]
    text = (
        "Товар: " + product_name + "\n"
        "Цена: " + price + "Р\n\n"
        "Выберите количество товара, которое хотите купить:"
    )
    await callback.message.edit_text(text, reply_markup=kb_qty("cheat:" + back, product_name, price))
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data.startswith("buy_fin:"))
async def buy_final(callback: types.CallbackQuery):
    parts = callback.data.split(":")
    product_name = parts[1]
    price = parts[2]
    qty = parts[3]
    total = int(price) * int(qty)
    text = (
        "Ваш заказ:\n"
        + product_name + "\n"
        "Количество: " + qty + "\n"
        "Сумма: " + str(total) + "Р\n\n"
        "Для оплаты свяжитесь с продавцом:\n"
        "@RATCHEATSHOP1\n"
        "@cdxzo"
    )
    await callback.message.edit_text(text, reply_markup=kb_pay())
    await callback.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
