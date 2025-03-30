import asyncio

HOST = 'localhost'
PORT = 9095

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(HOST, PORT)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Closing the connection')
    writer.close()
    await writer.wait_closed()

if name == 'main':
    message = 'Hello, world!'
    asyncio.run(tcp_echo_client(message))