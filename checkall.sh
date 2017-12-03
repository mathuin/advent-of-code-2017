#!/bin/bash

tmpout="$(mktemp -d /tmp/advent.XXXXXX)"
for dir in `ls -d */`; do
    basename=`basename $dir`
    pushd $dir >/dev/null
    languages=""
    if [ -f $basename.py ]; then
        languages="$languages Python"
    fi
    if [ -f $basename.go ]; then
        languages="$languages Go"
    fi
    if [ "$languages" != "" ]; then
        echo "$basename:"
        for language in $languages; do
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
    fi
    popd >/dev/null
done
rm -rf $tmpout
