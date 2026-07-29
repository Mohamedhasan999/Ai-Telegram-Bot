from ISABOT.FLOW import english_flow, learn_flow , hr_flow , bs_flow ,ai_flow

async def route_flow(update, context):
    user_id = update.effective_user.id

    if user_id in english_flow.user_state:
        return await english_flow.handle_flow(update, context)

    if user_id in learn_flow.user_state:
        return await learn_flow.handle_flow(update, context)

    if user_id in hr_flow.user_state:
        return await hr_flow.handle_flow(update, context)
    
    if user_id in bs_flow.user_state:
        return await bs_flow.handle_flow(update, context)
    
    if user_id in ai_flow.user_state:
        return await ai_flow.handle_flow(update, context)