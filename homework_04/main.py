import asyncio
from models import (Base,
                    User,
                    Post)

from models import (async_session,
                    async_engine,
                    Session)

from jsonplaceholder_requests import (fetch_posts_data,
                                      fetch_users_data)

async def create_users(session: Session,
                 *user_list: list[dict]
                 ) -> list[User]:
    users = []
    for user in user_list:
        for user_data in user:
            users.append(User(name=user_data['name'],
                              username=user_data['username'],
                              email=user_data['email']))
    session.add_all(users)
    await session.commit()
    return users

async def creare_posts(session: Session,
                 *post_list: list[Post]
                 ) -> list[Post]:
    posts = []
    for post in post_list:
        for post_data in post:
            posts.append(Post(title=post_data['title'],
                              body=post_data['body'],
                              user_id=post_data['userId']))
    session.add_all(posts)
    await session.commit()
    return posts

async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    users_data: list[dict]
    posts_data: list[dict]
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    async with async_session.begin() as conn:
        await create_users(conn, users_data)
    async with async_session.begin() as conn:
        await creare_posts(conn, posts_data)


def main():

    asyncio.run(async_main())
    pass

if __name__ == "__main__":
    main()


