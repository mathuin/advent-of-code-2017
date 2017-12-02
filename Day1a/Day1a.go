package main

import (
	"fmt"
	"io/ioutil"
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

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	seq, err := ioutil.ReadAll(os.Stdin)
	check(err)
	result, err := Captcha(strings.TrimSuffix(string(seq), "\n"))
	check(err)
	fmt.Println(result)
}
