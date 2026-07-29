from types import SimpleNamespace
# import start
# import ai_flow
# import bussnise_folw
from ISABOT import courses
# import en_flow
# import hr_flow
# import learn_flow
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    keyboard = [
        [InlineKeyboardButton("تقييم اللغة الانكليزية", callback_data="enflow"),
        InlineKeyboardButton("تقييم التربية والتعليم", callback_data="learnflow")],

        [InlineKeyboardButton("تقييم التنمية البشرية \nوالمهارات", callback_data="hrflow"),
        InlineKeyboardButton(" تقييم الإدارة \nوريادة الأعمال", callback_data="bsflow")],

        [InlineKeyboardButton(" التكنولوجيا والذكاء الاصطناعي", callback_data="aiflow"),
        InlineKeyboardButton(" لمعرفة ما نقدمه", callback_data="content")
    ]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query

    try:
            await update.message.reply_text(
        "مرحبا بك في أكاديمية المهارات الدولية ISA 🌍\n بوابتك نحو المهارات، اللغة، التطوير المهني، والتكنولوجيا الحديثة.\n\n"
                                    , reply_markup=reply_markup)
    except AttributeError:
        await query.message.reply_text(
        "مرحبا بك في أكاديمية المهارات الدولية ISA 🌍\n بوابتك نحو المهارات، اللغة، التطوير المهني، والتكنولوجيا الحديثة.\n\n"
                                    , reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()
    data = query.data

    if data == "start":
        await start(update, context)
        return
    elif data == "content":
        await courses.start(update, context)
        return
    
