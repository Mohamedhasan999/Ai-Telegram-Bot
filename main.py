import os
import logging

import start
from ISABOT import start as st

from ISABOT import courses
from ISABOT import flow_routing
from ISABOT import departments_routing
from ISABOT import qfaq_routing
from ISABOT.FLOW  import english_flow, learn_flow, hr_flow, bs_flow, ai_flow
from ISABOT.DEPARTMENTS  import english_dep, learn_dep, hr_dep, bs_dep, ai_dep, scholar_dep, cert_dep, reg_dep, faq_dep
from ISABOT.QFAQ import qfaq1, qfaq2, qfaq3, qfaq4, qfaq5, qfaq6, back





from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# =====================
# SETTINGS
# =====================
load_dotenv("settings.env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not configured")


# =====================
# LOGGING
# =====================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# =====================
# MAIN
# =====================
def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # =====================
    # COMMANDS
    # =====================
    application.add_handler(CommandHandler("start", start.start))
    application.add_handler(CommandHandler("start", st.start))
    application.add_handler(CallbackQueryHandler(st.start, pattern="^(isa)$"))


    # =====================
    # CALLBACKS FOR ISA
    # =====================

    application.add_handler(
        CallbackQueryHandler(st.start, pattern="^(start)$")
    )

    application.add_handler(
        CallbackQueryHandler(st.start, pattern="^(start)$")
    )
    application.add_handler(
        CallbackQueryHandler(courses.start, pattern="^(content)$")
     )
     
    application.add_handler(
        CallbackQueryHandler(english_flow.start_flow, pattern="^(enflow)$")
    )

    application.add_handler(
        CallbackQueryHandler(learn_flow.start_flow, pattern="^(learnflow)$")
    )
    
    application.add_handler(
        CallbackQueryHandler(hr_flow.start_flow, pattern="^(hrflow)$")
    )

    application.add_handler(
        CallbackQueryHandler(bs_flow.start_flow, pattern="^(bsflow)$")
    )

    application.add_handler(
        CallbackQueryHandler(ai_flow.start_flow, pattern="^(aiflow)$")
    )

    application.add_handler(
        CallbackQueryHandler(english_dep.English_Department, pattern="^(english)$")
    )

    application.add_handler(
        CallbackQueryHandler(learn_dep.learn_Department, pattern="^(learn)$")
    )

    application.add_handler(
        CallbackQueryHandler(hr_dep.hr_Department, pattern="^(hr)$")
    )

    application.add_handler(
        CallbackQueryHandler(bs_dep.bs_Department, pattern="^(bs)$")
    )

    application.add_handler(
        CallbackQueryHandler(ai_dep.ai_Department, pattern="^(ai)$")
    )

    application.add_handler(
        CallbackQueryHandler(scholar_dep.scholar_Department, pattern="^(scholarship)$")
    )

    application.add_handler(
        CallbackQueryHandler(cert_dep.cert_Department, pattern="^(certificate)$")
    )

    application.add_handler(
        CallbackQueryHandler(reg_dep.register_Department, pattern="^(register)$")
    )

    application.add_handler(
        CallbackQueryHandler(faq_dep.faq_Department, pattern="^(faq)$")
    )

    application.add_handler(
        CallbackQueryHandler(qfaq1.faq1_Department, pattern="^(faq1)$")
    )

    application.add_handler(
        CallbackQueryHandler(qfaq2.faq2_Department, pattern="^(faq2)$")
    )

    application.add_handler(
        CallbackQueryHandler(qfaq3.faq3_Department, pattern="^(faq3)$")
    )

    application.add_handler(
        CallbackQueryHandler(qfaq4.faq4_Department, pattern="^(faq4)$")
    )

    application.add_handler(
        CallbackQueryHandler(qfaq5.faq5_Department, pattern="^(faq5)$")
    )

    application.add_handler(
        CallbackQueryHandler(qfaq6.faq6_Department, pattern="^(faq6)$")
    )
    application.add_handler(
        CallbackQueryHandler(back.back_Department, pattern="^(back)$")
    )

    application.add_handler(
        CallbackQueryHandler(st.button)
    )

    # =====================
    # HANDLERS 
    # =====================
    
    async def global_text_router(update: Update, context: ContextTypes.DEFAULT_TYPE):
        
        if context.user_data.get("registering"):
            await reg_dep.handle_message(update, context)
            return

        await flow_routing.route_flow(update, context)
        
        await departments_routing.route_dep(update, context)
        await qfaq_routing.route_dep(update, context)

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, global_text_router))
    
    async def handle_registration_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
       query = update.callback_query
       await query.answer()
    
       if query.data == "register":
          await reg_dep.handle_message(update, context) 
       elif query.data == "start":
          await start.start(update, context)



    print("Bot is running...")
    application.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()