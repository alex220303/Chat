import asyncio

async def handle_input(reader, writer):
    while True:
        message = input("Enter message: ")
        writer.write(message.encode())
        await writer.drain()

async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    asyncio.create_task(handle_input(reader, writer))
    while True:
        data = await reader.read(100)
        print(data.decode())

if __name__ == "__main__":
    asyncio.run(main())
