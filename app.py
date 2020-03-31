import argparse
from tornado.ioloop import IOLoop
from config import config
from zima import create_app

# Command line options
parser = argparse.ArgumentParser(description="Zima Command Line")
parser.add_argument("-p", default=8000, type=int, help="Run on the given port.(default is 8000)")
parser.add_argument("-m", default=1, type=int, help="Run multiple instances of app.(default is 1)")
parser.add_argument("-l", default="default", type=str, help="Mode level-development,testing,production.(default is development)")
parser.add_argument("-v", default=False, type=bool, help="Verbosity.(default is False)")
args = parser.parse_args()


def manage_cli(m):
    """Manage ZIMA command line options"""

    if args.m == 1: # Single instance
        app = create_app(args.l)
        app.listen(args.p, config.get("HOST"))
        if args.v:
            print(f"Server started at {config[args.l].host}:{args.p}")
    elif args.m > 1: # Multiple instances
        app_list = []
        port = args.p
        for _ in range(args.m):
            app_list.append(create_app(args.l))
        for app in app_list:
            app.listen(port, config.get("HOST"))
            if args.v:
                print(f"Server started at {config[args.l].host}:{port}")
            port += 1
    else:
        print("value of 'm' must be 1 or more.")
        

manage_cli(args.m)
loop = IOLoop.instance()
loop.start()

