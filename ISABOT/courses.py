from ISABOT.FLOW import english_flow
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import ContextTypes
from dotenv import load_dotenv
import os


load_dotenv("settings.env")
support_url = os.getenv("support_url")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    keyboard = [
        [InlineKeyboardButton("اللغة الإنجليزية", callback_data="english"),
        InlineKeyboardButton("التربية والتعليم", callback_data="learn")],

        [InlineKeyboardButton(" التنمية البشرية والمهارات", callback_data="hr"),
        InlineKeyboardButton(" الإدارة وريادة الأعمال", callback_data="bs")],

        [InlineKeyboardButton(" التكنولوجيا والذكاء الاصطناعي", callback_data="ai"),
        InlineKeyboardButton(" البرامج الدولية والمنح", callback_data="scholarship")],

        [InlineKeyboardButton("الشهادات والاعتمادات", callback_data="certificate"),
        InlineKeyboardButton("التحدث مع فريق الدعم", url=support_url)],

        [InlineKeyboardButton(" التسجيل المباشر", callback_data="register"),
         InlineKeyboardButton("الأسئلة المتكررة", callback_data="faq")],
        [InlineKeyboardButton("العودة إلى القائمة الرئيسية", callback_data="start")]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard) 
    query = update.callback_query

    await query.message.reply_text(
        "اختر القسم الذي ترغب في المعرفة عنه:"
                                    , reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()

    data = query.data

    # if data == "start":
    #     await start.start(update, context)
    #     return
    # elif data == "enflow":
    #     await english_flow.start_flow(update, context)
    #     return