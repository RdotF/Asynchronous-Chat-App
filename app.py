from aiohttp import web
import aiohttp_jinja2, jinja2
from handlers import index, websocket_handler
app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

#ROUTES
app.router.add_get('/', index)
app.router.add_get('/ws', websocket_handler)
app.router.add_static('/static/', 'static/', show_index=True)

if __name__ == '__main__':
  web.run_app(app, host='localhost', port=8080)
  print('the web is running!')
