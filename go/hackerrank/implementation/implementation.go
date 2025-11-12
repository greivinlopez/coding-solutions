package main

import (
	"fmt"
	"math"
	"slices"
	"sort"
	"strconv"
	"time"
)

/*
 * Problem: https://www.hackerrank.com/challenges/grading/problem
 */
func gradingStudents(grades []int32) []int32 {
	result := make([]int32, len(grades))
	for i, g := range grades {
		if g >= 38 && (int32(math.Ceil(float64(g)/5)*5)-g) < 3 {
			result[i] = int32(math.Ceil(float64(g)/5) * 5)
		} else {
			result[i] = g
		}
	}
	return result
}

/*
 * Problem: https://www.hackerrank.com/challenges/apple-and-orange/problem
 */
func countApplesAndOranges(s int32, t int32, a int32, b int32, apples []int32, oranges []int32) {
	countApples, countOranges := 0, 0
	isWithin := func(n, a, b int32) bool { return n >= a && n <= b }
	for _, d := range apples {
		if isWithin(a+d, s, t) {
			countApples++
		}
	}
	for _, d := range oranges {
		if isWithin(b+d, s, t) {
			countOranges++
		}
	}
	fmt.Printf("%v\n%v\n", countApples, countOranges)
}

/*
 * Problem: https://www.hackerrank.com/challenges/kangaroo/problem
 */
func kangaroo(x1 int32, v1 int32, x2 int32, v2 int32) string {
	isInteger := func(n float64) bool { return n == math.Trunc(n) }
	if v1 == v2 {
		// If v1 == v2, they can only meet if they start at the same place (x1 == x2).
		if x1 == x2 {
			return "YES"
		}
		// If v1 == v2 but x1 != x2, they will never meet.
		return "NO"
	}
	k := float64(x1-x2) / float64(v2-v1)
	// Check if 'k' is a positive integer.
	if k > 0 && isInteger(k) {
		return "YES"
	}
	return "NO"
}

/*
 * Problem: https://www.hackerrank.com/challenges/between-two-sets/problem
 */
func getTotalX(a []int32, b []int32) int32 {
	var count int32
	start := slices.Max(a)
	end := slices.Min(b) + 1
	for x := start; x < end; x++ {
		valid := true
		for _, ai := range a {
			if x%ai != 0 {
				valid = false
				break
			}
		}
		for _, bi := range b {
			if bi%x != 0 {
				valid = false
				break
			}
		}
		if valid {
			count++
		}
	}
	return count
}

/*
 * Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
 */
func breakingRecords(scores []int32) []int32 {
	var high, low, brokes_h, brokes_l int32 = scores[0], scores[0], 0, 0
	for i, s := range scores {
		if i > 0 {
			if s > high {
				high = s
				brokes_h++
			}
			if s < low {
				low = s
				brokes_l++
			}
		}
	}
	return []int32{brokes_h, brokes_l}
}

/*
 * Problem: https://www.hackerrank.com/challenges/the-birthday-bar/problem
 */
func birthday(s []int32, d int32, m int32) int32 {
	var c int32 = 0
	sum := func(s []int32) int32 {
		var total int32
		for _, n := range s {
			total += n
		}
		return total
	}
	for i := range s {
		if i+int(m) <= len(s) && sum(s[i:i+int(m)]) == d {
			c++
		}
	}
	return c
}

/*
 * Problem: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
 */
func divisibleSumPairs(n int32, k int32, ar []int32) int32 {
	var c int32
	for i := 0; i < int(n); i++ {
		for j := i + 1; j < int(n); j++ {
			if (ar[i]+ar[j])%k == 0 {
				c++
			}
		}
	}
	return c
}

/*
 * Problem: https://www.hackerrank.com/challenges/migratory-birds/problem
 */
func migratoryBirds(arr []int32) int32 {
	sightings := make(map[int32]int32)
	for _, bird := range arr {
		sightings[bird]++ // Increment the count for each item
	}

	type KVPair struct {
		Key   int32
		Value int32
	}

	var pairs []KVPair
	for k, v := range sightings {
		pairs = append(pairs, KVPair{Key: k, Value: v})
	}

	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i].Value != pairs[j].Value {
			return pairs[i].Value > pairs[j].Value
		}
		return pairs[i].Key < pairs[j].Key
	})

	return pairs[0].Key
}

/*
 * Problem: https://www.hackerrank.com/challenges/day-of-the-programmer/problem
 */
