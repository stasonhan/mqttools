import asyncio
import mqttools

async def subscriber():
    client = mqttools.Client('test.mosquitto.org', 1883, b'mqttools-subscribe')

    await client.start()
    await client.subscribe(b'/test/#', 0)

    while True:
        topic, message = await client.messages.get()

        print(f'Topic:   {topic}')
        print(f'Message: {message}')
        print()

asyncio.run(subscriber())