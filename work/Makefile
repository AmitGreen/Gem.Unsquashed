#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
AGATE_FILES = ../Agate/RUNME.py

BERYL_FILES = \
    ../Beryl/__init__.py \
    ../Beryl/Ask.py \
    ../Beryl/BerylAnswer.py \
    ../Beryl/Main.py

GEM_FILES = \
	../Gem/__init__.py \
    ../Gem/Absent.py ../Gem/All.py ../Gem/Ascii.py \
	../Gem/Boot.py \
	../Gem/Cache.py ../Gem/Cadence.py ../Gem/Codec.py ../Gem/Core.py ../Gem/CatchException.py \
	../Gem/DelayedFileOutput.py \
	../Gem/ErrorNumber.py ../Gem/Exception.py ../Gem/ExecuteFile.py \
	../Gem/FileOutput.py ../Gem/FileStatus.py \
	../Gem/Global.py \
    ../Gem/Import.py ../Gem/IO.py \
    ../Gem/Map.py \
    ../Gem/Output.py \
    ../Gem/Path.py ../Gem/Path2.py ../Gem/PortrayString.py \
    ../Gem/RegularExpression.py \
    ../Gem/SimpleStringIO.py ../Gem/StringOutput.py ../Gem/System.py \
    ../Gem/Traceback.py

DRAVITE_FILES = \
    ../Dravite/Euclid.py \
    ../Dravite/__init__.py \
    ../Dravite/Main.py \
    ../Dravite/RSA_Example.py

IVORY_FILES = ../Ivory/Main.py

LICENSE_FILES = \
    ../OtherLicenses/README.txt


PEARL_FILES = \
    ../Pearl/Comment.py ../Pearl/ConjureTreeComment.py ../Pearl/Core.py \
    ../Pearl/Line.py \
    ../Pearl/Token.py ../Pearl/Tokenizer.py

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

SAPPHIRE_FILES = \
    ../Sapphire/ActionWord.py ../Sapphire/Atom.py \
    ../Sapphire/BinaryExpression.py ../Sapphire/BookcaseDualExpression.py ../Sapphire/BookcaseDualStatement.py \
        ../Sapphire/BookcaseExpression.py ../Sapphire/BookcaseKeywordStatement.py \
        ../Sapphire/BookcaseKeywordDualStatement.py ../Sapphire/BookcaseManyExpression.py \
        ../Sapphire/BookcaseManyFrill.py ../Sapphire/BookcaseManyStatement.py ../Sapphire/BookcaseStatement.py \
        ../Sapphire/BookcaseTriple.py ../Sapphire/BodyStatement.py \
    ../Sapphire/Cache.py ../Sapphire/CallStatement.py ../Sapphire/Comment.py ../Sapphire/ConditionStatement.py \
        ../Sapphire/Core.py ../Sapphire/CreateMeta.py \
    ../Sapphire/DefinitionHeader.py ../Sapphire/DualFrill.py ../Sapphire/DualToken.py ../Sapphire/DualTwig.py \
        ../Sapphire/DumpToken.py \
    ../Sapphire/Elemental.py \
    ../Sapphire/Indentation.py \
    ../Sapphire/LineMarker.py \
    ../Sapphire/Main.py ../Sapphire/ManyExpression.py ../Sapphire/ManyFrill.py ../Sapphire/MemberExpression.py \
    ../Sapphire/Parse1.py ../Sapphire/Parse1Atom.py ../Sapphire/Tokenize1Header.py ../Sapphire/Parse1Call.py \
        ../Sapphire/Parse1Complex.py ../Sapphire/Parse1Expression.py ../Sapphire/Parse1ExpressionStatement.py \
        ../Sapphire/Parse1From.py ../Sapphire/Parse1Function.py ../Sapphire/Parse1Import.py \
        ../Sapphire/Parse1Simple.py \
        ../Sapphire/Parse2.py ../Sapphire/Parse3.py \
        ../Sapphire/PostfixExpression.py \
    ../Sapphire/Pattern.py \
    ../Sapphire/QuadrupleFrill.py ../Sapphire/QuadrupleToken.py \
    ../Sapphire/Suite.py \
    ../Sapphire/TernaryExpression.py ../Sapphire/TokenCache.py ../Sapphire/TokenTuple.py \
      ../Sapphire/Tokenize1Atom.py ../Sapphire/Tokenize1Name.py ../Sapphire/Tokenize1Operator.py \
      ../Sapphire/Tree.py ../Sapphire/TripleFrill.py ../Sapphire/TripleToken.py ../Sapphire/TupleOfExpression.py \
    ../Sapphire/UnaryExpression.py ../Sapphire/UnaryStatement.py \
    ../Sapphire/Whitespace.py
    #
    #   Excludes:
    #       ../Sapphire/Match.py
    #

