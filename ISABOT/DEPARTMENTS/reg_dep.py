from telegram.ext import ContextTypes
from telegram import Update
from ISABOT import database
import start
db = database.data()

Questions = [
    "يرجى إدخال اسمك الثلاثي:",
    "يرجى إدخال عمرك:",
    "يرجى إدخال البلد الذي تسكن فيه:",
    "يرجى إدخال رقم هاتفك:",
    "يرجى إدخال بريدك الإلكتروني:",
    "يرجى إدخال التخصص الدراسي:",
    "يرجى إدخال سنة التخرج:",
    "يرجى إدخال العمل الحالي:",
]


async def register_Department(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:

    query = update.callback_query

    # التحقق من أن التحديث هو ضغطة زر تفاعلي فعلاً وبأن الرسالة المرتبطة به موجودة
    if not query or not query.message:
        return

    await query.answer()

    if query.data == "register":
        context.user_data["register_answers"] = []
        context.user_data["current_question"] = 0
        context.user_data["registering"] = True

        # إرسال السؤال الأول
        await query.message.reply_text(Questions[0])


async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:

    # 1. التحقق من أن المستخدم في وضع التسجيل حالياً
    if not context.user_data.get("registering"):
        return

    # 2. استخدام effective_message كبديل آمن لـ update.message لضمان عدم حدوث NoneType
    message = update.effective_message
    
    if not message or not message.text:
        # إذا أرسل المستخدم صورة أو ملصق أو أي شيء ليس نصاً، نطلب منه نصاً
        if message:
            await message.reply_text("الرجاء إدخال نص صحيح للإجابة على السؤال.")
        return

    # جلب النص بأمان
    answer = message.text.strip()

    # جلب البيانات المخزنة مؤقتاً
    answers = context.user_data.get("register_answers", [])
    current = context.user_data.get("current_question", 0)

    # حفظ الإجابة
    answers.append(answer)
    context.user_data["register_answers"] = answers

    # الانتقال للسؤال التالي
    current += 1
    context.user_data["current_question"] = current

    # تحقق هل انتهت الأسئلة أم لا
    if current < len(Questions):
        await message.reply_text(Questions[current])
    else:
        # إنهاء وضع التسجيل وحفظ البيانات
        context.user_data["registering"] = False

        # التأكد من أن المصفوفة تحتوي على جميع الإجابات المطلوبة تجنباً لأخطاء الـ Index
        if len(answers) >= 8:
            full_name = answers[0]
            age = answers[1]
            country = answers[2]
            phone = answers[3]
            email = answers[4]
            major = answers[5]
            graduation_year = answers[6]
            job = answers[7]
            
            # حفظ في قاعدة البيانات
            db.add_user(full_name, age, country, phone, email, major, graduation_year, job)
            await message.reply_text("شكراً لك! تم تسجيلك بنجاح.")
            await start.start(update, context)
        else:
            await message.reply_text("حدث خطأ أثناء جمع البيانات، يرجى إعادة المحاولة من البداية.")