#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
AGATE_FILES = ../Agate/RUNME.py

BERYL_FILES = \
    ../Beryl/__init__.py \
    ../Beryl/Ask.py \
    ../Beryl/BerylAnswer.py \
    ../Beryl/Main.py

CRYSTAL_FILES = \
    ../Crystal/__init__.py \
    ../Crystal/Board.py ../Crystal/BlankSquare.py \
    ../Crystal/CardRoot.py ../Crystal/ChessBishop.py ../Crystal/ChessKing.py ../Crystal/ChessKnight.py \
        ../Crystal/ChessPawn.py ../Crystal/ChessRook.py ../Crystal/Core.py \
    ../Crystal/Deck_7.py \
    ../Crystal/FrozenChessCard.py ../Crystal/FrozenCardRoot.py \
    ../Crystal/Game.py \
    ../Crystal/Main.py \
    ../Crystal/Player.py \
    ../Crystal/Square.py \
    ../Crystal/VoidSquare.py

DIAMOND_FILES = \
    ../Diamond/__init__.py \
    ../Diamond/Chore.py ../Diamond/Core.py \
    ../Diamond/Development.py \
    ../Diamond/Fibonacci.py \
    ../Diamond/Interval.py \
    ../Diamond/LifeCycle.py \
    ../Diamond/Main.py \
    ../Diamond/Shared.py ../Diamond/Status.py \
    ../Diamond/Thread.py

DRAVITE_FILES = \
    ../Dravite/Euclid.py \
    ../Dravite/__init__.py \
    ../Dravite/Main.py \
    ../Dravite/RSA_Example.py

IVORY_FILES = \
    ../Ivory/Main.py

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
    $(CRYSTAL_FILES) \
    $(DIAMOND_FILES) \
    $(DRAVITE_FILES) \
    $(IVORY_FILES) \
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
	rm -f d.py dc.py de.py df.py di.py dm.py dr.py dsh.py dst.py dt.py dw.py dy.py
	rm -f files
	rm -f hma1.py hma2.py
	rm -f iv.py
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
	rm -f ybd.py ybi.py ybq.py ycb.py ycr.py yd7.py yg.py yki.py ykn.py
	rm -f   ym.py yp.py yq.py yr.py yv.py yw.py yzc.py yzk.py yzr.py


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
	ln -s ../Diamond/Development.py                                             d.py
	ln -s ../Diamond/Core.py                                                    dc.py
	ln -s ../Dravite/Euclid.py                                                  de.py
	ln -s ../Diamond/Fibonacci.py                                               df.py
	ln -s ../Diamond/Interval.py                                                di.py
	ln -s ../Diamond/Main.py                                                    dm.py
	ln -s ../Dravite/RSA_Example.py                                             dr.py
	ln -s ../Diamond/Shared.py                                                  dsh.py
	ln -s ../Diamond/Status.py                                                  dst.py
	ln -s ../Diamond/Thread.py                                                  dt.py
	ln -s ../Diamond/Chore.py                                                   dw.py
	ln -s ../Diamond/LifeCycle.py                                               dy.py
	ln -s ../bin/.pyxie/hma.py                                                  hma1.py
	ln -s ../bin/.pyxie/hma2.py                                                 hma2.py
	ln -s ../Ivory/Main.py                                                      iv.py
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
	ln -s ../Crystal/Board.py                                                   ybd.py
	ln -s ../Crystal/ChessBishop.py                                             ybi.py
	ln -s ../Crystal/BlankSquare.py                                             ybq.py
	ln -s ../Crystal/CardRoot.py                                                ycb.py
	ln -s ../Crystal/Core.py                                                    ycr.py
	ln -s ../Crystal/Deck_7.py                                                  yd7.py
	ln -s ../Crystal/Game.py                                                    yg.py
	ln -s ../Crystal/ChessKing.py                                               yki.py
	ln -s ../Crystal/ChessKnight.py                                             ykn.py
	ln -s ../Crystal/Main.py                                                    ym.py
	ln -s ../Crystal/Player.py                                                  yp.py
	ln -s ../Crystal/Square.py                                                  yq.py
	ln -s ../Crystal/ChessRook.py                                               yr.py
	ln -s ../Crystal/VoidSquare.py                                              yv.py
	ln -s ../Crystal/ChessPawn.py                                               yw.py
	ln -s ../Crystal/FrozenChessCard.py                                         yzc.py
	ln -s ../Crystal/FrozenCardRoot.py                                          yzr.py


wc:
	#
	#  Excludes $(AGATE_FILES)
	#
	wc -l \
        $(BERYL_FILES) \
        $(CRYSTAL_FILES) \
        $(DIAMOND_FILES) \
        $(DRAVITE_FILES) \
        $(IVORY_FILES) \
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
        $(CRYSTAL_FILES) \
        $(DIAMOND_FILES) \
        $(DRAVITE_FILES) \
        $(IVORY_FILES) \
        $(JASPER_FILES) \
        $(MELANITE_FILES) \
        $(ONYX_FILES) \
        $(QUARTZ_FILES) \
        $(SARDONYX_FILES) \
            >test.py
	bash run.sh
