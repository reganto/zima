import sys
import argparse
import logging
from tornado.ioloop import IOLoop
from config import config
from zima import create_app

# logging
logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

# Command line options
parser = argparse.ArgumentParser(description="Zima Command Line")
parser.add_argument("-p", default=8000, type=int, help="Run on the given port.(default is 8000)")
parser.add_argument("-m", default=1, type=int, help="Run multiple instances of app.(default is 1)")
parser.add_argument("-l", default="default", type=str, help="Mode level-development,testing,production.(default is development)")
parser.add_argument("-t", default=False, type=bool, help="Run unit tests.(default is false)")
parser.add_argument("-v", default=False, type=bool, help="Verbosity.(default is false)")
args = parser.parse_args()


def run_tests():
    """Run the unit tests"""

    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)


def app_instances():
    """Manage app instances"""

    if args.m == 1: # Single instance
        app = create_app(args.l)
        app.listen(args.p, config.get("HOST"))
        if args.v:
            logger.info(f"Server started at {config[args.l].host}:{args.p}")
    elif args.m > 1: # Multiple instances
        app_list = []
        port = args.p
        for _ in range(args.m):
            app_list.append(create_app(args.l))
        for app in app_list:
            app.listen(port, config.get("HOST"))
            if args.v:
                logger.info(f"Server started at {config[args.l].host}:{port}")
            port += 1
    else:
        logger.warning("value of 'm' must be 1 or more.")
        sys.exit(0)


def manage_cli():
    """Manage command line options"""

    if args.t:
        run_tests()
        sys.exit(0)

    app_instances()
        

manage_cli()
io_loop = IOLoop.current()
io_loop.start()

