package main

import (
	"fmt"
	"io/ioutil"
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
