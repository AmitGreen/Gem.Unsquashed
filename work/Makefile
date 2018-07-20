#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
AGATE_FILES = ../Agate/RUNME.py

BERYL_FILES = \
    ../Beryl/__init__.py \
    ../Beryl/Ask.py \
    ../Beryl/BerylAnswer.py \
    ../Beryl/Main.py

DRAVITE_FILES = \
    ../Dravite/Euclid.py \
    ../Dravite/__init__.py \
    ../Dravite/Main.py \
    ../Dravite/RSA_Example.py

JASPER_FILES = \
    ../Jasper/Core.py \
    ../Jasper/Main.py \
    ../Jasper/Parse.py ../Jasper/Parse1.py \
        ../Jasper/Pattern.py
    #
    #   Excludes:
    #       ../Jasper/Match.py

LICENSE_FILES = \
    ../OtherLicenses/README.txt

MARBLE_FILES = \
    ../Marble/Core.py \
    ../Marble/GenerateAscii.py \
    ../Marble/GenerateTestPortrayString.py \
    ../Marble/NestedConjure.py \
    ../Marble/Main.py

MELANITE_FILES = \
    ../Melanite/Child.py \
    ../Melanite/Core.py \
    ../Melanite/Development.py \
    ../Melanite/Main.py \
    ../Melanite/Multiprocessing.py \

ONYX_FILES = \
    ../Onyx/__init__.py \
    ../Onyx/Core.py \
    ../Onyx/Development.py \
    ../Onyx/ElasticSearch.py \
    ../Onyx/Main.py \

QUARTZ_FILES = \
    ../Quartz/Parse1.py \
    ../Quartz/Core.py \
    ../Quartz/Main.py \
    ../Quartz/Line.py \
    ../Quartz/Pattern.py \
    #
    #   Excludes:
    #       ../Quartz/Match.py
    #

SARDONYX_FILES = \
    ../Sardonyx/Boot.py

WORK_FILES = \
    Makefile

FILES = \
    $(AGATE_FILES) \
    $(BERYL_FILES) \
    $(DRAVITE_FILES) \
    $(JASPER_FILES) \
    $(LICENSE_FILES) \
    $(MARBLE_FILES) \
    $(MELANITE_FILES) \
    $(ONYX_FILES) \
    $(QUARTZ_FILES) \
    $(SARDONYX_FILES) \
    $(WORK_FILES)


all: clean files links


clean:
	rm -rf __pycache__
	rm -f *.old *.new *.pyc
	rm -f 2re.py 2sf.py 2sp.py 2sc.py
	rm -f 3re.py 3sf.py 3sp.py 3sc.py
	rm -f ag.py
	rm -f ba.py bi.py bk.py bm.py
	rm -f files
	rm -f hma1.py hma2.py
	rm -f j0p.py j1p.py jb.py jcr.py jma.py jmc.py jp.py
	rm -f l.txt lr.txt
	rm -f m m.txt m1c.py m1ga.py m1gt.py m1m.py m1n.py
	rm -f   m2c.py m2m.py m3m.py
	rm -f   mc.py md.py mm.py
	rm -f oc.py od.py oe.py om.py
	rm -f ps3.py
	rm -f q1p.py qc.py ql.py qma.py qmc.py qp.py
	rm -f rm.py
	rm -f t.java t1.py
	rm -f xb.py
	rm -f vm.py


files:
	echo $(FILES) >files.1.tmp
	tr ' ' '\n' <files.1.tmp >files.2.tmp
	mv files.2.tmp files


