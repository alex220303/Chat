import asyncio

class ChatServer:
    def __init__(self):
        self.clients = set()

    async def handle_client(self, reader, writer):
        self.clients.add(writer)
        addr = writer.get_extra_info('peername')
        print(f"New connection from {addr}")

        try:
            while True:
                data = await reader.read(100)
                message = data.decode().strip()
                if message:
                    print(f"Received message from {addr}: {message}")
                    await self.broadcast(message)
                else:
                    print(f"Connection from {addr} closed")
                    break
        except Exception as e:
            print(f"Error with client {addr}: {e}")
        finally:
            self.clients.remove(writer)
            writer.close()
            await writer.wait_closed()

    async def broadcast(self, message):
        if self.clients:
            print(f"Broadcasting message: {message}")
            for client in self.clients:
                try:
                    client.write(message.encode())
                    await client.drain()
                except Exception as e:
                    print(f"Error broadcasting message: {e}")

    async def start(self, host, port):
        server = await asyncio.start_server(
            self.handle_client, host, port)
        async with server:
            print(f"Chat server started on {host}:{port}")
            await server.serve_forever()

async def main():
    server = ChatServer()
    await server.start('127.0.0.1', 8888)

if __name__ == "__main__":
    asyncio.run(main())
