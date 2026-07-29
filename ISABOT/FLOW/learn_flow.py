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
Questions = [
    "🏫 هل تعمل حاليًا في مجال التعليم؟",
    "💡 أي مجال يجذبك أكثر؟",
    "🌎 أين تطمح للعمل؟"
]


# =====================
# OPTIONS
# =====================
Options = {
    0: ["👨‍🏫 نعم", "❌ لا", "🎓 طالب جامعي"],
    1: ["🧒 تعليم الأطفال", "❤️ التربية الخاصة", "📖 التعليم الحديث", "🏢 تأسيس مشروع تعليمي", "🌍 العمل كمعلم دولي"],
    2: ["🏠 داخل البلد", "✈️ خارج البلد", "💻 أونلاين"]
}


# =====================
# USER STATE
# =====================
user_state = {}


# =====================
# START FLOW (FIXED)
# =====================
async def start_flow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
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
    options = Options[index]

    keyboard = []
    row = []

    for opt in options:
        row.append(KeyboardButton(opt))

        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    await source.message.reply_text(
        Questions[index],
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
        await update.message.reply_text("اضغط /start ثم اختر تقييم التربية والتعليم")
        return

    state = user_state[user_id]
    state["answers"].append(text)
    state["step"] += 1

    if state["step"] < len(Questions):
        await send_question(update, state["step"])
        return

    prompt = f"""
أنت مستشار أكاديمي محترف.

المستخدم يريد مجال التربية والتعليم.

إجابات المستخدم:
{state['answers']}

اختر له كورس مناسب:
- دبلوم مونتيسوري
- دبلوم التربية الحديثة
- تدريب إدارة الصف
- برنامج إعداد معلم دولي

واشرح السبب باختصار.
وفي النهاية اكتب:
اضغط على /start للعودة إلى القائمة الرئيسية.

"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
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

    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

    user_state.pop(user_id, None)