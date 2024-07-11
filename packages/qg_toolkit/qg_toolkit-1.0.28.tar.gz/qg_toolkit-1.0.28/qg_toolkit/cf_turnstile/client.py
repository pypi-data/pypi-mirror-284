import flask
from flask import request

from qg_toolkit.cf_turnstile.cf_turnstile import CFTurnstileSolver


class CFTurnstileSolverClient:
    def __init__(self):
        # self.cf_solve = CFTurnstileSolver(site_key, target_url, headless=headless, proxy=proxy)
        self.app = flask.Flask(__name__)
        self.add_routes()

    # def __del__(self):
    #     self.cf_solve.close_browser()

    def start(self, port=5000):
        from gevent import monkey
        monkey.patch_all()
        self.app.run(host='0.0.0.0', port=port)

    def add_routes(self):
        @self.app.route("/")
        def index():
            return flask.redirect("https://pioneer.particle.network/zh-CN/point")

        @self.app.route("/solve", methods=["POST"])
        def solve():
            # 解决逻辑放在这里
            if request.is_json:
                data = request.get_json()
                site_key = data.get('site_key')
                target_url = data.get('target_url')
                headless = data.get('headless')
                print(f"[CF_TOKEN]开始破解: {site_key}, {target_url},{headless}")
                cf_solve = CFTurnstileSolver(site_key, target_url, headless=headless, proxy=None)
                token = cf_solve.solve()
                print(f"[CF_TOKEN]破解成功: {token}")
                cf_solve.close_browser()
                return make_response(token)
            else:
                return make_response("failed")

        def make_response(captcha_key):
            if captcha_key == "failed":
                return flask.jsonify({"status": "error", "token": None})
            return flask.jsonify({"status": "success", "token": captcha_key})


if __name__ == '__main__':
    client = CFTurnstileSolverClient()
    client.start(port=5555)