func dayOfProgrammer(year int32) string {
	if year == 1918 {
		return "26.09.1918"
	}
	if year < 1918 {
		if year%4 == 0 {
			return "12.09." + strconv.Itoa(int(year))
		} else {
			return "13.09." + strconv.Itoa(int(year))
		}
	}
	t := time.Date(int(year), time.January, 1, 0, 0, 0, 0, time.UTC)
	d := t.Add(time.Hour * 24 * 255)
	return d.Format("02.01.2006")
}

/*
 * Problem: https://www.hackerrank.com/challenges/bon-appetit/problem
 */
func bonAppetit(bill []int32, k int32, b int32) {
	sum := func(s []int32) int32 {
		var total int32
		for _, n := range s {
			total += n
		}
		return total
	}

	brianBill := append(bill[:k], bill[int(k)+1:]...)
	annaBill := math.Round(float64(sum(brianBill) / 2.0))
	if int32(annaBill) == b {
		fmt.Println("Bon Appetit")
	} else {
		fmt.Println(b - int32(annaBill))
	}
}

/*
 * Problem: https://www.hackerrank.com/challenges/sock-merchant/problem
 */
func sockMerchant(_ int32, ar []int32) int32 {
	var count int32
	socks := make(map[int32]bool)
	for _, s := range ar {
		if _, exists := socks[s]; exists {
			delete(socks, s)
			count++
		} else {
			socks[s] = true
		}
	}
	return count
}

/*
 * Problem: https://www.hackerrank.com/challenges/drawing-book/problem
 */
func pageCount(n int32, p int32) int32 {
	floorDiv := func(a, b int32) int32 {
		res := a / b
		if (a%b != 0) && ((a < 0) != (b < 0)) {
			res--
		}
		return res
	}
	s := floorDiv(p, 2)
	e := floorDiv(n, 2) - s
	return min(s, e)
}

/*
 * Problem: https://www.hackerrank.com/challenges/counting-valleys/problem
 */
func countingValleys(_ int32, path string) int32 {
	var valleys, level int32

	for _, step := range path {
		if step == 'U' {
			level++
			// If the level is 0 now, we *must* have just
			// stepped up from -1, completing a valley.
			if level == 0 {
				valleys++
			}
		} else { // step == 'D'
			level--
		}
	}
	return valleys
}

/*
 * Problem: https://www.hackerrank.com/challenges/electronics-shop/problem
 */
func getMoneySpent(keyboards []int32, drives []int32, b int32) int32 {
	var maxSpent int32 = -1
	for _, k := range keyboards {
		for _, d := range drives {
			sum := k + d

			if sum <= b {
				if sum > maxSpent {
					maxSpent = sum
				}
			}
		}
	}
	return maxSpent
}

/*
 * Problem: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
 */
func catAndMouse(x int32, y int32, z int32) string {
	abs := func(n int32) int32 {
		if n < 0 {
			return -n
		}
		return n
	}
	cat_a := abs(z - x)
	cat_b := abs(z - y)
	if cat_a < cat_b {
		return "Cat A"
	}
	if cat_b < cat_a {
		return "Cat B"
	}
	return "Mouse C"
}

/*
 * Problem: https://www.hackerrank.com/challenges/picking-numbers/problem
 */
func pickingNumbers(a []int32) int32 {
	maxVal := slices.Max(a)
	c := make([]int32, maxVal+1)
	for _, v := range a {
		c[v] += 1
	}
	var m int32
	for i := 0; i < len(c)-1; i++ {
		m = max(m, c[i]+c[i+1])
	}
	return m
}

/*
 * Problem: https://www.hackerrank.com/challenges/the-hurdle-race/problem
 */
func hurdleRace(k int32, height []int32) int32 {
	maxHeight := slices.Max(height)
	if k >= maxHeight {
		return 0
	} else {
		return maxHeight - k
	}
}

/*
 * Problem: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
 */
func designerPdfViewer(h []int32, word string) int32 {
	var tallest int32 = 1
	for _, c := range word {
		height := h[int(c)-97]
		tallest = max(tallest, height)
	}
	return tallest * int32(len(word))
}

/*
 * Problem: https://www.hackerrank.com/challenges/utopian-tree/problem
 */
func utopianTree(n int32) int32 {
	var height int32 = 1
	for c := 1; c < int(n)+1; c++ {
		if c%2 == 0 {
			height++
		} else {
			height *= 2
		}
	}
	return height
}

/*
 * Problem: https://www.hackerrank.com/challenges/angry-professor/problem
 */
func angryProfessor(k int32, a []int32) string {
	students := 0
	for _, t := range a {
		if t <= 0 {
			students++
		}
	}
	if students >= int(k) {
		return "NO"
	}
	return "YES"
}

