###################################
####    From  Yukki Music Bot  ####
###################################

from lang import get_string
from Rose.mongo.language import *
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,Message
from Rose.utils.lang import *
from lang import get_command
from Rose.utils.custom_filters import admin_filter
from button import *

LANG = get_command("LANG")

keyboard = InlineKeyboardMarkup(
    [[
            InlineKeyboardButton(
                text="🇱🇷 English", callback_data="languages_en"
            ),
        ], 
        [
            InlineKeyboardButton(
                text="🇱🇰 සිංහල", callback_data="languages_si"
            ), 
            InlineKeyboardButton(
                text="🇮🇳 हिन्दी", callback_data="languages_hi"
            )
        ], 
        [
            InlineKeyboardButton(
                text="🇮🇹 Italiano", callback_data="languages_it"
            ), 
            InlineKeyboardButton(
                text="🇮🇳 తెలుగు", callback_data="languages_ta"
            ), 
        ], 
        [
            InlineKeyboardButton(
                text="🇮🇩 Indonesia", callback_data="languages_id"
            ), 
            InlineKeyboardButton(
                text="🇦🇪 عربي", callback_data="languages_ar"
            ),
        ], 
        [
            InlineKeyboardButton(
                text="🇮🇳 മലയാളം", callback_data="languages_ml"
            ), 
            InlineKeyboardButton(
                text="🇲🇼 Chichewa", callback_data="languages_ny"
            ), 
        ], 
        [
            InlineKeyboardButton(
                text="🇩🇪 German", callback_data="languages_ge"
            ), 
            InlineKeyboardButton(
                text="🇷🇺 Russian", callback_data="languages_ru"
            ), 
        ]]
)


@app.on_message(filters.command(LANG) & admin_filter)
@language
async def langs_command(client, message: Message, _):
    userid = message.from_user.id if message.from_user else None
    chat_type = message.chat.type
    user = message.from_user.mention
    lang = await get_lang(message.chat.id)
    if chat_type == "private":
      await message.reply_text("𝗢𝘂𝗿 𝗕𝗼𝘁 𝗰𝗮𝗻 𝘀𝗽𝗲𝗮𝗸 𝗼𝗻𝗹𝘆 𝗲𝗻𝗴𝗹𝗶𝘀𝗵.𝗜𝗳 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲 𝗽𝗹𝗲𝗮𝘀𝗲 𝗴𝗼 𝗼𝘂𝗿 𝗮𝗯𝗼𝘂𝘁 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗻𝗱 𝗳𝗶𝗻𝗱 𝗼𝘁𝗵𝗲𝗿 𝗴𝗿𝗼𝘂𝗽 𝗺𝗮𝗻𝗮𝗴𝗶𝗻𝗴 𝗯𝗼𝘁 𝗯𝗲𝗰𝗮𝘂𝘀𝗲 𝘁𝗵𝗮𝘁 𝗯𝗼𝘁 𝗶𝘀 𝗼𝗻𝗹𝘆 𝗳𝗼𝗿 𝗔𝗟 𝗞𝗨𝗣𝗣𝗜𝗬𝗔 𝗧𝗘𝗔𝗠.🚂💨".format(lang),
        reply_markup=keyboard,
     )
    elif chat_type in ["group", "supergroup"]:
        lang = await get_lang(message.chat.id)
        group_id = message.chat.id
        st = await app.get_chat_member(group_id, userid)
        if (
                st.status != "administrator"
                and st.status != "creator"
        ):
         return 
        try:   
            await message.reply_text( "𝗢𝘂𝗿 𝗕𝗼𝘁 𝗰𝗮𝗻 𝘀𝗽𝗲𝗮𝗸 𝗼𝗻𝗹𝘆 𝗲𝗻𝗴𝗹𝗶𝘀𝗵.𝗜𝗳 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲 𝗽𝗹𝗲𝗮𝘀𝗲 𝗴𝗼 𝗼𝘂𝗿 𝗮𝗯𝗼𝘂𝘁 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗻𝗱 𝗳𝗶𝗻𝗱 𝗼𝘁𝗵𝗲𝗿 𝗴𝗿𝗼𝘂𝗽 𝗺𝗮𝗻𝗮𝗴𝗶𝗻𝗴 𝗯𝗼𝘁 𝗯𝗲𝗰𝗮𝘂𝘀𝗲 𝘁𝗵𝗮𝘁 𝗯𝗼𝘁 𝗶𝘀 𝗼𝗻𝗹𝘆 𝗳𝗼𝗿 𝗔𝗟 𝗞𝗨𝗣𝗣𝗜𝗬𝗔 𝗧𝗘𝗔𝗠.🚂💨".format(user),
        reply_markup=keyboard,
     )
        except Exception as e:
            return await app.send_message(LOG_GROUP_ID,text= f"{e}")


@app.on_callback_query(filters.regex("languages"))
async def language_markup(_, CallbackQuery):
    langauge = (CallbackQuery.data).split("_")[1]
    user = CallbackQuery.from_user.mention
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer("You're already on same language 🌝")
    await set_lang(CallbackQuery.message.chat.id, langauge)
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer("Successfully changed your language. 🌚👍🏽")
    except:
        return await CallbackQuery.answer(
            "This language is Under Construction 👷")
    await set_lang(CallbackQuery.message.chat.id, langauge)
    return await CallbackQuery.message.delete()

__MODULE__ = f"{Languages}"
__HELP__ = """
Not every group speaks fluent english; some groups would rather have AL Kuppiya Protector respond in their own language.

This is where translations come in; you can change the language of most replies to be in the language of your choice!

**Admin commands:**
- /lang : Set your preferred language.
"""
__helpbtns__ = (
    [
        [
            InlineKeyboardButton(
                text="🇱🇷 English", callback_data="languages_en"
            ),
       ], 
       [
            InlineKeyboardButton(
                text="🇱🇰 සිංහල", callback_data="languages_si"
            ), 
            InlineKeyboardButton(
                text="🇮🇳 हिन्दी", callback_data="languages_hi"
            )
       ], 
       [
            InlineKeyboardButton(
                text="🇮🇹 Italiano", callback_data="languages_it"
            ), 
            InlineKeyboardButton(
                text="🇮🇳 తెలుగు", callback_data="languages_ta"
            )
       ], 
       [
            InlineKeyboardButton(
                text="🇮🇩 Indonesia", callback_data="languages_id"
            ),
            InlineKeyboardButton(
                text="🇦🇪 عربي", callback_data="languages_ar"
            ),
       ], 
       [
            InlineKeyboardButton(
                text="🇮🇳 മലയാളം", callback_data="languages_ml"
            ), 
            InlineKeyboardButton(
                text="🇲🇼 Chichewa", callback_data="languages_ny"
            ), 
       ], 
       [
            InlineKeyboardButton(
                text="🇩🇪 German", callback_data="languages_ge"
            ), 
            InlineKeyboardButton(
                text="🇷🇺 Russian", callback_data="languages_ru"
            ), 
        ], 
    ]
)
