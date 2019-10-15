import asyncio
from os import environ
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


class Component(ApplicationSession):
    """
    An application component calling the different backend procedures.
    """

    async def onJoin(self, details):

        await self.call(u'com.arguments.ping')
        print("Pinged!")

        res = await self.call(u'com.arguments.add2', 2, 3)
        print("Add2: {}".format(res))

        starred = await self.call(u'com.arguments.stars')
        print("Starred 1: {}".format(starred))

        starred = await self.call(u'com.arguments.stars', nick=u'Homer')
        print("Starred 2: {}".format(starred))

        starred = await self.call(u'com.arguments.stars', stars=5)
        print("Starred 3: {}".format(starred))

        starred = await self.call(u'com.arguments.stars', nick=u'Homer', stars=5)
        print("Starred 4: {}".format(starred))

        orders = await self.call(u'com.arguments.orders', u'coffee')
        print("Orders 1: {}".format(orders))

        orders = await self.call(u'com.arguments.orders', u'coffee', limit=10)
        print("Orders 2: {}".format(orders))

        arglengths = await self.call(u'com.arguments.arglen')
        print("Arglen 1: {}".format(arglengths))

        arglengths = await self.call(u'com.arguments.arglen', 1, 2, 3)
        print("Arglen 1: {}".format(arglengths))

        arglengths = await self.call(u'com.arguments.arglen', a=1, b=2, c=3)
        print("Arglen 2: {}".format(arglengths))

        arglengths = await self.call(u'com.arguments.arglen', 1, 2, 3, a=1, b=2, c=3)
        print("Arglen 3: {}".format(arglengths))

        self.leave()

    def onDisconnect(self):
        asyncio.get_event_loop().stop()


if __name__ == '__main__':
    import six
    url = environ.get("AUTOBAHN_DEMO_ROUTER", u"ws://127.0.0.1:8000/ws")
    if six.PY2 and type(url) == six.binary_type:
        url = url.decode('utf8')
    realm = u"crossbardemo"
    runner = ApplicationRunner(url, realm)
    runner.run(Component)