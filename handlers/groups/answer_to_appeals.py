from aiogram import types
from aiogram.types import Message
from loader import dp, bot, db
import re
from datetime import datetime
import pytz


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def reply_to_appeal(msg: Message):
    # faqat guruhda yozilgan xabarlar
    if msg.chat.type not in ['group', 'supergroup']:
        return

    # reply bo‘lishi va bot yuborgan murojaatga javob bo‘lishi kerak
    if not msg.reply_to_message or not msg.reply_to_message.from_user.is_bot:
        return

    # Foydalanuvchi ID sini ajratib olish
    match = re.search(r'ID:\s*<code>(\d+)</code>', msg.reply_to_message.html_text or "")
    if not match:
        return

    user_id = int(match.group(1))

    # Murojaat matnini ajratib olish
    appeal_match = re.search(r"📩 <b>Yangi murojaat!</b>\n\n<i>(.*?)</i>", msg.reply_to_message.html_text or "",
                             re.DOTALL)
    appeal_text = appeal_match.group(1) if appeal_match else "Matn topilmadi"

    # Foydalanuvchiga yuboriladigan javob
    await bot.send_message(
        chat_id=user_id,
        text=(
            f"📬 Sizning murojaatingizga javob keldi!\n\n"
            f"<b>📝 Sizning murojaatingiz:</b>\n<i>{appeal_text}</i>\n\n"
            f"<b>💬 Javob:</b>\n{msg.text}"
        ),
        parse_mode="HTML"
    )

    # Javobni DB ga saqlash (answers jadvali)
    tz = pytz.timezone("Asia/Tashkent")
    tashkent_time = datetime.now(tz)

    # Murojaat ID sini ajratib olish
    appeal_id_match = re.search(r"📝 Murojaat ID:\s*<code>(\d+)</code>", msg.reply_to_message.html_text or "")
    if appeal_id_match:
        appeal_id = int(appeal_id_match.group(1))
        await db.add_answer(
            appeal_id=appeal_id,
            answer_text=msg.text,
            created_at=tashkent_time.replace(tzinfo=None)
        )

    # Adminga tasdiq
    await msg.reply("Javob murojaatchiga yuborildi✅")
