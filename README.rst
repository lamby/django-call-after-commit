README
======

 * Add ``django_call_after_commit.middleware.CallAfterCommitMiddleware`` to your
   middleware.

 * Instead of::

    some_method(arg1, arg2)

   use::

    from django_call_after_commit.utils import call_after_commit
    
    call_after_commit(some_method, arg1, arg2)
