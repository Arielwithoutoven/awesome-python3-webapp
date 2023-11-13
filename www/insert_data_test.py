import orm
from models import User, Blog, Comment
import asyncio


async def test():
    await orm.create_pool(user="Circleplus", password="111111", db="awesome")

    u = User(
        name="Test", email="test@example.com", passwd="1234567890", image="about:blank"
    )

    await u.save()


loop = asyncio.get_event_loop()
r = loop.run_until_complete(test())
print(r)
loop.close()
