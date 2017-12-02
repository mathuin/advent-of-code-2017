package main

import "testing"

var checksumtests = []struct {
	in  []byte
	out int
	err error
}{
	{[]byte("5 9 2 8\n9 4 7 3\n3 8 6 5\n"), 9, nil},
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
