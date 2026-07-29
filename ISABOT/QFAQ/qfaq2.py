from telegram.ext import ContextTypes
from telegram import Update

async def faq2_Department(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query

    if not query:
        return

    await query.answer()

    if query.data == "faq2":
        await query.message.reply_text(
            """
            نعم، يمكن استخدام الشهادات التي نقدمها للعمل في العديد من المجالات. نحن نعمل مع شركاء في الصناعة لضمان أن الشهادات التي نقدمها تلبي احتياجات سوق العمل.
            """
            )