import asyncio
from os import environ
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


class Component(ApplicationSession):
    """
    An application component providing procedures with different kinds
    of arguments.
    """

    async def onJoin(self, details):

        def ping():
            return

        def add2(a, b):
            return a + b

        def stars(nick="somebody", stars=0):
            return u"{} starred {}x".format(nick, stars)

        # noinspection PyUnusedLocal
        def orders(product, limit=5):
            return [u"Product {}".format(i) for i in range(50)][:limit]

        def arglen(*args, **kwargs):
            return [len(args), len(kwargs)]

        await self.register(ping, u'com.arguments.ping')
        await self.register(add2, u'com.arguments.add2')
        await self.register(stars, u'com.arguments.stars')
        await self.register(orders, u'com.arguments.orders')
        await self.register(arglen, u'com.arguments.arglen')
        print("Registered methods; ready for frontend.")


if __name__ == '__main__':
    import six
    url = environ.get("AUTOBAHN_DEMO_ROUTER", u"ws://localhost:8000/ws")
    print(url)
    if six.PY2 and type(url) == six.binary_type:
        url = url.decode('utf8')
    realm = u"crossbardemo"
    runner = ApplicationRunner(url, realm)
    runner.run(Component)