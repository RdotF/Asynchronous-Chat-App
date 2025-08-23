import aiohttp_jinja2
from aiohttp import web

active_ws = set()

@aiohttp_jinja2.template('index.html')
async def index(request):
  return {}

async def websocket_handler(request):
  ws = web.WebSocketResponse()
  await ws.prepare(request)
  active_ws.add(ws)
  try:
    async for msg in ws:
      if msg.type == web.WSMsgType.TEXT:
        print(f'Received message: {msg.data}')
        print('active_ws', active_ws)
        for peer in active_ws:
          
          print('Sending the message...')
          await peer.send_str(msg.data)
          print(f'Sent message: {msg.data}')
  finally:
    active_ws.remove(ws)
  return ws
