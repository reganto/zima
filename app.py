from tornado.ioloop import IOLoop
from tornado.options import parse_command_line
from anorc import create_app


parse_command_line()
app = create_app()
app.listen(8001)
IOLoop.instance().start()

