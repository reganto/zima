import argparse
from tornado.ioloop import IOLoop
from anorc import create_app


parser = argparse.ArgumentParser(description="Anorc command line")
parser.add_argument("--host", default="127.0.0.1", type=str, help="Run on the given host.")
parser.add_argument("--port", default=8000, type=int, help="Run on the given port.")
parser.add_argument("--m", default=1, type=int, help="Run multiple instances of app.")
args = parser.parse_args()

if args.m == 1:
    app = create_app()
    app.listen(args.port, args.host)
    print("Server started at %s:%s" % (args.host, args.port))
elif args.m > 1:
    app_list = []
    port = args.port
    for _ in range(args.m):
        app_list.append(create_app())
    for app in app_list:
        app.listen(port, args.host)
        print("Server started at %s:%s" % (args.host, port))
        port += 1
else:
    print("value of 'm' must be 1 or more.")
        
IOLoop.instance().start()

