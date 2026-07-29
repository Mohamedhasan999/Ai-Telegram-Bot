import os
from dotenv import load_dotenv
from google import genai
from ISABOT.DEPARTMENTS import reg_dep

from telegram import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update
)
from telegram.ext import ContextTypes


# =====================
# GEMINI
# =====================
load_dotenv("settings.env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("deepseek_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("Missing API key")

client = genai.Client(api_key=GEMINI_API_KEY)


# =====================
# QUESTIONS
# =====================
QUESTIONS = [
    "🖥️ كيف تقيّم خبرتك التقنية؟",
    "🤖 لماذا تريد تعلم التكنولوجيا؟"
]


# =====================
# OPTIONS
# =====================
OPTIONS = {
    0: [
        "🟢 مبتدئ",
        "🟡 متوسط",
        "🔵 محترف"
    ],

    1: [
        "💸 العمل الحر",
        "🏢 وظيفة",
        "📈 تطوير عملي",
        "🎬 صناعة محتوى",
        "🚀 مشروع خاص"
    ]
}


# =====================
# USER STATE
# =====================
user_state = {}


# =====================
# START FLOW
# =====================
async def start_flow(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    if not query:
        return

    await query.answer()

    user_id = query.from_user.id

    user_state[user_id] = {
        "step": 0,
        "answers": []
    }

    await send_question(query, 0)


# =====================
# SEND QUESTION
# =====================
async def send_question(source, index: int):

    options = OPTIONS[index]

    keyboard = []
    row = []

    for option in options:
        row.append(KeyboardButton(option))

        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    await source.message.reply_text(
        QUESTIONS[index],
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )


# =====================
# HANDLE FLOW
# =====================
async def handle_flow(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    user_id = update.effective_user.id
    text = update.message.text

    if user_id not in user_state:
        return

    state = user_state[user_id]

    state["answers"].append(text)
    state["step"] += 1

    if state["step"] < len(QUESTIONS):
        await send_question(update, state["step"])
        return

    prompt = f"""
أنت مستشار أكاديمي وتقني محترف.

إجابات المستخدم:
{state['answers']}

اختر له برنامجاً واحداً فقط من البرامج التالية:

- AI Tools
- ChatGPT
- التسويق بالذكاء الاصطناعي
- صناعة المحتوى بالذكاء الاصطناعي
- البرمجة
- التصميم
- العمل الحر الرقمي
- الأتمتة

اشرح سبب اختيارك بشكل مختصر وواضح.

وفي النهاية اكتب:
اضغط على /start للعودة إلى القائمة الرئيسية.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        result = getattr(response, "text", None) or str(response)
       
      
        keyboard = [[InlineKeyboardButton("📝 اضغط هنا للتسجيل المباشر", callback_data="register")],
                    [InlineKeyboardButton("🏠 العودة للقائمة الرئيسية", callback_data="start")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            f"🎯 التوصية المناسبة لك:\n\n{result}",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

    except Exception as error:
        await update.message.reply_text(
            f"حدث خطأ أثناء إنشاء التوصية:\n{error}"
        )

    finally:
        user_state.pop(user_id, None)
        await reg_dep.handle_message(update, context)