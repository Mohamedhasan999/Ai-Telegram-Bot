from telegram.ext import ContextTypes
from telegram import Update

async def faq6_Department(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query

    if not query:
        return

    await query.answer()

    if query.data == "faq6":
        await query.message.reply_text(
            """
            نعم، الشهادات التي نقدمها مناسبة للسفر. نحن نضمن أن شهاداتنا معترف بها دوليًا ويمكن استخدامها في مختلف البلدان. يمكنك التحقق من تفاصيل الدورة والشهادة لمعرفة المزيد عن مدى قبولها في الوجهات التي تخطط للسفر إليها.
            """
            )