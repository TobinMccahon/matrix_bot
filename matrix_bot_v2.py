import asyncio
from nio import AsyncClient, LoginResponse, RoomMessageText

async def message_callback(room, event):
    if isinstance(event, RoomMessageText):
        print('Received message:', event.body)
        await room.send('m.room.message', {'msgtype': 'm.text', 'body': 'Thank you for your message!'})

async def main():
    client = AsyncClient('https://matrix.org', 'your_username')  # Replace with your username
    response = await client.login('your_password')  # Replace with your password
    if isinstance(response, LoginResponse):
        print('Logged in successfully!')
        client.add_event_callback(message_callback, RoomMessageText)
        await client.sync_forever(timeout=30000)  # Sync every 30 seconds
    else:
        print('Failed to log in:', response)

asyncio.run(main())
