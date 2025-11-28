package main

import (
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

/*
 * Problem: https://www.hackerrank.com/challenges/weighted-uniform-string/problem
 */
func weightedUniformStrings(s string, queries []int32) []string {
	weights := make(map[int]struct{})
	w := 0
	for i := 0; i < len(s); i++ {
		if i > 0 && s[i] == s[i-1] {
			w += int(s[i] - 'a' + 1)
		} else {
			w = int(s[i] - 'a' + 1)
		}
		weights[w] = struct{}{}
	}
	r := []string{}
	for i := range queries {
		if _, exists := weights[int(queries[i])]; exists {
			r = append(r, "Yes")
		} else {
			r = append(r, "No")
		}
	}
	return r
}

/*
 * Problem: https://www.hackerrank.com/challenges/reduced-string/problem
 */
func superReducedString(s string) string {
	stack := []byte{}

	for i := 0; i < len(s); i++ {
		char := s[i]

		// If the stack is not empty and the top element matches the current char:
		if len(stack) > 0 && stack[len(stack)-1] == char {
			// Rremove the last element
			stack = stack[:len(stack)-1]
		} else {
			// Otherwise, push the current char onto the stack
			stack = append(stack, char)
		}
	}

	if len(stack) == 0 {
		return "Empty String"
	}

	return string(stack)
}

/*
 * Problem: https://www.hackerrank.com/challenges/simple-array-sum/problem
 */
func camelcase(s string) int32 {
	var count int32 = 1
	for _, c := range s {
		if unicode.IsUpper(c) {
			count++
		}
	}
	return count
}

/*
 * Problem: https://www.hackerrank.com/challenges/strong-password/problem
 */
func minimumNumber(n int32, password string) int32 {
	specialChars := "!@#$%^&*()-+"

	// Use boolean flags to track what we have found.
	var (
		hasDigit   bool
		hasLower   bool
		hasUpper   bool
		hasSpecial bool
	)

	var missingTypes int32 = 4
	for _, char := range password {
		// We check if we ALREADY found the type (!hasDigit).
		// If not, and the char matches, we mark it found and decrease the missing count.
		if !hasDigit && unicode.IsDigit(char) {
			hasDigit = true
			missingTypes--
		} else if !hasLower && unicode.IsLower(char) {
			hasLower = true
			missingTypes--
		} else if !hasUpper && unicode.IsUpper(char) {
			hasUpper = true
			missingTypes--
		} else if !hasSpecial && strings.ContainsRune(specialChars, char) {
			hasSpecial = true
			missingTypes--
		}
	}

	// We need at least 6 characters total.
	missingLength := max(0, 6-n)

	// Return the maximum of the two requirements.
	return max(missingTypes, missingLength)
}

/*
 * Problem: https://www.hackerrank.com/challenges/two-characters/problem
 */
func alternate(s string) int32 {
	// Characters present in s
	var present [26]bool
	for _, char := range s {
		if char >= 'a' && char <= 'z' {
			present[char-'a'] = true
		}
	}

	maxLen := 0

	// Iterate through all unique pairs of characters (i, j).
	for i := range 26 {
		if !present[i] {
			continue
		}
		for j := i + 1; j < 26; j++ {
			if !present[j] {
				continue
			}

			charA := rune('a' + i)
			charB := rune('a' + j)

			currentLen := 0
			var lastSeen rune // Defaults to 0 (null char), safe for comparison
			isValid := true

			for _, char := range s {
				// We only care about the two characters in our current pair
				if char == charA || char == charB {
					if char == lastSeen {
						// Optimization: If we see the same char twice in a row, this pair is invalid.
						// We can break immediately.
						isValid = false
						break
					}
					lastSeen = char
					currentLen++
				}
			}

			if isValid && currentLen > maxLen {
				maxLen = currentLen
			}
		}
	}

	return int32(maxLen)
}

/*
 * Problem: https://www.hackerrank.com/challenges/caesar-cipher-1/problem
 */
func caesarCipher(s string, k int32) string {
	var sb strings.Builder
	sb.Grow(len(s))
	shift := rune(k % 26)

	for _, char := range s {
		if char >= 'a' && char <= 'z' {
			newChar := 'a' + (char-'a'+shift)%26
			sb.WriteRune(newChar)
		} else if char >= 'A' && char <= 'Z' {
			newChar := 'A' + (char-'A'+shift)%26
			sb.WriteRune(newChar)
		} else {
			sb.WriteRune(char)
		}
	}

	return sb.String()
}

/*
 * Problem: https://www.hackerrank.com/challenges/mars-exploration/problem
 */
func marsExploration(s string) int32 {
	changedCount := 0

	for i := range len(s) {
		remainder := i % 3

		if remainder == 1 {
			if s[i] != 'O' {
				changedCount++
			}
		} else {
			if s[i] != 'S' {
				changedCount++
			}
		}
	}

	return int32(changedCount)
}

/*
 * Problem: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
 */
func hackerrankInString(s string) string {
	target := "hackerrank"

	if len(s) < len(target) {
		return "NO"
	}

	// 'j' tracks our position in the "hackerrank" string.
	j := 0
	for i := range len(s) {
		if s[i] == target[j] {
			j++

			if j == len(target) {
				return "YES"
			}
		}
	}

	return "NO"
}

/*
 * Problem: https://www.hackerrank.com/challenges/pangrams/problem
 */
func pangrams(s string) string {
	var seen [26]bool
	uniqueCount := 0

	for _, r := range s {
		var index int

		if r >= 'a' && r <= 'z' {
			index = int(r - 'a')
		} else if r >= 'A' && r <= 'Z' {
			index = int(r - 'A')
		} else {
			// Skip spaces and non-letter characters
			continue
		}

		if !seen[index] {
			seen[index] = true
			uniqueCount++

			// If we have found all 26 letters, we can stop immediately.
			if uniqueCount == 26 {
				return "pangram"
			}
		}
	}

	return "not pangram"
}

/*
 * Problem: https://www.hackerrank.com/challenges/separate-the-numbers/problem
 */
func separateNumbers(s string) {
	n := len(s)
	if n < 2 {
		fmt.Println("NO")
		return
	}

	for i := 1; i <= n/2; i++ {
		sub := s[:i]

		first, err := strconv.ParseInt(sub, 10, 64)
		if err != nil {
			continue
		}

		seq := strconv.FormatInt(first, 10)

		var sb strings.Builder
		sb.WriteString(seq)

		cur := first
		for sb.Len() < n {
			cur++
			sb.WriteString(strconv.FormatInt(cur, 10))
		}

		if sb.String() == s {
			fmt.Printf("YES %d\n", first)
			return
		}
	}

	fmt.Println("NO")
}

/*
 * Problem: https://www.hackerrank.com/challenges/funny-string/problem
 */
func funnyString(s string) string {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	n := len(s)

	for i := 0; i < n/2; i++ {
		diffStart := abs(int(s[i]) - int(s[i+1]))
		diffEnd := abs(int(s[n-1-i]) - int(s[n-2-i]))

		if diffStart != diffEnd {
			return "Not Funny"
		}
	}

	return "Funny"
}

/*
 * Problem: https://www.hackerrank.com/challenges/gem-stones/problem
 */
func gemstones(arr []string) int32 {
	var occurrences [26]int

	for _, rock := range arr {
		var seenInRock [26]bool

		for _, char := range rock {
			if char >= 'a' && char <= 'z' {
				index := char - 'a'

				if !seenInRock[index] {
					seenInRock[index] = true
					occurrences[index]++
				}
			}
		}
	}

	gems := 0
	totalRocks := len(arr)
	for _, count := range occurrences {
		if count == totalRocks {
			gems++
		}
	}

	return int32(gems)
}

func main() {
	// Problem: camel case
	c := camelcase("saveChangesInTheEditor")
	fmt.Println(c)

	fmt.Println("--------------------------")

	// Problem: Super Reduced String
	fmt.Println(superReducedString("aaabccddd")) // abd
	fmt.Println(superReducedString("aa"))        // Empty String
	fmt.Println(superReducedString("baab"))      // Empty String

	fmt.Println("--------------------------")

	// Problem: Strong Password
	fmt.Println(minimumNumber(3, "Ab1"))          // 3
	fmt.Println(minimumNumber(11, "#HackerRank")) // 1

	fmt.Println("--------------------------")

	// Problem: Weighted Uniform Strings
	fmt.Println(weightedUniformStrings("abccddde", []int32{1, 3, 12, 5, 9, 10}))
	fmt.Println(weightedUniformStrings("aaabbbbcccddd", []int32{9, 7, 8, 12, 5}))

	fmt.Println("--------------------------")

	// Problem: Two Characters
	fmt.Println(alternate("beabeefeab"))                   // 5
	fmt.Println(alternate("aaaa"))                         // 0
	fmt.Println(alternate("asdcbsdcagfsdbgdfanfghbsfdab")) // 8

	fmt.Println("--------------------------")

	// Problem: Caesar Cipher
	fmt.Println(caesarCipher("middle-Outz", 2)) // "okffng-Qwvb"
	fmt.Println(caesarCipher("www.abc.xy", 87)) // fff.jkl.gh

	fmt.Println("--------------------------")

	// Problem: Mars Exploration
	fmt.Println(marsExploration("SOSSPSSQSSOR")) // 3
	fmt.Println(marsExploration("SOSSOSSOS"))    // 0

	fmt.Println("--------------------------")

	// Problem: HackerRank in a String!
	fmt.Println(hackerrankInString("hereiamstackerrank")) // YES
	fmt.Println(hackerrankInString("hackerworld"))        // NO
	fmt.Println(hackerrankInString("hackerrank"))         // YES

	fmt.Println("--------------------------")

	// Problem: Pangrams
	fmt.Println(pangrams("The quick brown fox jumps over the lazy dog"))                 // pangram
	fmt.Println(pangrams("We promptly judged antique ivory buckles for the next prize")) // pangram
	fmt.Println(pangrams("We promptly judged antique ivory buckles for the prize"))      // not pangram

	fmt.Println("--------------------------")

	// Problem: Separate the Numbers
	separateNumbers("1234")         // YES 1
	separateNumbers("91011")        // YES 9
	separateNumbers("99100")        // YES 99
	separateNumbers("999100010001") // NO

	fmt.Println("--------------------------")

	// Problem: Mars Exploration
	fmt.Println(funnyString("acxz")) // Funny
	fmt.Println(funnyString("bcxz")) // Not Funny

	fmt.Println("--------------------------")

	// Problem:
	input1 := []string{"abcdde", "baccd", "eeabg"}
	fmt.Println(gemstones(input1))
	input2 := []string{"aba", "bba", "aabb"}
	fmt.Println(gemstones(input2))

	fmt.Println("--------------------------")
}
