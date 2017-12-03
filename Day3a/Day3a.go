package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"os"
	"strconv"
	"strings"
)

// Steps as defined in the puzzle:
// Each square on the grid is allocated in a spiral pattern starting at a
// location marked 1 and then counting up while spiraling outward. For
// example, the first few squares are allocated like this:
//
// 17  16  15  14  13
// 18   5   4   3  12
// 19   6   1   2  11
// 20   7   8   9  10
// 21  22  23---> ...
//
// While this is very space-efficient (no squares are skipped), requested data
// must be carried back to square 1 (the location of the only access port for
// this memory system) by programs that can only move up, down, left, or
// right. They always take the shortest path: the Manhattan Distance between
// the location of the data and square 1.
func Steps(square string) (int, error) {
	var steps int

	// Comes in as a string, need it as a number.
	// Golang prefers floats for ciel and sqrt.
	sq, err := strconv.ParseFloat(square, 64)
	if err != nil {
		return steps, err
	}
	// Square 1 is a special case.
	if sq == 1 {
		return 0, nil
	}
	// Rings are numbered by odd squares, counting from zero.
	// 1 is in ring 0, because 1 (sqrt(1)) is the zeroth odd square.
	// 2-9 are in ring 1, because 3 (sqrt(9)) is the second odd square.
	root := int(math.Ceil(math.Sqrt(sq)))
	// If the square is even, must add one!
	var oddsq int
	if root%2 == 0 {
		oddsq = root + 1
	} else {
		oddsq = root
	}
	// Ring is nth odd square.
	ring := (oddsq - 1) / 2

	// Rings are composed of four equal sequences.
	// Counting backwards from the maximum, the sequences:
	// start at 2*ring,
	// decrement 1 to ring, then
	// increment to 2*ring-1

	inseq := (oddsq*oddsq - int(sq)) % (2 * ring)
	if inseq < ring {
		steps = 2*ring - inseq
	} else {
		steps = inseq
	}

	return steps, nil
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	square, err := ioutil.ReadAll(os.Stdin)
	check(err)
	result, err := Steps(strings.TrimSuffix(string(square), "\n"))
	check(err)
	fmt.Println(result)
}
