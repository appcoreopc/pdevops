

import logging
import asyncio

class Employee:

    def __init__(self):
        print("init")
    
    async def sayHello(self):
        print("calling sayhellomore")
        self.sayHelloMore()

    def sayHelloMore(self):
        print('say hello')


async def main():
    emp = Employee()
    emp.sayHelloMore()
    await emp.sayHello()
    # logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
 

async def solo(msg):
    print("solo", msg)


if __name__ == '__main__':
    asyncio.run(solo('test'))
    #asyncio.run(main())
