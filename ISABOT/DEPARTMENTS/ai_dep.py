from ISABOT import courses

from telegram import Update
from telegram.ext import ContextTypes


async def ai_Department(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query

    if not query:
        return

    await query.answer()

    if query.data == "ai":

        await query.message.reply_text(
            "Testing AI Department"
        )

        await courses.start(update, context)