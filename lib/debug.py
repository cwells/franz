import pdb
from memory_profiler import show_results, LineProfiler

TRACE = False
PROFILE = False
DEBUG = False

def trace(f):
    def _trace(*args, **kw):
        kwstr = ', '.join('%r: %r' % (k, kw[k]) for k in sorted(kw))
        print("calling %s with args %s, {%s}" % (f.__name__, args, kwstr))
        return f(*args, **kw)

    return _trace if TRACE else f

def profile(f):
    def _profile(*args, **kwargs):
            prof = LineProfiler() # backend=backend)
            val = prof(f)(*args, **kwargs)
            show_results(prof) # , stream=stream, precision=precision)
            return val

    return _profile if PROFILE else f

def debug(f):
    '''Decorator that places a break point right before calling the function.'''
    def _debug(*args, **kwargs):
        pdb.set_trace()  # XXX BREAKPOINT
        return f(*args, **kwargs)

    return _debug if DEBUG else f
