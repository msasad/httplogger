from mitmproxy import ctx
from models import Log
import json


class Logger:

    def response(self, flow):
        self.log.response_body = flow.response.get_text()
        self.log.response_headers = json.dumps(dict(flow.response.headers))
        self.log.rtt = flow.request.timestamp_end - flow.request.timestamp_start
        self.log.code = flow.response.status_code
        ctx.log.info(str(flow.request.method))
        ctx.log.info(str(flow.request.url))
        self.log.save()

    def request(self, flow):
        self.log = Log()
        self.log.request_body = flow.request.get_text()
        self.log.method = flow.request.method
        self.log.url = flow.request.url
        ctx.log.info(flow.request.headers.get('X-Application-Id'))
        del flow.request.headers['X-Application-Id']
        self.log.request_headers = json.dumps(dict(flow.request.headers))
        self.log.save()


addons = [
    Logger()
]
