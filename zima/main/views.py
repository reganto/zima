from .. import route, BaseHandler


@route("/")
class MainHandler(BaseHandler):
    def get(self):
        self.write({
            "status": "success",
            "method": "GET"
        })

