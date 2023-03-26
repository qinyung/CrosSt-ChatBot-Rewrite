import asyncio
import websockets
import json

data = json.dumps({
        'cmd': 'join',
        'nick': 'botname',
        'password': 'password',
        "clientName": '[识字街](about:blank)',
        # "clientKey": 'Z1ozsN2ZExhhUHt',
        'channel': '公共聊天室',
    })

async def hello():
    async with websockets.connect("wss://ws.crosst.chat:35197/") as websocket:
        await websocket.send(data)
        await websocket.recv()

asyncio.run(hello())
