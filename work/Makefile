#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
AGATE_FILES = ../Agate/RUNME.py

BERYL_FILES = \
    ../Beryl/__init__.py \
    ../Beryl/Ask.py \
    ../Beryl/BerylAnswer.py \
    ../Beryl/Main.py

LICENSE_FILES = \
    ../OtherLicenses/README.txt

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
    $(LICENSE_FILES) \
    $(ONYX_FILES) \
    $(QUARTZ_FILES) \
    $(SARDONYX_FILES) \
    $(WORK_FILES)


all: clean files links


clean:
	rm -rf __pycache__
	rm -f *.old *.new *.pyc
	rm -f ag.py
	rm -f ba.py bi.py bk.py bm.py
	rm -f files
	rm -f hma1.py hma2.py
	rm -f j1p.py jb.py
	rm -f l.txt lr.txt
	rm -f m
	rm -f oc.py od.py oe.py om.py
	rm -f ps3.py
	rm -f q1p.py qc.py ql.py qma.py qmc.py qp.py
	rm -f rm.py
	rm -f t.java t1.py
	rm -f xb.py


files:
	echo $(FILES) >files.1.tmp
	tr ' ' '\n' <files.1.tmp >files.2.tmp
	mv files.2.tmp files


links:
	ln -s ../Agate/RUNME.py                                                     ag.py
	ln -s ../Beryl/BerylAnswer.py                                               ba.py
	ln -s ../Beryl/__init__.py                                                  bi.py
	ln -s ../Beryl/Ask.py                                                       bk.py
	ln -s ../Beryl/Main.py                                                      bm.py
	ln -s ../bin/.pyxie/hma.py                                                  hma1.py
	ln -s ../bin/.pyxie/hma2.py                                                 hma2.py
	ln -s ../Junk/Boot.py                                                       jb.py
	ln -s log.txt                                                               l.txt
	ln -s ../OtherLicenses/README.txt                                           lr.txt
	ln -s Makefile                                                              m
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
	ln -s ../Sardonyx/Boot.py                                                   xb.py


wc:
	#
	#  Excludes $(AGATE_FILES)
	#
	wc -l \
        $(BERYL_FILES) \
        $(LICENSE_FILES) \
        $(ONYX_FILES) \
        $(QUARTZ_FILES) \
        $(SARDONYX_FILES) \
        $(WORK_FILES)

test:
	cat \
        $(BERYL_FILES) \
        $(ONYX_FILES) \
        $(QUARTZ_FILES) \
        $(SARDONYX_FILES) \
            >test.py
	bash run.sh
