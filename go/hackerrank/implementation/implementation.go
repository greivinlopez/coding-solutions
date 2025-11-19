package main

import (
	"fmt"
	"math"
	"math/big"
	"slices"
	"sort"
	"strconv"
	"strings"
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

/*
 * Problem: https://www.hackerrank.com/challenges/permutation-equation/problem
 */
func permutationEquation(p []int32) []int32 {
	p1 := make(map[int32]int32)
	for i, v := range p {
		p1[v] = int32(i) + 1
	}
	r := make([]int32, 0, len(p))
	for x := 1; x <= len(p); x++ {
		px := p1[int32(x)]
		r = append(r, p1[px])
	}
	return r
}

/*
 * Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
 */
func jumpingOnClouds(c []int32, k int32) int32 {
	var e int32 = 100
	var current int32
	n := int32(len(c))

	for {
		current = (current + k) % n

		if c[current] == 1 {
			e -= 3
		} else {
			e -= 1
		}

		if current == 0 {
			break
		}
	}

	return e
}

/*
 * Problem: https://www.hackerrank.com/challenges/find-digits/problem
 */
func findDigits(n int32) int32 {
	nStr := strconv.Itoa(int(n))
	var count int32

	for _, char := range nStr {
		digit, err := strconv.Atoi(string(char))

		// In a real application, you'd handle this error, but since we are guaranteed
		// the input 'n' is an integer, this error should not occur.
		if err != nil {
			continue
		}

		if digit != 0 && int(n)%digit == 0 {
			count++
		}
	}

	return count
}

/*
 * Problem: https://www.hackerrank.com/challenges/extra-long-factorials/problem
 */
func extraLongFactorials(n int32) {
	r := new(big.Int)
	r = r.MulRange(1, int64(n))
	fmt.Print(r)
}

/*
 * Problem: https://www.hackerrank.com/challenges/append-and-delete/problem
 */
func appendAndDelete(s string, t string, k int32) string {
	lenS := len(s)
	lenT := len(t)

	if int(k) >= (lenS + lenT) {
		return "Yes"
	}

	i := 0
	for i < lenT && i < lenS {
		if s[i] != t[i] {
			break
		}
		i++
	}
	// 'i' is the length of the common prefix.
	steps := lenS + lenT - 2*i

	if int(k) >= steps && (int(k)-steps)%2 == 0 {
		return "Yes"
	}

	return "No"
}

/*
 * Problem: https://www.hackerrank.com/challenges/sherlock-and-squares/problem
 */
func squares(a int32, b int32) int32 {
	// Calculate the largest integer whose square is <= b.
	largestRoot := math.Floor(math.Sqrt(float64(b)))

	// Calculate the smallest integer whose square is >= a.
	smallestRoot := math.Ceil(math.Sqrt(float64(a)))

	// The number of perfect squares is the difference in the roots plus 1.
	r := 1 + largestRoot - smallestRoot

	return int32(r)
}

/*
 * Problem: https://www.hackerrank.com/challenges/library-fine/problem
 */
func libraryFine(d1 int32, m1 int32, y1 int32, d2 int32, m2 int32, y2 int32) int32 {
	if y1 > y2 {
		return 10000
	}

	if y1 == y2 && m1 > m2 {
		return (m1 - m2) * 500
	}

	if y1 == y2 && m1 == m2 && d1 > d2 {
		return (d1 - d2) * 15
	}

	return 0
}

/*
 * Problem: https://www.hackerrank.com/challenges/cut-the-sticks/problem
 */
func cutTheSticks(arr []int32) []int32 {
	slices.Sort(arr)

	var results []int32
	n := int32(len(arr))
	var i int32 = 0

	for i < n {
		results = append(results, n-i)
		currentShortest := arr[i]

		j := i
		for j < n && arr[j] == currentShortest {
			j++
		}

		i = j
	}

	return results
}

/*
 * Problem: https://www.hackerrank.com/challenges/cut-the-sticks/problem
 */
func nonDivisibleSubset(k int32, s []int32) int32 {
	remainderCounts := make([]int32, k)
	for _, val := range s {
		remainderCounts[val%k]++
	}

	var count int32 = 0

	if remainderCounts[0] > 0 {
		count += 1
	}

	for i := 1; i <= int(k)/2; i++ {

		if i*2 == int(k) {
			if remainderCounts[i] > 0 {
				count += 1
			}
		} else {
			c1 := remainderCounts[i]
			c2 := remainderCounts[int(k)-i]

			maxCount := int32(math.Max(float64(c1), float64(c2)))
			count += maxCount
		}
	}

	return count
}

/*
 * Problem: https://www.hackerrank.com/challenges/save-the-prisoner/problem
 */
func saveThePrisoner(n int32, m int32, s int32) int32 {
	return ((s + m - 2) % n) + 1
}

/*
 * Problem: https://www.hackerrank.com/challenges/repeated-string/problem
 */
func repeatedString(s string, n int64) int64 {
	size := int64(len(s))

	countInS := int64(strings.Count(s, "a"))
	totalFullCount := (n / size) * countInS

	remainderLen := n % size
	remainder := s[:int(remainderLen)]

	countInRemainder := int64(strings.Count(remainder, "a"))

	return totalFullCount + countInRemainder
}

/*
 * Problem: https://www.hackerrank.com/challenges/equality-in-a-array/problem
 */
func equalizeArray(arr []int32) int32 {
	counts := make(map[int]int)

	for _, val := range arr {
		counts[int(val)]++
	}

	maxFrequency := 0
	// Find the maximum frequency.
	for _, count := range counts {
		if count > maxFrequency {
			maxFrequency = count
		}
	}

	return int32(len(arr) - maxFrequency)
}

/*
 * Problem: https://www.hackerrank.com/challenges/queens-attack-2/problem
 */
func queensAttack(n int32, k int32, r_q int32, c_q int32, obstacles [][]int32) int32 {
	type position struct {
		row int32
		col int32
	}
	// In Go, convention is to use camelCase for variables
	boardSize := n
	var result int32 = 0

	// Create a map for efficient O(1) obstacle lookups.
	obstacleMap := make(map[position]bool)
	for _, obs := range obstacles {
		obsRow1 := obs[0]
		obsCol1 := obs[1]

		// Apply the same conversion
		obsRow0 := n - obsRow1
		obsCol0 := obsCol1 - 1

		obstacleMap[position{row: obsRow0, col: obsCol0}] = true
	}

	// Check all 8 directions: horizontal, vertical, and diagonal
	for rowDirection := int32(-1); rowDirection <= 1; rowDirection++ {
		for colDirection := int32(-1); colDirection <= 1; colDirection++ {

			// Skip the case where both directions are 0 (no movement)
			if rowDirection == 0 && colDirection == 0 {
				continue
			}

			// Start from queen's position
			currentRow, currentCol := n-r_q, c_q-1

			// Move in the current direction until we hit a boundary or obstacle
			for {
				// Calculate the next position
				nextRow := currentRow + rowDirection
				nextCol := currentCol + colDirection

				// Check for boundaries.
				if nextRow < 0 || nextRow >= boardSize || nextCol < 0 || nextCol >= boardSize {
					break // Hit a boundary, stop this direction
				}

				// Move one step in the current direction
				currentRow = nextRow
				currentCol = nextCol

				// Check if there's an obstacle at this new position
				// We check if the key exists in our map
				if obstacleMap[position{row: currentRow, col: currentCol}] {
					break // Found an obstacle, stop this direction
				}

				// If no boundary and no obstacle, it's a valid square
				result++
			}
		}
	}

	return result
}

/*
 * Problem: https://www.hackerrank.com/challenges/acm-icpc-team/problem
 */
func acmTeam(topic []string) []int32 {
	n := len(topic)

	// --- Edge Case Checks ---
	// If there are no members, or no topics, return [0, 0]
	if n == 0 {
		return []int32{0, 0}
	}
	// m is the number of topics (length of the binary string)
	// We assume all strings have the same length, as per the problem.
	m := len(topic[0])
	if m == 0 {
		return []int32{0, 0}
	}
	// --- End Edge Case Checks ---

	var maxTopics int = 0
	var maxTopicCount int = 0

	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			s1 := topic[i]
			s2 := topic[j]

			currentTopics := 0

			for k := 0; k < m; k++ {
				if s1[k] == '1' || s2[k] == '1' {
					currentTopics++
				}
			}

			if currentTopics > maxTopics {
				maxTopics = currentTopics
				maxTopicCount = 1
			} else if currentTopics == maxTopics {
				maxTopicCount++
			}
		}
	}

	return []int32{int32(maxTopics), int32(maxTopicCount)}
}

