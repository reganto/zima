import argparse
from tornado.ioloop import IOLoop
from anorc import create_app


parser = argparse.ArgumentParser(description="Anorc command line")
parser.add_argument("--host", default="127.0.0.1", type=str, help="Run on the given host.")
parser.add_argument("--port", default=8000, type=int, help="Run on the given port.")
args = parser.parse_args()

app = create_app()
app.listen(args.port, args.host)
print("Server started at %s:%s" % (args.host, args.port))
IOLoop.instance().start()

