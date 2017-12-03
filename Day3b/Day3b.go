package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

type Loc struct {
	X int
	Y int
}

func (l Loc) nextLoc(dir Loc) Loc {
	return Loc{X: l.X + dir.X, Y: l.Y + dir.Y}
}

type Grid map[Loc]int

func (g Grid) sumNeighbors(curr Loc) int {
	var sum int
	neighvals := []int{-1, 0, 1}
	for _, i := range neighvals {
		for _, j := range neighvals {
			elem, ok := g[curr.nextLoc(Loc{X: i, Y: j})]
			if ok {
				sum += elem
			}
		}
	}
	return sum
}

// Larger as defined in the puzzle:
// As a stress test on the system, the programs here clear the grid and then
// store the value 1 in square 1. Then, in the same allocation order as shown
// above, they store the sum of the values in all adjacent squares, including
// diagonals.
//
// So, the first few squares' values are chosen as follows:
//
//  - Square 1 starts with the value 1.
//  - Square 2 has only one adjacent filled square (with value 1), so it
//    also stores 1.
//  - Square 3 has both of the above squares as neighbors and stores the sum
//    of their values, 2.
//  - Square 4 has all three of the aforementioned squares as neighbors and
//    stores the sum of their values, 4.
//  - Square 5 only has the first and fourth squares as neighbors, so it
//    gets the value 5.
//
// Once a square is written, its value does not change. Therefore, the first
// few squares would receive the following values:
//
// 147  142  133  122   59
// 304    5    4    2   57
// 330   10    1    1   54
// 351   11   23   25   26
// 362  747  806--->   ...
//
// What is the first value written that is larger than your puzzle input?
func Larger(square string) (int, error) {
	var currVal int

	// Comes in as a string, need it as a number.
	sq, err := strconv.Atoi(square)
	if err != nil {
		return currVal, err
	}

	// Have to step around the array in order.
	dirs := []Loc{Loc{1, 0}, Loc{0, 1}, Loc{-1, 0}, Loc{0, -1}}
	dirp := len(dirs) - 1

	// Initial conditions
	grid := make(Grid)
	currVal = 1
	currLoc := Loc{0, 0}
	grid[currLoc] = currVal

	// While the current value is less than the desired value:
	for currVal < sq {
		nextDir := (dirp + 1) % len(dirs)
		if _, ok := grid[currLoc.nextLoc(dirs[nextDir])]; !ok {
			dirp = nextDir
		}
		currLoc = currLoc.nextLoc(dirs[dirp])
		currVal = grid.sumNeighbors(currLoc)
		grid[currLoc] = currVal
	}

	return currVal, nil
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	square, err := ioutil.ReadAll(os.Stdin)
	check(err)
	result, err := Larger(strings.TrimSuffix(string(square), "\n"))
	check(err)
	fmt.Println(result)
}