/*
 * Problem: https://www.hackerrank.com/challenges/taum-and-bday/problem
 */
func taumBday(b int32, w int32, bc int32, wc int32, z int32) int64 {
	x := min(bc, wc+z)
	y := min(wc, bc+z)
	return int64(b)*int64(x) + int64(w)*int64(y)
}

/*
 * Problem: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
 */
func organizingContainers(container [][]int32) string {
	n := len(container)
	capacity := make([]int64, n)
	typeCount := make([]int64, n)

	for i := range n {
		var currentCapacity int64 = 0
		var currentTypeCount int64 = 0

		for j := range n {
			currentCapacity += int64(container[i][j])
			currentTypeCount += int64(container[j][i])
		}

		// Store the calculated sums in their respective slices.
		capacity[i] = currentCapacity
		typeCount[i] = currentTypeCount
	}

	slices.Sort(capacity)
	slices.Sort(typeCount)

	for i := range n {
		if capacity[i] != typeCount[i] {
			return "Impossible"
		}
	}

	return "Possible"
}

/*
 * Problem: https://www.hackerrank.com/challenges/encryption/problem
 */
func encryption(s string) string {
	noSpaces := strings.ReplaceAll(s, " ", "")

	lenStr := len(noSpaces)
	if lenStr == 0 {
		return ""
	}

	sqrt := math.Sqrt(float64(lenStr))
	c := int(math.Ceil(sqrt))
	var e strings.Builder

	i := 0
	j := 0

	for range lenStr {
		if i+j > lenStr-1 {
			e.WriteByte(' ')
			j++
			i = 0
		}

		e.WriteByte(noSpaces[i+j])
		i += c
	}

	return e.String()
}

