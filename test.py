import aiohttp
import json
import asyncio

async def main():
	async with aiohttp.ClientSession() as session:
		async with session.get('https://www.albion-online-data.com/api/v2/stats/prices/T6_HIDE') as resp:
			print(await resp.json())

asyncio.run(main())
