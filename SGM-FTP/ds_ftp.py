"""
DS: SaveGameManager. Runs on port 2121.

Use guest:guest
"""
try:
    import coloredlogs
    coloredlogs.install(level='DEBUG')
except:
    pass

import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

SAVE_PATH=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Saves')

def run():
    if not os.path.exists(SAVE_PATH):
        os.mkdir(SAVE_PATH)

    authorizer = DummyAuthorizer()
    authorizer.add_user("guest", "guest", SAVE_PATH, perm="elradfmw")
    authorizer.add_anonymous(SAVE_PATH, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("0.0.0.0", 2121), handler)
    server.serve_forever()

if __name__ == '__main__':
    run()
