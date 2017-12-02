package main

import (
	"fmt"
	"io/ioutil"
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
	Loop:
		for i, elem := range ints {
			for _, oelem := range ints[i+1:] {
				if elem > oelem {
					if elem%oelem == 0 {
						sum += elem / oelem
						break Loop
					}
				} else {
					if oelem%elem == 0 {
						sum += oelem / elem
						break Loop
					}
				}
			}
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
	sheet, err := ioutil.ReadFile("input")
	check(err)
	result, err := Checksum(sheet)
	check(err)
	fmt.Println(result)
}
