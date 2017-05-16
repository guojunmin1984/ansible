#作者：郭俊民

class CallbackModule(object):
    def runner_on_ok(self, host, res):
        print(res)
        if 'stdout' in res.keys():
            print(res[''])
        if 'state' in res.keys():
            print(res['state'])
        if 'invocation' in res.keys():
            print(res['invocation'])
    def runner_on_failed(self, host, res, ignore_errors=False):
        pass
    def runner_on_skipped(self, host, item=None):
        pass
    def runner_on_unreachable(self, host, res):
        pass