import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/"

async def fetch_users_data() -> list[dict]:
    url = USERS_DATA_URL
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def fetch_posts_data() -> list[dict]:
    url = POSTS_DATA_URL
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()