import asyncio


async def handle_client(reader, writer):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        writer.write(data)
        await writer.drain()
    writer.close()


async def main():
    host = ""
    port = 12345

    server = await asyncio.start_server(handle_client, host, port)

    async with server:
        print(f"Listening on {host}:{port}")
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
