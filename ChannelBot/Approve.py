from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest
from pyrogram.errors import FloodWait, MessageNotModified
from ChannelBot.database.channel_sql import (
    get_auto_approve
)

@client.on_chat_join_request(filters.channel)
async def approve(c: Client, m: ChatJoinRequest):
    auto_approve = await get_auto_approve(channel_id)
    if auto_approve == 'on'
        return
    try:
        if not m.from_user:
            return
        try:
            await c.approve_chat_join_request(m.chat.id, m.from_user.id)
        except FloodWait as e:
            await asyncio.sleep(e.x + 2)
            await c.approve_chat_join_request(m.chat.id, m.from_user.id)