/*
 * Problem: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
 */
func beautifulDays(i int32, j int32, k int32) int32 {
	var count int32
	for n := i; n <= j; n++ {
		num := n
		reversed := int32(0)

		for num > 0 {
			digit := num % 10
			reversed = reversed*10 + digit
			num /= 10
		}

		diff := n - reversed
		if diff < 0 {
			diff = -diff
		}

		if diff%k == 0 {
			count++
		}
	}
	return count
}

/*
 * Problem: https://www.hackerrank.com/challenges/strange-advertising/problem
 */
func viralAdvertising(n int32) int32 {
	var people, cumulative int32 = 5, 0
	for i := int32(1); i <= n; i++ {
		likes := math.Floor(float64(people) / 2.0)
		cumulative += int32(likes)
		people = int32(likes) * 3
	}
	return cumulative
}

/*
 * Problem: https://www.hackerrank.com/challenges/circular-array-rotation/problem
 */
func circularArrayRotation(a []int32, k int32, queries []int32) []int32 {
	rotateRight := func(s []int32, n int32) []int32 {
		length := int32(len(s))
		if length == 0 {
			return s
		}
		n = n % length
		return append(s[length-n:], s[:length-n]...)
	}
	result := make([]int32, len(queries))
	rotated := rotateRight(a, k)
	for i, v := range queries {
		result[i] = rotated[v]
	}
	return result
}

func main() {

	// var grades []int32 = []int32{73, 67, 38, 33}
	// result := gradingStudents(grades)
	// fmt.Println(result)

	// var apples []int32 = []int32{-2, 2, 1}
	// var oranges []int32 = []int32{5, -6}
	// countApplesAndOranges(7, 11, 5, 15, apples, oranges)

	// result := kangaroo(0, 3, 4, 2)
	// fmt.Println(result)
	// result = kangaroo(0, 2, 5, 3)
	// fmt.Println(result)

	// var a []int32 = []int32{2, 4}
	// var b []int32 = []int32{16, 32, 96}
	// result := getTotalX(a, b)
	// fmt.Println(result)

	// var scores []int32 = []int32{10, 5, 20, 20, 4, 5, 2, 25, 1}
	// result := breakingRecords(scores)
	// fmt.Println(result)

	// var s []int32 = []int32{1, 2, 1, 3, 2}
	// result := birthday(s, 3, 2)
	// fmt.Println(result)

	// var ar []int32 = []int32{1, 3, 2, 6, 1, 2}
	// result := divisibleSumPairs(6, 3, ar)
	// fmt.Println(result)

	// var arr []int32 = []int32{1, 4, 4, 4, 5, 3}
	// result := migratoryBirds(arr)
	// fmt.Println(result)

	// result := dayOfProgrammer(2016)
	// fmt.Println(result)

	// var bill []int32 = []int32{3, 10, 2, 9}
	// bonAppetit(bill, 1, 7)

	// var socks []int32 = []int32{10, 20, 20, 10, 10, 30, 50, 10, 20}
	// result := sockMerchant(9, socks)
	// fmt.Println(result)

	// result := pageCount(6, 2)
	// fmt.Println(result)

	// result := countingValleys(8, "UDDDUDUU")
	// fmt.Println(result)

	// var keyboards []int32 = []int32{3, 1}
	// var drives []int32 = []int32{5, 2, 8}
	// result := getMoneySpent(keyboards, drives, 10)
	// fmt.Println(result)

	// result := catAndMouse(2, 5, 4)
	// fmt.Println(result)

	// var a []int32 = []int32{1, 1, 2, 2, 4, 4, 5, 5, 5}
	// result := pickingNumbers(a)
	// fmt.Println(result)

	// var height []int32 = []int32{1, 6, 3, 5, 2}
	// result := hurdleRace(4, height)
	// fmt.Println(result)

	// var h []int32 = []int32{1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5}
	// result := designerPdfViewer(h, "abc")
	// fmt.Println(result)

	// result := utopianTree(4)
	// fmt.Println(result)

	// var a []int32 = []int32{26, 94, -95, 34, 67, -97, 17, 52, 1, 86}
	// result := angryProfessor(7, a)
	// fmt.Println(result)

	// result := beautifulDays(20, 23, 6)
	// fmt.Println(result)

	// result := viralAdvertising(3)
	// fmt.Println(result)

	var a []int32 = []int32{1, 2, 3}
	var q []int32 = []int32{0, 1, 2}
	result := circularArrayRotation(a, 2, q)
	fmt.Println(result)
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
