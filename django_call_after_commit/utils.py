import sys

from django.http import HttpRequest

def call_after_commit(fn, *args, **kwargs):
    f = sys._getframe()
    request = None

    while f:
        candidate = f.f_locals.get('request')
        if isinstance(candidate, HttpRequest):
            request = candidate
            break
        f = f.f_back

    if request is None:
        # If we can't find the request object, run it now.
        fn(*args, **kwargs)
        return

    if not hasattr(request, '_post_commit_callbacks'):
        request._post_commit_callbacks = []

    request._post_commit_callbacks.append((fn, args, kwargs))
