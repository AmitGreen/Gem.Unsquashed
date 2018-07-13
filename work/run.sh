#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
set -e$-

usage=false

case $# in
  0) ;;
  1) usage=true ;;
esac

if $usage
then
    echo "? usage: $0" >&2
    exit 1
fi

tmp_dir='../tmp'

if [ ! -d $tmp_dir ]
then
    mkdir $tmp_dir
fi

tmp1=$tmp_dir/tmp.1.$$.txt
tmp2=$tmp_dir/tmp.2.$$.txt
tmp3=$tmp_dir/tmp.3.$$.txt

for i in 1 2 3 15
do
    trap "trap $i; rm -f $tmp1 $tmp2 $tmp3; kill -$i $$; exit $i" $i
done

Main_py=show.py
Main_py=../Beryl/Main.py
Main_py=../Ivory/Main.py
Main_py=../Tremolite/Main.py
Main_py=../Quartz/Main.py
Main_py=../Dravite/Main.py
Main_py=../Crystal/Main.py
Main_py=../Topaz/Main.py
Main_py=../Onyx/Main.py
Main_py=../Diamond/Main.py
Main_py=../Jasper/Main.py
Main_py=../Sapphire/Main.py
Main_py=../Melanite/Main.py
Main_py=../Marble/Main.py

show=j
all=false
#all=true
total=75

command="python -sS $Main_py"
commandO="python -O $Main_py"
command3="python3 $Main_py"
command3O="python3 -O $Main_py"
#command="../bin/x"

option="dev"

cat >$tmp1 <<END
AmitGreen
CA1A41C16B1D3F25
Amit Green
his
y
y
END

echo -en '\E[H\E[J'

if [ -f $show ]; then
    tail -$total $show
else
    touch $show
fi

while :
do
    if [ $show = 2 -o $all = true ]; then
        if $command $option <$tmp1 >&$tmp2; then
            :
        fi

        #diff ../Topaz/GeneratedConjureDual.gpy ../Topaz/GeneratedConjureDual.py >>$tmp2
        #diff ../Topaz/GeneratedNew.gpy ../Topaz/GeneratedNew.py >>$tmp2
        if cmp -s $tmp2 2; then
            :
        else
            mv $tmp2 2

            if [ $show = 2 ]; then
                echo -en '\E[H\E[J'
                tail -$total 2
            fi
        fi
    fi

    if [ $show = 2o -o $all = true ]; then
        if $commandO $option <$tmp1 >&$tmp3; then
            :
        fi

        mv $tmp3 2o
    fi
   
    if [ $show = 3 -o $all = true ]; then
        $command3 $option <$tmp1 >&$tmp3
        if cmp -s $tmp3 3; then
            :
        else
            mv $tmp3 3
   
            if [ $show = 3 ]; then
                echo -en '\E[H\E[J'
                tail -$total 3
            fi
        fi
    fi
   
    if [ $show = 3o -o $all = true ]; then
       $command3O $option <$tmp1 >&$tmp3
       mv $tmp3 3o
    fi

    if [ $show = j ]; then
        (
            cd ../Jacinth

            if mvn package -DskipTests; then
                if java -ea -cp target/Jacinth-1.0-SNAPSHOT.jar link.crystal.Jacinth.Main; then
                    :
                fi
            fi

        ) <$tmp1 >&$tmp2

        sed \
            -e '/^\[ERROR\] COMPILATION ERROR : $/d' \
            -e '/^\[ERROR\] $/d' \
            -e '/^\[ERROR\] Failed to execute goal [-0-9.:a-z]* (default-compile) on project Jacinth: Compilation failure$/d' \
            -e '/^\[ERROR\] For more information about the errors and possible solutions, please read the following articles:$/d' \
            -e '/^\[ERROR\] -> \[Help 1\]/d' \
            -e '/^\[ERROR\] \[Help 1\] http:\/\/cwiki\.apache\.org\/confluence\/display\/MAVEN\/MojoFailureException$/d' \
            -e '/^\[ERROR\] Re-run Maven using the -X switch to enable full debug logging.$/d' \
            -e '/^\[ERROR\] To see the full stack trace of the errors, re-run Maven with the -e switch\.$/d' \
            -e '/^\[INFO\] 1 error$/d' \
            -e '/^\[INFO\] 1 warning$/d' \
            -e '/^\[INFO\] BUILD FAILURE$/d' \
            -e '/^\[INFO\] Building Jacinth 1\.0-SNAPSHOT$/d' \
            -e '/^\[INFO\] Building jar: /d' \
            -e '/^\[INFO\] BUILD SUCCESS$/d' \
            -e '/^\[INFO\] Changes detected - recompiling the module!$/d' \
            -e '/^\[INFO\] Compiling [1-9][0-9]* source files to /d' \
            -e '/^\[INFO\] Compiling 1 source file to /d' \
            -e '/^\[INFO\] --- .* ---$/d' \
            -e '/^\[INFO\] -*$/d' \
            -e '/^\[INFO\] $/d' \
            -e '/^\[INFO\] Final Memory: /d' \
            -e '/^\[INFO\] Finished at: /d' \
            -e '/^\[INFO\] Nothing to compile - all classes are up to date$/d' \
            -e '/^\[INFO\] Scanning for projects\.\.\.$/d' \
            -e '/^\[INFO\] skip non existing resourceDirectory /d' \
            -e '/^\[INFO\] Tests are skipped\.$/d' \
            -e '/^\[INFO\] Total time: /d' \
            -e '/^\[WARNING\] COMPILATION WARNING : $/d' \
            -e '/^\[WARNING\] File encoding has not been set, using platform encoding /d' \
            -e '/^\[WARNING\] Some messages have been simplified; recompile with -Xdiags:verbose to get full output$/d' \
            -e '/^\[WARNING\] Using platform encoding /d' \
                <$tmp2 >$tmp3

        cp $tmp2 /tmp/run.txt

        if cmp -s $tmp3 j; then
            :
        else
            mv $tmp3 j

            echo -en '\E[H\E[J'
            tail -$total j
        fi
    fi

    sleep 0.01
done
