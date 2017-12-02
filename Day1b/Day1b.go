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
// Now, instead of considering the next digit, it wants you to consider the
// digit halfway around the circular list. That is, if your list contains 10
// items, only include a digit in your sum if the digit 10/2 = 5 steps forward
// matches it. Fortunately, your list has an even number of elements.
func Captcha(seq string) (int, error) {
	var sum int

	seql := strings.Split(seq, "")
	seqlen := len(seql)
	step := int(seqlen / 2)

	for i, s := range seql {
		if s == seql[(i+step)%seqlen] {
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
