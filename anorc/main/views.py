from anorc import route, BaseHandler


@route("/", name="home")
class MainHandler(BaseHandler):
    def get(self):
        self.write({"status": "OK"})


@route("/user/", name="user")
class UserHandler(BaseHandler):
    def get(self):
        self.write({"status": "main.user"})

