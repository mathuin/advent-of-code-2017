package main

import "testing"

var captchatests = []struct {
	in  string
	out int
	err error
}{
	{"1122", 3, nil},
	{"1111", 4, nil},
	{"1234", 0, nil},
	{"91212129", 9, nil},
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
