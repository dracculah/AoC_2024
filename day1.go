package main

import (
	"slices"
	"regexp"
	"strconv"
	"strings"
)

// 3 helper functions
func abs(x int) int {
	if (x < 0) {
		return -x
	} else {
		return x
	}
}

func assert(positiveRequest bool, message string) {
	if (positiveRequest == false) {
		panic(message)
	}
}

func compareSlices(sl1 []int, sl2 []int) bool {
	if (len(sl1) != len(sl2)) {
		return false
	}
	for i,x := range sl1 {
		if (x != sl2[i]) {
			return false
		}
	}
	return true
}

// AoC

// converts list of 2 integers separated by whitespace into 2 slices accordingly
func convertTableToSlices(strs []string) ([]int, []int) {

	// regexp of a line
	r, _ := regexp.Compile("\\s*([0-9]+)\\s+([0-9]+)")
	
	// calculate *valid* length first
	len_ := 0
	for _,x := range strs {
		if (r.MatchString(x)) {
			len_ += 1
		}
	}
	
	// create the slices
	sl1 := make([]int, len_)
	sl2 := make([]int, len_)
	
	// have an index of valid values
	idx := 0
	
	for _,x := range strs {
		if (r.MatchString(x)) {
			subs := r.FindStringSubmatch(x)
			//
			int_1, err1 := strconv.Atoi(subs[1])
			assert(err1 == nil, "error converting subs[1]='"+subs[1]+"' to int")
			sl1[idx] = int_1
			//
			int_2, err2 := strconv.Atoi(subs[2])
			assert(err2 == nil, "error converting subs[2]='"+subs[2]+"' to int")
			sl2[idx] = int_2
			
			idx += 1
		}
	}
	
	return sl1, sl2
}

// calculates distance from 2 slices
func getDistance(sl1, sl2 []int) int {
	assert(len(sl1) == len(sl2), "slices need to be equal sizes!")
	slices.Sort(sl1)
	slices.Sort(sl2)
	distance := 0
	for i, x := range sl1 {
		distance += abs(x - sl2[i])
	}
	return distance
}

// calculates distance from table
func getDistanceFromTable(strs []string) (int) {
	return getDistance(convertTableToSlices(strs))
}

func test_getDistance() {
	l1 := []int{3,4,2,1,3,3}
	l2 := []int{4,3,5,3,9,3}
	dist := getDistance(l1, l2)
	assert(dist == 11, "dist != 11")
}

func test_table_conversions() {
	s := `
	3   4
	4   3
	2   5
	1   3
	3   9
	3   3`
	ss := strings.Split(s, "\n")
	expected_1 := []int{3,4,2,1,3,3}
	expected_2 := []int{4,3,5,3,9,3}
	actual_1, actual_2 := convertTableToSlices(ss)
	assert(compareSlices(expected_1, actual_1), "expected_1 != actual_1")
	assert(compareSlices(expected_2, actual_2), "expected_2 != actual_2")
	assert(11 == getDistanceFromTable(ss), "11 != getDistanceFromTable(ss)")
}

// runs unit-tests
func main() {
	test_getDistance()
	test_table_conversions()
}
