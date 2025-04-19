import sqlite3, os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message

load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = "data.db"

app = Client("search-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def search_channels(keyword, limit=5):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT name, link FROM channels
        WHERE name LIKE ? OR description LIKE ?
        LIMIT ?
    """, (f"%{keyword}%", f"%{keyword}%", limit))
    results = c.fetchall()
    conn.close()
    return results

@app.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply("欢迎使用中文频道搜索机器人！使用 /search 关键词 来搜索频道。")

@app.on_message(filters.command("search"))
async def search(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("请输入关键词，例如：/search chatgpt")
    keyword = " ".join(message.command[1:])
    results = search_channels(keyword)
    if not results:
        return await message.reply("没有找到匹配的频道 😢")
    text = "\n".join([f"{i+1}. [{name}]({link})" for i, (name, link) in enumerate(results)])
    await message.reply(f"🔍 搜索结果：\n{text}", disable_web_page_preview=True)

app.run()
