from .. import route, BaseHandler


@route("/")
class MainHandler(BaseHandler):
    def get(self):
        self.write({
            "status": "success",
            "method": "GET"
        })

    def post(self):
        self.write({
            "status": "success",
            "method": "POST"
        })

    def put(self):
        self.write({
            "status": "success",
            "method": "PUT"
        })

    def delete(self):
        self.write({
            "status": "success",
            "method": "DELETE"
        })

