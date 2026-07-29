from telegram.ext import ContextTypes
from telegram import Update

async def faq4_Department(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query

    if not query:
        return

    await query.answer()

    if query.data == "faq4":
        await query.message.reply_text(
            """
            نعم، جميع الشهادات التي نقدمها تحتوي على رقم تحقق فريد يمكن التحقق منه عبر الإنترنت. يمكنك استخدام هذا الرقم للتحقق من صحة الشهادة والتأكد من أنها صادرة عن مؤسستنا.
            """
            )