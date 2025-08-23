import aiohttp_jinja2
from aiohttp import web
import json
active_ws = set()

@aiohttp_jinja2.template('index.html')
async def index(request):
  return {}

async def websocket_handler(request):
  ws = web.WebSocketResponse()
  await ws.prepare(request)
  current_user_id = request.query.get('user_id', 'guest')
  active_ws.add(ws) 
  try:
    async for msg in ws:
      if msg.type == web.WSMsgType.TEXT:
        print(f'Received message: {msg.data}\nType - {type(msg.data)}')
        for peer in active_ws:
          print('Sending the message...')
          message_data = {
                            'userId': current_user_id,  
                            'text': msg.data
                        }
          await peer.send_str(json.dumps(message_data))
          print(f'Sent message: {current_user_id} - {msg.data}')
  finally:
    active_ws.remove(ws)
  return ws
