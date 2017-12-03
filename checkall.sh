#!/bin/bash

tmpout="$(mktemp -d /tmp/advent.XXXXXX)"
for dir in `ls -d */`; do
    basename=`basename $dir`
    echo "$basename:"
    pushd $dir >/dev/null
    for language in Python Go; do
        if [ $language == "Python" ]; then
            ./$basename.py < input > $tmpout/checkout
        elif [ $language == "Go" ]; then
            go run ./$basename.go < input > $tmpout/checkout
        fi
        diff $tmpout/checkout output >/dev/null
        if [ $? -eq 0 ]; then
            echo "  $language PASS"
        else
            echo "  $language FAIL"
        fi
    done
    popd >/dev/null
done
rm -rf $tmpout