links:
	ln -s /usr/lib/python2.7/re.py                                              2re.py
	ln -s /usr/lib/python2.7/sre_compile.py                                     2sc.py
	ln -s /usr/lib/python2.7/sre_constants.py                                   2sf.py
	ln -s /usr/lib/python2.7/sre_parse.py                                       2sp.py
	ln -s /usr/lib/python3.5/re.py                                              3re.py
	ln -s /usr/lib/python3.5/sre_compile.py                                     3sc.py
	ln -s /usr/lib/python3.5/sre_constants.py                                   3sf.py
	ln -s /usr/lib/python3.5/sre_parse.py                                       3sp.py
	ln -s ../Agate/RUNME.py                                                     ag.py
	ln -s ../Beryl/BerylAnswer.py                                               ba.py
	ln -s ../Beryl/__init__.py                                                  bi.py
	ln -s ../Beryl/Ask.py                                                       bk.py
	ln -s ../Beryl/Main.py                                                      bm.py
	ln -s ../bin/.pyxie/hma.py                                                  hma1.py
	ln -s ../bin/.pyxie/hma2.py                                                 hma2.py
	ln -s ../Jasper/Parse.py                                                    j0p.py
	ln -s ../Jasper/Parse1.py                                                   j1p.py
	ln -s ../Junk/Boot.py                                                       jb.py
	ln -s ../Jasper/Core.py                                                     jcr.py
	ln -s ../Jasper/Main.py                                                     jma.py
	ln -s ../Jasper/Match.py                                                    jmc.py
	ln -s ../Jasper/Pattern.py                                                  jp.py
	ln -s log.txt                                                               l.txt
	ln -s ../OtherLicenses/README.txt                                           lr.txt
	ln -s Makefile                                                              m
	ln -s mine.txt                                                              m.txt
	ln -s ../Marble/Core.py                                                     m1c.py
	ln -s ../Marble/GenerateAscii.py                                            m1ga.py
	ln -s ../Marble/GenerateTestPortrayString.py                                m1gt.py
	ln -s ../Marble/Main.py                                                     m1m.py
	ln -s ../Marble/NestedConjure.py                                            m1n.py
	ln -s ../Melanite/Core.py                                                   m2c.py
	ln -s ../Melanite/Main.py                                                   m2m.py
	ln -s ../Melanite/Child.py                                                  mc.py
	ln -s ../Melanite/Development.py                                            md.py
	ln -s ../Melanite/Multiprocessing.py                                        mm.py
	ln -s ../Onyx/Core.py                                                       oc.py
	ln -s ../Onyx/Development.py                                                od.py
	ln -s ../Onyx/ElasticSearch.py                                              oe.py
	ln -s ../Onyx/Main.py                                                       om.py
	ln -s ../Junk/PortrayString_3.py                                            ps3.py
	ln -s ../Quartz/Parse1.py                                                   q1p.py
	ln -s ../Quartz/Core.py                                                     qc.py
	ln -s ../Quartz/Line.py                                                     ql.py
	ln -s ../Quartz/Main.py                                                     qma.py
	ln -s ../Quartz/Match.py                                                    qmc.py
	ln -s ../Quartz/Pattern.py                                                  qp.py
	ln -s ../Agate/RUNME.py                                                     rm.py
	ln -s test.java                                                             t.java
	ln -s test.py                                                               t1.py
	ln -s ../Dravite/Main.py                                                    vm.py
	ln -s ../Sardonyx/Boot.py                                                   xb.py


wc:
	#
	#  Excludes $(AGATE_FILES)
	#
	wc -l \
        $(BERYL_FILES) \
        $(DRAVITE_FILES) \
        $(JASPER_FILES) \
        $(LICENSE_FILES) \
        $(MARBLE_FILES) \
        $(MELANITE_FILES) \
        $(ONYX_FILES) \
        $(QUARTZ_FILES) \
        $(SARDONYX_FILES) \
        $(WORK_FILES)

test:
	cat \
        $(BERYL_FILES) \
        $(DRAVITE_FILES) \
        $(JASPER_FILES) \
        $(MELANITE_FILES) \
        $(ONYX_FILES) \
        $(QUARTZ_FILES) \
        $(SARDONYX_FILES) \
            >test.py
	bash run.sh