TOPAZ_FILES = \
    ../Topaz/ConjureTreeComment.py ../Topaz/Core.py \
    ../Topaz/ExceptionChain.py \
    ../Topaz/Main.py \
    ../Topaz/Path.py ../Topaz/Pattern.py ../Topaz/PortrayString.py \
    ../Topaz/StringOutput.py

TREMOLITE_FILES = \
    ../Tremolite/Build.py \
    ../Tremolite/Compile.py ../Tremolite/Core.py ../Tremolite/CreateMatch.py \
    ../Tremolite/Main.py \
    ../Tremolite/Name.py \
    ../Tremolite/Parse.py ../Tremolite/PatternWrapper.py \
    #
    #   Excludes:
    #       ../Tremolite/LICENSE
    #       ../Tremolite/Match.py
    #


WORK_FILES = Makefile

FILES = \
    $(AGATE_FILES) \
    $(BERYL_FILES) \
    $(DRAVITE_FILES) \
    $(GEM_FILES) \
    $(IVORY_FILES) \
    $(LICENSE_FILES) \
    $(PEARL_FILES) \
    $(QUARTZ_FILES) \
    $(SAPPHIRE_FILES) \
    $(TOPAZ_FILES) \
    $(TREMOLITE_FILES) \
    $(WORK_FILES)


all: clean files links


clean:
	rm -rf __pycache__
	rm -f *.old *.new *.pyc

	rm -f 2re.py 2sf.py 2sp.py 2sc.py
	rm -f 3re.py 3sf.py 3sp.py 3sc.py
	rm -f a.py ab.py ac.py ag.py
	rm -f ba.py bi.py bk.py bm.py bo.py
	rm -f ca.py cd.py ce.py co.py
	rm -f de.py dfo.py di.py dm.py dr.py
	rm -f ef.py en.py ex.py
	rm -f files fo.py fs.py
	rm -f gd.py gg.py
	rm -f h1p.py h1pa.py h1pc.py h1pe.py h1pes.py h1pf.py h1pi.py h1pm.py h1ps.py h1px.py
	rm -f   h1za.py h1zh.py h1zn.py h1zo.py
	rm -f   h2f.py h2p.py h3e.py h3f.py h2t.py h2w.py h3t.py h3p.py h4f.py h4t.py
	rm -f   hat.py haw.py hbe.py hbs.py hca.py hcc.py hcd.py hcm.py hco.py hcs.py hdh.py hdt.py hel.py
	rm -f   hk.py hkd.py hkds.py hkf.py hkk.py hkkd.py hkm.py hkms.py hks.py hkt.py hi.py hl.py
	rm -f   hma.py hmc.py hme.py hmf.py hpt.py hs.py htc.py hto.py htr.py htt.py hu.py hus.py hw.py hx.py hy.py
	rm -f in.py im.py io.py iv.py
	rm -f jb.py
	rm -f l.txt lr.txt
	rm -f m m.py m.txt
	rm -f o.py
	rm -f pa.py pa2.py pco.py pcm.py pj.py pk.py pl.py ps.py ps3.py pz.py
	rm -f q1p.py qc.py ql.py qma.py qmc.py qp.py
	rm -f rm.py rx.py
	rm -f so.py ssio.py sy.py
	rm -f t.py t1.py tb.py tcm.py tco.py tlp.txt tma.py tmc.py tn.py tp.py tu.py tw.py tx.py
	rm -f zc.py ze.py zj.py zm.py zpa.py zps.py zpt.py zso.py


files:
	echo $(FILES) >files.new
	mv files.new files


