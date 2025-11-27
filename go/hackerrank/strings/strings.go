package main

import (
	"fmt"
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
}
