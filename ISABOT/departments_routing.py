from ISABOT.DEPARTMENTS import english_dep, learn_dep,hr_dep,bs_dep,ai_dep,scholar_dep,cert_dep,reg_dep,faq_dep

async def route_dep(update, context):
    user_id = update.effective_user.id

    if user_id in english_dep.user_state:
        return await english_dep.handle_flow(update, context)

    if user_id in learn_dep.user_state:
        return await learn_dep.handle_flow(update, context)

    if user_id in hr_dep.user_state:
        return await hr_dep.handle_flow(update, context)

    if user_id in bs_dep.user_state:
        return await bs_dep.handle_flow(update, context)

    if user_id in ai_dep.user_state:
        return await ai_dep.handle_flow(update, context)
    
    if user_id in scholar_dep.user_state:
        return await scholar_dep.handle_flow(update, context)
    
    if user_id in cert_dep.user_state:
        return await cert_dep.handle_flow(update, context)
    
    if user_id in reg_dep.user_state:
        return await reg_dep.handle_flow(update, context)
    
    if user_id in faq_dep.user_state:
        return await faq_dep.handle_flow(update, context)
    
