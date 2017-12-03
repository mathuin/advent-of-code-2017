package main

import "testing"

var steptests = []struct {
	in  string
	out int
	err error
}{
	{"1", 0, nil},
	{"12", 3, nil},
	{"23", 2, nil},
	{"1024", 31, nil},
}

func TestSteps(t *testing.T) {
	for _, tt := range steptests {
		var out int
		var err error
		out, err = Steps(tt.in)
		if out != tt.out {
			t.Errorf("Given %s, expected %d, got %d", tt.in, tt.out, out)
		}
		if err != tt.err {
			t.Errorf("Given %s, expected %d, got %d", tt.in, tt.err, err)
		}

	}
}
