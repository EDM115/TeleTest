import asyncio
import config
from pyrogram import Client, filters, StopPropagation
from ​pyrogram​.​types import ReplyKeyboardMarkup​, ​InlineKeyboardMarkup​, ​InlineKeyboardButton

BOT_TOKEN​ ​=​ ​config​.​BOT_TOKEN 
​APP_ID​ ​=​ ​config​.​APP_ID 
API_HASH​ ​=​ ​config​.​API_HASH

#async def main():
#    async with Client("my_account", api_id, api_hash) as app:
#        await app.send_message("me", "Greetings from **Pyrogram**!")
#asyncio.run(main())

@​bot​.​on_message​(​filters​.​command​([​"start"​])) 
async​ ​def​ ​start​(​client​, ​message​):
	joinButton​ ​=​ ​InlineKeyboardMarkup​([
		[​InlineKeyboardButton​(​"Channel"​, ​url​=​"https://t.me/EDM115bots"​)],
		[​InlineKeyboardButton​(
			"Report Bugs 😊"​, ​url​=​"https://t.me/EDM115"​)]
	])
	welcomed​ ​=​ ​f"Hey <b>​{​message​.​from_user​.​first_name​}​</b>​\n​/help for More info"
	await​ ​message​.​reply_text​(​welcomed​, ​reply_markup​=joinButton)
	raise​ ​StopPropagation

bot = Client(
	"TeleTest"​,
	​bot_token​=​BOT_TOKEN​,
	​api_id​=​APP_ID​,
	​api_hash​=​API_HASH
	).​run​()
