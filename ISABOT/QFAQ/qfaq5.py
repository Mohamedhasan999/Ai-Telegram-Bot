from telegram.ext import ContextTypes
from telegram import Update

async def faq5_Department(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query

    if not query:
        return

    await query.answer()

    if query.data == "faq5":
        await query.message.reply_text(
            """
            نعم، نقدم تدريبًا عمليًا في بعض الدورات التي نقدمها. يعتمد توفر التدريب العملي على الدورة المحددة التي تختارها. يمكنك التحقق من تفاصيل الدورة لمعرفة ما إذا كانت تشمل تدريبًا عمليًا أم لا.
            """
            )