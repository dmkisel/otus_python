"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/"
async def fetch_users_data(id):
    url = USERS_DATA_URL + str(id)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def fetch_posts_data(id):
    url = POSTS_DATA_URL + str(id)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()

