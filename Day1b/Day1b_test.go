package main

import "testing"

var captchatests = []struct {
	in  string
	out int
	err error
}{
	{"1212", 6, nil},
	{"1221", 0, nil},
	{"123425", 4, nil},
	{"123123", 12, nil},
	{"12131415", 4, nil},
}

func TestCaptcha(t *testing.T) {
	for _, tt := range captchatests {
		var out int
		var err error
		out, err = Captcha(tt.in)
		if out != tt.out {
			t.Errorf("Given %s, expected %d, got %d", tt.in, tt.out, out)
		}
		if err != tt.err {
			t.Errorf("Given %s, expected %d, got %d", tt.in, tt.err, err)
		}
	}
}
