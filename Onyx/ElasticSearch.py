#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Onyx.ElasticSearch')
def gem():
    share = Shared.share


    @privileged
    def run_privileged_import():
        import sys


        sys.path.append('/usr/local/lib/python2.7/dist-packages')


        import  elasticsearch


        del sys.path[-1]


        share(
            'ElasticSearch',    elasticsearch.Elasticsearch,            #   NOTE: exported with capital 'S'
        )



    run_privileged_import()
