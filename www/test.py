import orm
from models import User, Blog, Comment
import asyncio
import aiomysql


def test():
    loop = asyncio.get_event_loop()
    c_p = orm.create_pool(user='root', password='123456', db='awesome')
    loop.run_until_complete(c_p)

    u = User(
        name='Test', email='test@example.com', passwd='1234567890', image='about:blank'
    )

    yield from u.save()


for x in test():
    pass
