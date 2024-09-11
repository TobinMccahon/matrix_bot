from nio import AsyncClient, MatrixRoom

async def main():
    user_id = 'YOUR_USER_ID'  # Replace with your Matrix user ID
    password = 'YOUR_PASSWORD'  # Replace with your Matrix password

    if user_id == 'YOUR_USER_ID' or password == 'YOUR_PASSWORD':
        print('Please replace YOUR_USER_ID and YOUR_PASSWORD with actual credentials.')
        return

    print('Creating client...')
    client = AsyncClient('https://matrix.org', user_id)
    print('Logging in...')
    await client.login(password)
    print('Creating room...')
    room = await client.room_create('Test Room')
    print('Sending message...')
    await client.room_send(
        room.room_id,
        'm.room.message',
        {'msgtype': 'm.text', 'body': 'Hello, Matrix!'}
    )
    print('Message sent!')
    await client.close()

import asyncio
asyncio.run(main())