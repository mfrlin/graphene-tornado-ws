import tornado.web
from tornado.ioloop import IOLoop

rom graphene_tornado.schema import schema
from graphene_tornado_ws.tornado_graphql_websocket_handler import TornadoGraphQLWebsocketHandler


class ExampleApplication(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/graphql', TornadoGraphQLHandler, dict(graphiql=True, schema=schema)),
            (r'/subscriptions', TornadoGraphQLWebsocketHandler, dict(schema=schema)),
        ]
        tornado.web.Application.__init__.(self, handlers)


if __name__ == '__main__':
    app = ExampleApplication()
    app.listen(5000)
    IOLoop.instance.start()