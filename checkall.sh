#!/bin/bash

tmpout="$(mktemp -d /tmp/advent.XXXXXX)"
for dir in `ls -d */`; do
    basename=`echo $dir | sed -e "s|/||"`
    pushd $dir >/dev/null
    for language in Python Go; do
        if [ $language == "Python" ]; then
            ./$basename.py < input > $tmpout/checkout
        elif [ $language == "Go" ]; then
            go build && ./$basename < input > $tmpout/checkout && rm ./$basename
        fi
        diff $tmpout/checkout output >/dev/null
        if [ $? -eq 0 ]; then
            echo "$basename $language PASS"
        else
            echo "$basename $language FAIL"
        fi
    done
    popd >/dev/null
done
rm -rf $tmpout