/*
 * Problem: https://www.hackerrank.com/challenges/bigger-is-greater/problem
 */
func biggerIsGreater(w string) string {
	reverse := func(slice []byte) {
		for l, r := 0, len(slice)-1; l < r; l, r = l+1, r-1 {
			slice[l], slice[r] = slice[r], slice[l]
		}
	}

	bytes := []byte(w)
	n := len(bytes)

	i := n - 2
	for i >= 0 && bytes[i] >= bytes[i+1] {
		i--
	}

	if i < 0 {
		return "no answer"
	}

	j := n - 1
	for bytes[j] <= bytes[i] {
		j--
	}

	bytes[i], bytes[j] = bytes[j], bytes[i]
	reverse(bytes[i+1:])

	return string(bytes)
}

/*
 * Problem: https://www.hackerrank.com/challenges/kaprekar-numbers/problem
 */
func kaprekarNumbers(p int32, q int32) {
	var kaprekar []int64

	for i := p; i <= q; i++ {
		// # n = i^2
		n := int64(i) * int64(i)
		s := strconv.FormatInt(n, 10)
		lenS := len(s)

		mid := lenS / 2
		lStr := s[:mid]
		rStr := s[mid:]

		var l int64
		if lStr != "" {
			l, _ = strconv.ParseInt(lStr, 10, 64)
		}

		var r int64
		if rStr != "" {
			r, _ = strconv.ParseInt(rStr, 10, 64)
		}

		if l+r == int64(i) {
			kaprekar = append(kaprekar, int64(i))
		}
	}

	if len(kaprekar) > 0 {
		strVals := make([]string, len(kaprekar))
		for idx, val := range kaprekar {
			strVals[idx] = strconv.FormatInt(val, 10)
		}

		fmt.Println(strings.Join(strVals, " "))
	} else {
		fmt.Println("INVALID RANGE")
	}
}

