from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import ContextTypes
from types import SimpleNamespace
from ISABOT import start as st


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("ISA", callback_data="isa")],

        [InlineKeyboardButton("CHL", callback_data="chl")],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    try:
            await update.message.reply_text(
                 "اختر المنصة التي تود الانضمام إليها:" , reply_markup=reply_markup)
    except AttributeError:
        await query.message.reply_text(  "حدث خطأ", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()
    data = query.data

    if data == "isa":
        await st.start(update, context)
        return
