import asyncio
from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    message = f"Hello, {name}!"
    return web.Response(text=message)

async def init_app():
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_get('/{name}', handle)
    return app

if __name__ == '__main__':
    app = asyncio.run(init_app())
    web.run_app(app)
