from ISABOT.QFAQ import qfaq1,qfaq2,qfaq3,qfaq4,qfaq5,qfaq6,back

async def route_dep(update, context):
    user_id = update.effective_user.id

    if user_id in qfaq1.user_state:
        return await qfaq1.handle_flow(update, context)
    
    if user_id in qfaq2.user_state:
        return await qfaq2.handle_flow(update, context)
    
    if user_id in qfaq3.user_state:
        return await qfaq3.handle_flow(update, context)

    if user_id in qfaq4.user_state:
        return await qfaq4.handle_flow(update, context)

    if user_id in qfaq5.user_state:
        return await qfaq5.handle_flow(update, context)
    
    if user_id in qfaq6.user_state:
        return await qfaq6.handle_flow(update, context)
    if user_id in back.user_state:
        return await back.handle_flow(update, context)
