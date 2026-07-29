from telegram.ext import ContextTypes
from telegram import Update

async def faq1_Department(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query

    if not query:
        return

    await query.answer()

    if query.data == "faq1":
        await query.message.reply_text(
            """
            نعم، جميع الشهادات التي نقدمها معترف بها من قبل المؤسسات التعليمية والشركات في جميع أنحاء العالم. نحن نعمل مع شركاء معتمدين لضمان جودة الشهادات التي نقدمها.
            """
            )