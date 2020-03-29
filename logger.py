from models import Log
import json


class Logger:


    def response(self, flow):
        self.l.response_body = flow.response.get_text()
        self.l.response_headers = json.dumps(dict(flow.response.headers))
        self.l.rtt = flow.response.timestamp_end - flow.request.timestamp_start
        self.l.code = flow.response.status_code
        self.l.save()

    def request(self, flow):
        self.l = Log()
        self.l.request_body = flow.request.get_text()
        self.l.method = flow.request.method
        self.l.url = flow.request.url
        self.l.request_headers = json.dumps(dict(flow.request.headers))
        self.l.save()


addons = [
    Logger()
]
