from telegram.ext import ContextTypes
from telegram import Update
from ISABOT import courses

async def back_Department(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query

    if not query:
        return

    await query.answer()

    if query.data == "back":

        await courses.start(update, context)