class CallAfterCommitMiddleware(object):
    def process_response(self, request, response):
        try:
            callbacks = request._post_commit_callbacks
        except AttributeError:
            callbacks = []

        for fn, args, kwargs in callbacks:
            fn(*args, **kwargs)

        return response
