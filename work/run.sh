#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
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

Main_py=../Beryl/Main.py
Main_py=../Ivory/Main.py
Main_py=../Tremolite/Main.py
Main_py=../Quartz/Main.py
Main_py=../Dravite/Main.py
Main_py=../Topaz/Main.py
Main_py=../Sapphire/Main.py

show=2

command="python $Main_py"
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
cat $show

while :
do
    $command $option <$tmp1 >&$tmp2
    if cmp -s $tmp2 2
    then
        :
    else
        mv $tmp2 2

        if [ $show = 2 ]; then
            echo -en '\E[H\E[J'
            tail -60 2
        fi
    fi

    $commandO $option <$tmp1 >&$tmp3
    mv $tmp3 2o

    $command3 $option <$tmp1 >&$tmp3
    if cmp -s $tmp3 3
    then
        :
    else
        mv $tmp3 3

        if [ $show = 3 ]; then
            echo -en '\E[H\E[J'
            tail -60 3
        fi
    fi

    $command3O $option <$tmp1 >&$tmp3
    mv $tmp3 3o

    sleep 0.01
done
