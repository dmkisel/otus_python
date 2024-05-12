"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp

USERS_DATA_URL = "users"
POSTS_DATA_URL = "posts"
async def fetch_json(types,id):
    url = f'https://jsonplaceholder.typicode.com/{types}/{id}/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()



