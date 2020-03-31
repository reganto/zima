import argparse
from tornado.ioloop import IOLoop
from config import config
from zima import create_app

# Command line options
parser = argparse.ArgumentParser(description="Anorc command line")
parser.add_argument("-p", default=8000, type=int, help="Run on the given port.")
parser.add_argument("-m", default=1, type=int, help="Run multiple instances of app.")
parser.add_argument("-v", default=False, type=bool, help="Verbosity.(default is False)")
args = parser.parse_args()


def manage_cli(m):
    """Manage anorc command line options"""

    if args.m == 1: # Single instance
        app = create_app("default")
        app.listen(args.p, config.get("HOST"))
        if args.v:
            print(f"Server started at {config.get('HOST')}:{args.p}")
    elif args.m > 1: # Multiple instances
        app_list = []
        port = args.p
        for _ in range(args.m):
            app_list.append(create_app("default"))
        for app in app_list:
            app.listen(port, config.get("HOST"))
            if args.v:
                print(f"Server started at {config.get('HOST')}:{port}")
            port += 1
    else:
        print("value of 'm' must be 1 or more.")
        

manage_cli(args.m)
loop = IOLoop.instance()
loop.start()

