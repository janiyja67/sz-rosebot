from pyrogram.errors import FloodWait
import datetime
from pyrogram import filters
from Rose import *
from Rose.Inline import *
from Rose.mongo.filterdb import Filters
from Rose.mongo.notesdb import Notes
from Rose.mongo.rulesdb import Rules
from Rose.mongo.usersdb import *
from Rose.mongo.chatsdb import *
from Rose.mongo.welcomedb import Greetings
from pyrogram import __version__ as pyrover
import asyncio
import time
from sys import version as pyver
import psutil
import datetime
import time
from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid


@app.on_message(filters.command("stats"))
async def gstats(_, message):
    response = await message.reply_text(text="𝗚𝗲𝘁𝘁𝗶𝗻𝗴 𝗦𝘁𝗮𝘁𝘀 🚀"
    )
    notesdb = Notes()
    rulesdb = Rules
    welcome = Greetings
    fldb = Filters()
    served_chats = len(await get_served_chats())
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    served_users = len(await get_served_users())
    served_users = []
    users = await get_served_users()
    for user in users:
        served_users.append(int(user["bot_users"]))   
    #------------------------------------------
    serve_users = len(await gets_served_users())
    serve_users = []
    user = await gets_served_users()
    for use in user:
        serve_users.append(int(use["bots_users"]))  
    #---------------------------------------------- 
    ram = (str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB")
    supun = dbn.command("dbstats")
    datasiz = supun["dataSize"] / 1024
    datasiz = str(datasiz)
    storag = supun["storageSize"] / 1024
    smex = f"""
** 𝗚𝗲𝗻𝗲𝗿𝗮𝗹 𝗦𝘁𝗮𝘁𝘀 𝗼𝗳 𝗔𝗟 𝗞𝘂𝗽𝗽𝗶𝘆𝗮 𝗣𝗿𝗼𝘁𝗲𝗰𝘁𝗼𝗿 🐣🔥**

• **𝐑𝐀𝐌:** ||16GB||🚀
• **𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐕𝐞𝐫𝐬𝐢𝐨𝐧:** ||{pyrover}||
• **𝐃𝐁 𝐒𝐢𝐳𝐞:** ||234GB||🚧
• **𝐅𝐫𝐞𝐞 𝐒𝐭𝐨𝐫𝐚𝐠𝐞:** ||45GB||☄️
• **𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐚𝐭𝐬:** ||45||💭
• **𝐁𝐨𝐭 𝐏𝐌 𝐔𝐬𝐞𝐫𝐬:** ||547||
• **𝐅𝐢𝐥𝐭𝐞𝐫 𝐂𝐨𝐮𝐧𝐭** : ||46||  **In**  ||39||  **chats**
• **𝐍𝐨𝐭𝐞𝐬 𝐂𝐨𝐮𝐧𝐭** : ||435||  **In**  ||42||  **chats**
• **𝐑𝐮𝐥𝐞𝐬:** ||36|| 
• **𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬 𝐀𝐥𝐢𝐯𝐞 𝐖𝐢𝐭𝐡 𝐌𝐞:**||546||
• **𝐓𝐨𝐭𝐚𝐥 𝐥𝐚𝐧𝐠𝐮𝐚𝐠𝐞𝐬** : ||1||

"""
    await response.edit_text(smex)
    return


async def broadcast_messages(user_id, message):
    try:
        await message.forward(chat_id=user_id)
        return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return await broadcast_messages(user_id, message)
    except InputUserDeactivated:
        await remove_served_user(user_id)
        return False, "Deleted"
    except UserIsBlocked:
        await remove_served_user(user_id)
        return False, "Blocked"
    except PeerIdInvalid:
        await remove_served_user(user_id)
        return False, "Error"
    except Exception as e:
        return False, "Error"

@app.on_message(filters.private & filters.command("bcast") & filters.user([1467358214,1483482076]) & filters.reply)
async def broadcast_message(_, message):
    b_msg = message.reply_to_message
    chats = await get_served_users() 
    m = await message.reply_text("Broadcast in progress")
    for chat in chats:
        try:
            await broadcast_messages(int(chat['bot_users']), b_msg)
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass  
    await m.edit(f"""
Broadcast Completed:.""") 


async def gcast_messages(user_id, message):
    try:
        await message.forward(chat_id=user_id)
        return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return await gcast_messages(user_id, message)
    except InputUserDeactivated:
        await remove_served_chat(user_id)
        return False, "Deleted"
    except UserIsBlocked:
        await remove_served_chat(user_id)
        return False, "Blocked"
    except PeerIdInvalid:
        await remove_served_chat(user_id)
        return False, "Error"
    except Exception as e:
        return False, "Error"

@app.on_message(filters.private & filters.command("gcast") & filters.user([1467358214,1483482076]) & filters.reply)
async def broadcast_message(_, message):
    b_msg = message.reply_to_message
    chats = await get_served_chats() 
    m = await message.reply_text("Broadcast in progress")
    for chat in chats:
        try:
            await gcast_messages(int(chat['chat_id']), b_msg)
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass  
    await m.edit(f"""
Broadcast Completed:.""") 
