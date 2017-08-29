import sys, traceback


def line(format, *arguments):
    sys.stderr.flush()
    print (format % arguments)
    sys.stdout.flush()


try:
    assert 0, 'b'
except:
    try:
        assert 0, 'a'
    finally:
        [e_type, e, e_traceback] = sys.exc_info()

        line('e: %s', e)
