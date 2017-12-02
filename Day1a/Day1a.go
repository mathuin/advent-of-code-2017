package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

// Captcha as defined in the puzzle:
// The captcha requires you to review a sequence of digits (your puzzle input)
// and find the sum of all digits that match the next digit in the list. The
// list is circular, so the digit after the last digit is the first digit in
// the list.
func Captcha(seq string) (int, error) {
	var sum int

	seql := strings.Split(seq, "")
	last := len(seql) - 1

	for i, s := range seql {
		var d int
		if i == last {
			d = 0
		} else {
			d = i + 1
		}
		if s == seql[d] {
			v, err := strconv.Atoi(s)
			if err != nil {
				return sum, err
			}
			sum += v
		}
	}
	return sum, nil
}

func usage() {
	fmt.Fprintf(os.Stderr, "usage: %s [sequence]\n", os.Args[0])
	flag.PrintDefaults()
	os.Exit(2)
}

func main() {
	flag.Usage = usage
	flag.Parse()

	args := flag.Args()
	if len(args) < 1 {
		fmt.Println("Sequence missing.")
		os.Exit(1)
	}
	// No sanity checking on input here either.
	retval, err := Captcha(args[0])
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(retval)
}
