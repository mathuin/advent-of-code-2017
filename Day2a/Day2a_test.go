package main

import "testing"

var checksumtests = []struct {
	in  []byte
	out int
	err error
}{
	{[]byte("5 1 9 5\n7 5 3\n2 4 6 8\n"), 18, nil},
}

func TestChecksum(t *testing.T) {
	for _, tt := range checksumtests {
		var out int
		var err error
		out, err = Checksum(tt.in)
		if out != tt.out {
			t.Errorf("Given %s, expected %d, got %d", tt.in, tt.out, out)
		}
		if err != tt.err {
			t.Errorf("Given %s, expected %d, got %d", tt.in, tt.err, err)
		}

	}
}
