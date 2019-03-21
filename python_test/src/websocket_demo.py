import asyncio
import websockets
@asyncio.coroutine
def echo(websocket, path):
    message = websocket.recv()
    print('recv', message)
    server_data = "收到客户端数据:%s,返回服务端数据为%s"%(message," 来自服务端")
    yield from websocket.send(server_data)
start_server = websockets.serve(echo, '127.0.0.1', 9000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
