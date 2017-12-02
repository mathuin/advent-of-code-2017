package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

// Checksum as defined in the puzzle:
// The spreadsheet consists of rows of apparently-random numbers. To make sure
// the recovery process is on the right track, they need you to calculate the
// spreadsheet's checksum. For each row, determine the difference between the
// largest value and the smallest value; the checksum is the sum of all of
// these differences.
func Checksum(sheet []byte) (int, error) {
	var sum int

	lines := strings.Split(string(sheet), "\n")

	for _, line := range lines {
		var ints []int
		cells := strings.Fields(line)
		if len(cells) == 0 {
			break
		}
		for _, elem := range cells {
			val, err := strconv.Atoi(elem)
			if err != nil {
				return sum, err
			}
			ints = append(ints, val)
		}
		// Go has no built-in max or min for int slices.
		max := 0
		min := math.MaxInt64
		for _, e := range ints {
			if e < min {
				min = e
			}
			if e > max {
				max = e
			}
		}
		sum += max
		sum -= min
	}

	return sum, nil
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	sheet, err := ioutil.ReadFile("input")
	if err != nil {
		panic(err)
	}
	result, err := Checksum(sheet)
	if err != nil {
		panic(err)
	}
	fmt.Println(result)
}