/*
 * Problem: https://www.hackerrank.com/challenges/beautiful-triplets/problem
 */
func beautifulTriplets(d int32, arr []int32) int32 {
	var res int32 = 0

	lookup := make(map[int32]struct{})
	for _, val := range arr {
		lookup[val] = struct{}{}
	}

	for _, val := range arr {
		// Check if the 2nd and 3rd elements exist in our "set".
		val2 := val + d
		val3 := val + (d * 2)

		_, ok1 := lookup[val2]
		_, ok2 := lookup[val3]

		if ok1 && ok2 {
			res++
		}
	}

	return res
}

/*
 * Problem: https://www.hackerrank.com/challenges/minimum-distances/problem
 */
func minimumDistances(a []int32) int32 {
	n := len(a)
	minDistance := int32(n + 1)
	for i := range n {
		for j := i + 1; j < n; j++ {
			if a[i] == a[j] {
				minDistance = min(int32(j-i), minDistance)
				break
			}
		}
	}
	if minDistance == int32(n+1) {
		return -1
	}
	return minDistance
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

	// var a []int32 = []int32{1, 2, 3}
	// var q []int32 = []int32{0, 1, 2}
	// result := circularArrayRotation(a, 2, q)
	// fmt.Println(result)

	// var p []int32 = []int32{4, 3, 5, 1, 2}
	// result := permutationEquation(p)
	// fmt.Println(result)

	// var c []int32 = []int32{0, 0, 1, 0, 0, 1, 1, 0}
	// result := jumpingOnClouds(c, 2)
	// fmt.Println(result)

	// result := findDigits(1012)
	// fmt.Println(result)

	// extraLongFactorials(30)

	// result := appendAndDelete("hackerhappy", "hackerrank", 9)
	// fmt.Println(result)

	// result := squares(3, 9)
	// fmt.Println(result)

	// result := libraryFine(9, 6, 2015, 6, 6, 2015)
	// fmt.Println(result)

	// var arr []int32 = []int32{5, 4, 4, 2, 2, 8}
	// result := cutTheSticks(arr)
	// fmt.Println(result)

	// var s []int32 = []int32{278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436}
	// result := nonDivisibleSubset(7, s)
	// fmt.Println(result)

	// result := saveThePrisoner(7, 19, 2)
	// fmt.Println(result)

	// result := repeatedString("aba", int64(10))
	// fmt.Println(result)

	// var arr []int32 = []int32{3, 3, 2, 1, 3}
	// result := equalizeArray(arr)
	// fmt.Println(result)

	// obstacles := [][]int32{
	// 	{5, 5},
	// 	{4, 2},
	// 	{2, 3},
	// }
	// result := queensAttack(5, 3, 4, 3, obstacles)
	// fmt.Println(result)

	// var topic []string = []string{"10101", "11100", "11010", "00101"}
	// result := acmTeam(topic)
	// fmt.Println(result)

	// result := taumBday(27984, 1402, 619246, 615589, 247954)
	// fmt.Println(result)

	// container := [][]int32{
	// 	{1, 3, 1},
	// 	{2, 1, 2},
	// 	{3, 3, 3},
	// }
	// result := organizingContainers(container)
	// fmt.Println(result)

	// result := encryption("feedthedog")
	// fmt.Println(result)

	// result := biggerIsGreater("dkhc")
	// fmt.Println(result)

	// kaprekarNumbers(1, 100)

	// var arr []int32 = []int32{1, 6, 7, 7, 8, 10, 12, 13, 14, 19}
	// result := beautifulTriplets(3, arr)
	// fmt.Println(result)

	var arr []int32 = []int32{1, 2, 3, 4, 5, 1}
	result := minimumDistances(arr)
	fmt.Println(result)
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
