#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
print '1: %s' % ((globals().keys(),))
print '1.__builtins__: %s' % ((__builtins__.keys(),))
print
print

@gem('Onyx.Development')
def gem():
    require_gem('Onyx.Core')

    print '2: %s' % ((globals().keys(),))
    print '2.__builtins__: %s' % ((__builtins__.keys(),))
    print

    import sys

    sys.path.append('/usr/local/lib/python2.7/dist-packages')


    @share
    @privileged
    def command_development():
        print '3: %s' % ((globals().keys(),))
        print '3.__builtins__: %s' % ((__builtins__.keys(),))
        print


        from elasticsearch      import      Elasticsearch
        from elasticsearch_dsl  import      Search



        #line('sys.path: %s', sys.path)
        client = Elasticsearch()
        line('client: %s', client)
