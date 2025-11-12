package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"slices"
	"sort"
	"strings"
	"time"
)

/*
 * Problem: https://www.hackerrank.com/challenges/simple-array-sum/problem
 */
func simpleArraySum(ar []int32) int32 {
	// Write your code here
	var result int32
	for _, value := range ar {
		result += value
	}
	return result
}

/*
 * Problem: https://www.hackerrank.com/challenges/compare-the-triplets/problem
 */
func compareTriplets(a []int32, b []int32) []int32 {
	r := make([]int32, 2)
	for i := 0; i < 3; i++ {
		if a[i] > b[i] {
			r[0] += 1
		} else if a[i] < b[i] {
			r[1] += 1
		}
	}
	return r
}

/*
 * Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
 */
func diagonalDifference(arr [][]int32) int32 {
	var diag1, diag2 int32
	j := len(arr) - 1
	for i := 0; i < len(arr); i++ {
		diag1 += arr[i][i]
		diag2 += arr[i][j]
		j--
	}
	return int32(math.Abs(float64(diag1) - float64(diag2)))
}

/*
 * Problem: https://www.hackerrank.com/challenges/plus-minus/problem
 */
func plusMinus(arr []int32) {
	var pos, neg, zer float64
	var n float64 = float64(len(arr))
	for i := 0; i < len(arr); i++ {
		if arr[i] > 0 {
			pos++
		} else if arr[i] < 0 {
			neg++
		} else {
			zer++
		}
	}
	fmt.Printf("%.6f\n", pos/n)
	fmt.Printf("%.6f\n", neg/n)
	fmt.Printf("%.6f\n", zer/n)
}

/*
 * Problem: https://www.hackerrank.com/challenges/staircase/problem
 */
func staircase(n int32) {
	for i := range n {
		spaces := strings.Repeat(" ", int(n-i-1))
		hashes := strings.Repeat("#", int(i+1))
		fmt.Printf("%v%v\n", string(spaces), string(hashes))
	}
}

/*
 * Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem
 */
func miniMaxSum(arr []int32) {
	sort.Slice(arr, func(i, j int) bool { return arr[i] < arr[j] })
	minSum, maxSum := 0, 0
	for i := range len(arr) {
		if i > 0 {
			maxSum += int(arr[i])
		}
		if i < len(arr)-1 {
			minSum += int(arr[i])
		}
	}
	fmt.Printf("%v %v\n", minSum, maxSum)
}

/*
 * Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
 */
func birthdayCakeCandles(candles []int32) int32 {
	tallest := slices.Max(candles)
	var count int32
	for _, candle := range candles {
		if tallest == candle {
			count++
		}
	}
	return count
}

/*
 * Problem: https://www.hackerrank.com/challenges/time-conversion/problem
 */
func timeConversion(s string) string {
	if t, error := time.Parse("03:04:05PM", s); error == nil {
		return t.Format(time.TimeOnly)
	}
	return ""
}

func main() {
	// var arr []int32 = []int32{-1, -1, 0, 2, 2}
	// plusMinus(arr)
	// var n int32 = 4
	// staircase(n)
	// var arr []int32 = []int32{1, 3, 5, 7, 9}
	// miniMaxSum(arr)
	// c := birthdayCakeCandles([]int32{3, 2, 1, 3})
	// fmt.Println(c)
	t := timeConversion("07:05:45PM")
	fmt.Println(t)
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
