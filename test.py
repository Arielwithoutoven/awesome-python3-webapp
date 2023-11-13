async def childG():
    yield 1
    return 1


async def comm():
    return await childG()


x = comm()
print(x.send(None))
