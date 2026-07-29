from telegram.ext import ContextTypes
from telegram import Update

async def faq3_Department(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query

    if not query:
        return

    await query.answer()

    if query.data == "faq3":
        await query.message.reply_text(
            """
            الشهادات التي نقدمها متاحة بنسختين: نسخة إلكترونية ونسخة ورقية. النسخة الإلكترونية تحتوي على رمز تحقق فريد يمكن التحقق منه عبر الإنترنت، بينما النسخة الورقية تحتوي على نفس المعلومات ولكن في شكل مطبوع. يمكنك اختيار النسخة التي تناسبك عند التسجيل.
            """
            )