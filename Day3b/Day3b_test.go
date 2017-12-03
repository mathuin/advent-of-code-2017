package main

import "testing"

var largertests = []struct {
	in  string
	out int
	err error
}{
	{"3", 4, nil},
	{"12", 23, nil},
	{"25", 25, nil},
	{"512", 747, nil},
}

func TestLarger(t *testing.T) {
	for _, tt := range largertests {
		var out int
		var err error
		out, err = Larger(tt.in)
		if out != tt.out {
			t.Errorf("Given %s, expected %d, got %d", tt.in, tt.out, out)
		}
		if err != tt.err {
			t.Errorf("Given %s, expected %d, got %d", tt.in, tt.err, err)
		}

	}
}