links:
	ln -s /usr/lib/python2.7/re.py                      2re.py
	ln -s /usr/lib/python2.7/sre_compile.py             2sc.py
	ln -s /usr/lib/python2.7/sre_constants.py           2sf.py
	ln -s /usr/lib/python2.7/sre_parse.py               2sp.py
	ln -s /usr/lib/python3.5/re.py                      3re.py
	ln -s /usr/lib/python3.5/sre_compile.py             3sc.py
	ln -s /usr/lib/python3.5/sre_constants.py           3sf.py
	ln -s /usr/lib/python3.5/sre_parse.py               3sp.py
	ln -s ../Gem/All.py                                 a.py
	ln -s ../Gem/Absent.py                              ab.py
	ln -s ../Gem/Ascii.py                               ac.py
	ln -s ../Agate/RUNME.py                             ag.py
	ln -s ../Beryl/BerylAnswer.py                       ba.py
	ln -s ../Beryl/__init__.py                          bi.py
	ln -s ../Beryl/Ask.py                               bk.py
	ln -s ../Beryl/Main.py                              bm.py
	ln -s ../Gem/Boot.py                                bo.py
	ln -s ../Gem/Cache.py                               ca.py
	ln -s ../Gem/Cadence.py                             cd.py
	ln -s ../Gem/CatchException.py                      ce.py
	ln -s ../Gem/Core.py                                co.py
	ln -s ../Dravite/Euclid.py                          de.py
	ln -s ../Gem/DelayedFileOutput.py                   dfo.py
	ln -s ../Dravite/__init__.py                        di.py
	ln -s ../Dravite/Main.py                            dm.py
	ln -s ../Dravite/RSA_Example.py                     dr.py
	ln -s ../Gem/ExecuteFile.py                         ef.py
	ln -s ../Gem/ErrorNumber.py                         en.py
	ln -s ../Gem/Exception.py                           ex.py
	ln -s ../Gem/FileOutput.py                          fo.py
	ln -s ../Gem/FileStatus.py                          fs.py
	ln -s ../Gem/Codec.py                               gd.py
	ln -s ../Gem/Global.py                              gg.py
	ln -s ../Sapphire/Parse1.py                         h1p.py
	ln -s ../Sapphire/Parse1Atom.py                     h1pa.py
	ln -s ../Sapphire/Parse1Call.py                     h1pc.py
	ln -s ../Sapphire/Parse1Expression.py               h1pe.py
	ln -s ../Sapphire/Parse1ExpressionStatement.py      h1pes.py
	ln -s ../Sapphire/Parse1Function.py                 h1pf.py
	ln -s ../Sapphire/Parse1Import.py                   h1pi.py
	ln -s ../Sapphire/Parse1From.py                     h1pm.py
	ln -s ../Sapphire/Parse1Simple.py                   h1ps.py
	ln -s ../Sapphire/Parse1Complex.py                  h1px.py
	ln -s ../Sapphire/Tokenize1Atom.py                  h1za.py
	ln -s ../Sapphire/Tokenize1Header.py                h1zh.py
	ln -s ../Sapphire/Tokenize1Name.py                  h1zn.py
	ln -s ../Sapphire/Tokenize1Operator.py              h1zo.py
	ln -s ../Sapphire/Parse2.py                         h2p.py
	ln -s ../Sapphire/Parse3.py                         h3p.py
	ln -s ../Sapphire/DualFrill.py                      h2f.py
	ln -s ../Sapphire/DualToken.py                      h2t.py
	ln -s ../Sapphire/DualTwig.py                       h2w.py
	ln -s ../Sapphire/TernaryExpression.py              h3e.py
	ln -s ../Sapphire/TripleFrill.py                    h3f.py
	ln -s ../Sapphire/TripleToken.py                    h3t.py
	ln -s ../Sapphire/QuadrupleFrill.py                 h4f.py
	ln -s ../Sapphire/QuadrupleToken.py                 h4t.py
	ln -s ../Sapphire/Atom.py                           hat.py
	ln -s ../Sapphire/ActionWord.py                     haw.py
	ln -s ../Sapphire/BinaryExpression.py               hbe.py
	ln -s ../Sapphire/BodyStatement.py                  hbs.py
	ln -s ../Sapphire/Cache.py                          hca.py
	ln -s ../Sapphire/CreateMeta.py                     hcc.py
	ln -s ../Sapphire/ConditionStatement.py             hcd.py
	ln -s ../Sapphire/Comment.py                        hcm.py
	ln -s ../Sapphire/Core.py                           hco.py
	ln -s ../Sapphire/CallStatement.py                  hcs.py
	ln -s ../Sapphire/DefinitionHeader.py               hdh.py
	ln -s ../Sapphire/DumpToken.py                      hdt.py
	ln -s ../Sapphire/Elemental.py                      hel.py
	ln -s ../Sapphire/BookcaseExpression.py             hk.py
	ln -s ../Sapphire/BookcaseDualExpression.py         hkd.py
	ln -s ../Sapphire/BookcaseDualStatement.py          hkds.py
	ln -s ../Sapphire/BookcaseManyFrill.py              hkf.py
	ln -s ../Sapphire/BookcaseKeywordStatement.py       hkk.py
	ln -s ../Sapphire/BookcaseKeywordDualStatement.py   hkkd.py
	ln -s ../Sapphire/BookcaseManyExpression.py         hkm.py
	ln -s ../Sapphire/BookcaseManyStatement.py          hkms.py
	ln -s ../Sapphire/BookcaseStatement.py              hks.py
	ln -s ../Sapphire/BookcaseTriple.py                 hkt.py
	ln -s ../Sapphire/Indentation.py                    hi.py
	ln -s ../Sapphire/LineMarker.py                     hl.py
	ln -s ../Sapphire/Main.py                           hma.py
	ln -s ../Sapphire/Match.py                          hmc.py
	ln -s ../Sapphire/MemberExpression.py               hme.py
	ln -s ../Sapphire/ManyFrill.py                      hmf.py
	ln -s ../Sapphire/Pattern.py                        hpt.py
	ln -s ../Sapphire/Suite.py                          hs.py
	ln -s ../Sapphire/TokenCache.py                     htc.py
	ln -s ../Sapphire/TupleOfExpression.py              hto.py
	ln -s ../Sapphire/Tree.py                           htr.py
	ln -s ../Sapphire/TokenTuple.py                     htt.py
	ln -s ../Sapphire/UnaryExpression.py                hu.py
	ln -s ../Sapphire/UnaryStatement.py                 hus.py
	ln -s ../Sapphire/Whitespace.py                     hw.py
	ln -s ../Sapphire/PostfixExpression.py              hx.py
	ln -s ../Sapphire/ManyExpression.py                 hy.py
	ln -s ../Gem/__init__.py                            in.py
	ln -s ../Gem/Import.py                              im.py
	ln -s ../Ivory/Main.py                              iv.py
	ln -s ../Gem/IO.py                                  io.py
	ln -s ../Junk/Boot.py                               jb.py
	ln -s log.txt                                       l.txt
	ln -s ../OtherLicenses/README.txt                   lr.txt
	ln -s Makefile                                      m
	ln -s mine.txt                                      m.txt
	ln -s ../Gem/Map.py                                 m.py
	ln -s ../Gem/Output.py                              o.py
	ln -s ../Gem/Path.py                                pa.py
	ln -s ../Gem/Path2.py                               pa2.py
	ln -s ../Pearl/Comment.py                           pcm.py
	ln -s ../Pearl/Core.py                              pco.py
	ln -s ../Pearl/ConjureTreeComment.py                pj.py
	ln -s ../Pearl/Token.py                             pk.py
	ln -s ../Pearl/Line.py                              pl.py
	ln -s ../Gem/PortrayString.py                       ps.py
	ln -s ../Junk/PortrayString_3.py                    ps3.py
	ln -s ../Pearl/Tokenizer.py                         pz.py
	ln -s ../Quartz/Parse1.py                           q1p.py
	ln -s ../Quartz/Core.py                             qc.py
	ln -s ../Quartz/Line.py                             ql.py
	ln -s ../Quartz/Main.py                             qma.py
	ln -s ../Quartz/Match.py                            qmc.py
	ln -s ../Quartz/Pattern.py                          qp.py
	ln -s ../Agate/RUNME.py                             rm.py
	ln -s ../Gem/RegularExpression.py                   rx.py
	ln -s ../Gem/StringOutput.py                        so.py
	ln -s ../Gem/SimpleStringIO.py                      ssio.py
	ln -s ../Gem/System.py                              sy.py
	ln -s test2.py                                      t.py
	ln -s test.py                                       t1.py
	ln -s ../Gem/Traceback.py                           tb.py
	ln -s ../Tremolite/CreateMatch.py                   tcm.py
	ln -s ../Tremolite/Core.py                          tco.py
	ln -s ../Tremolite/LicenseTemplate.txt              tlp.txt
	ln -s ../Tremolite/Main.py                          tma.py
	ln -s ../Tremolite/Match.py                         tmc.py
	ln -s ../Tremolite/Name.py                          tn.py
	ln -s ../Tremolite/Parse.py                         tp.py
	ln -s ../Tremolite/Build.py                         tu.py
	ln -s ../Tremolite/PatternWrapper.py                tw.py
	ln -s ../Tremolite/Compile.py                       tx.py
	ln -s ../Topaz/Core.py                              zc.py
	ln -s ../Topaz/ExceptionChain.py                    ze.py
	ln -s ../Topaz/ConjureTreeComment.py                zj.py
	ln -s ../Topaz/Main.py                              zm.py
	ln -s ../Topaz/Path.py                              zpa.py
	ln -s ../Topaz/PortrayString.py                     zps.py
	ln -s ../Topaz/Pattern.py                           zpt.py
	ln -s ../Topaz/StringOutput.py                      zso.py
    
    
wc:
	#
	#  Excludes $(AGATE_FILES)
	#
	wc -l \
		$(BERYL_FILES) \
		$(DRAVITE_FILES) \
        $(GEM_FILES) \
        $(IVORY_FILES) \
        $(LICENSE_FILES) \
        $(QUARTZ_FILES) \
        $(SAPPHIRE_FILES) \
        $(TOPAZ_FILES) \
        $(TREMOLITE_FILES) \
        $(WORK_FILES)

test:
	cat \
		$(BERYL_FILES) \
		$(DRAVITE_FILES) \
		$(GEM_FILES) \
		$(IVORY_FILES) \
		$(QUARTZ_FILES) \
		$(SAPPHIRE_FILES) \
		$(TOPAZ_FILES) \
		$(TREMOLITE_FILES) \
            >test.py
	bash run.sh
