from ISABOT import courses

from telegram import Update
from telegram.ext import ContextTypes
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)

async def faq_Department(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query

    if not query:
        return

    await query.answer()

    if query.data == "faq":

        keyboard = [
        [InlineKeyboardButton("هل الشهادات معترف بها؟", callback_data="faq1"),
        InlineKeyboardButton("هل يمكن استخدامها للعمل؟", callback_data="faq2")],

        [InlineKeyboardButton(" هل الشهادات أونلاين أم ورقية؟", callback_data="faq3"),
        InlineKeyboardButton(" هل يوجد رقم تحقق؟", callback_data="faq4")],

        [InlineKeyboardButton(" هل يوجد تدريب عملي؟", callback_data="faq5"),
        InlineKeyboardButton(" هل الشهادات مناسبة للسفر؟", callback_data="faq6")],
        [InlineKeyboardButton("العودة إلى السابق", callback_data="back")]
    ]
        reply_markup = InlineKeyboardMarkup(keyboard) 

        await query.message.reply_text(
            "اختر السؤال الذي تريد الإجابة عليه:", reply_markup=reply_markup
        )

        # await courses.start(update, context)