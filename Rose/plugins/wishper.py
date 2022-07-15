from typing import Optional
from Rose import app
from pyrogram import filters, emoji
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton,
)

lengths = 200
IMG = "https://telegra.ph/file/c1b6243f41419dffba9b5.jpg"


@app.on_inline_query()
async def wishper_ai(_, sz: InlineQuery):
    query = sz.query
    split = query.split(' ', 1)
    if query == '' or len(query) > lengths \
            or (query.startswith('@') and len(split) == 1):
        title = f"Write a whisper message 🐣🌳"
        content = ("**Send whisper messages through inline mode**\n\n"
                   "Usage: `@alkuppiyaprotectorbot [@username|@] text`")
        description = "Usage: @alkuppiyaprotectorbot [@username|@] text"
        button = InlineKeyboardButton(
            "Learn more...",
            url="https://t.me/alkuppiyaprotectorbot?start=learn"
        )
    elif not query.startswith('@'):
        title = f"{emoji.EYE} Whisper once to the first one who open it"
        content = (
            f"{emoji.EYE} The first one who open the whisper can read it"
        )
        description = f"{emoji.SHUSHING_FACE} {query}"
        button = InlineKeyboardButton(
            f"show message 🐻🐣",
            callback_data="show_whisper"
        )
    else:
        # Python 3.8+
        u_target = 'anyone' if (x := split[0]) == '@' else x
        title = f"🔒 A whisper message to {u_target}, Only he/she can open it."
        content = f"🔒 A whisper message to {u_target}, Only he/she can open it."
        description = f"{emoji.SHUSHING_FACE} {split[1]}"
        button = InlineKeyboardButton(
            f"{emoji.LOCKED_WITH_KEY} show message",
            callback_data="show_whisper"
        )
    switch_pm_text = f"{emoji.INFORMATION} Learn how to send whispers"
    switch_pm_parameter = "learn"
    await sz.answer(
        results=[
            InlineQueryResultArticle(
                title=title,
                input_message_content=InputTextMessageContent(content),
                description=description,
                thumb_url=IMG,
                reply_markup=InlineKeyboardMarkup([[button]])
            )
        ],
        switch_pm_text=switch_pm_text,
        switch_pm_parameter=switch_pm_parameter
    )




