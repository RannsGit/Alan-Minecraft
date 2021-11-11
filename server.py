#11/8/21 Kyle Tennison

import tornado.web
import tornado.ioloop
import os
from datetime import datetime
import movements

saveFilename = "current.key"

class recv(tornado.web.RequestHandler):

    #Request as "localhost:1234/recv?d=3"

    def get(self):
        d = self.get_argument("d")
        print(f"Receved {d} as {type(d)}")
        with open(saveFilename, 'w') as saveFile:
            saveFile.write(d)

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/recv", recv)
    ])

    speed = 0


    port = 8888
    app.listen(port)
    print(f"Listening on {port}")
    tornado.ioloop.IOLoop.current().start()
