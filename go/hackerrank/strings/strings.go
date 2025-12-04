package main

import (
	"fmt"
	"math"
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

/*
 * Problem: https://www.hackerrank.com/challenges/alternating-characters/problem
 */
func alternatingCharacters(s string) int32 {
	var deletions int32

	for i := 0; i < len(s)-1; i++ {
		if s[i] == s[i+1] {
			deletions++
		}
	}

	return deletions
}

/*
 * Problem: https://www.hackerrank.com/challenges/beautiful-binary-string/problem
 */
func beautifulBinaryString(b string) int32 {
	return int32(strings.Count(b, "010"))
}

/*
 * Problem: https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
 */
func theLoveLetterMystery(s string) int32 {
	count := 0
	left := 0
	right := len(s) - 1

	for left < right {
		diff := int(s[left]) - int(s[right])

		// Get absolute value
		if diff < 0 {
			diff = -diff
		}

		count += diff

		// Move pointers towards the center
		left++
		right--
	}

	return int32(count)
}

/*
 * Problem: https://www.hackerrank.com/challenges/palindrome-index/problem
 */
func palindromeIndex(s string) int32 {
	isPalindrome := func(s string, left, right int) bool {
		for left < right {
			if s[left] != s[right] {
				return false
			}
			left++
			right--
		}
		return true
	}

	left := 0
	right := len(s) - 1

	for left < right {
		if s[left] != s[right] {
			if isPalindrome(s, left+1, right) {
				return int32(left)
			}
			if isPalindrome(s, left, right-1) {
				return int32(right)
			}
			// Neither works, so it's not possible by removing just one char.
			return -1
		}
		left++
		right--
	}

	// If we went through the whole loop, it's already a palindrome.
	return -1
}

/*
 * Problem: https://www.hackerrank.com/challenges/anagram/problem
 */
func anagram(s string) int32 {
	n := len(s)

	// If the length is odd, we cannot split it into two equal substrings.
	if n%2 != 0 {
		return -1
	}

	mid := n / 2

	var counts [26]int

	for i := range mid {
		counts[s[i]-'a']++
	}

	for i := mid; i < n; i++ {
		counts[s[i]-'a']--
	}

	changes := 0
	for _, diff := range counts {
		if diff > 0 {
			changes += diff
		}
	}

	return int32(changes)
}

/*
 * Problem: https://www.hackerrank.com/challenges/making-anagrams/problem
 */
func makingAnagrams(s1, s2 string) int32 {
	var counts [26]int

	for _, char := range s1 {
		counts[char-'a']++
	}

	for _, char := range s2 {
		counts[char-'a']--
	}

	deletions := 0
	for _, diff := range counts {
		if diff < 0 {
			deletions += -diff
		} else {
			deletions += diff
		}
	}

	return int32(deletions)
}

/*
 * Problem: https://www.hackerrank.com/challenges/game-of-thrones/problem
 */
func gameOfThrones(s string) string {
	var counts [26]int

	for _, char := range s {
		if char >= 'a' && char <= 'z' {
			counts[char-'a']++
		}
	}

	oddCount := 0
	for _, freq := range counts {
		// Use bitwise check for odd numbers (freq & 1)
		if freq&1 == 1 {
			oddCount++
		}
	}

	if oddCount > 1 {
		return "NO"
	}
	return "YES"
}

/*
 * Problem: https://www.hackerrank.com/challenges/two-strings/problem
 */
func twoStrings(s1, s2 string) string {
	var seen [26]bool

	for _, char := range s1 {
		if char >= 'a' && char <= 'z' {
			seen[char-'a'] = true
		}
	}

	for _, char := range s2 {
		if char >= 'a' && char <= 'z' {
			if seen[char-'a'] {
				return "YES"
			}
		}
	}

	return "NO"
}

/*
 * Problem: https://www.hackerrank.com/challenges/string-construction/problem
 */
func stringConstruction(s string) int32 {
	var seen [26]bool
	uniqueCount := 0

	for _, char := range s {
		idx := char - 'a'
		if !seen[idx] {
			seen[idx] = true
			uniqueCount++
		}
	}

	return int32(uniqueCount)
}

/*
 * Problem: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
 */
func isValid(s string) string {
	var charCounts [26]int
	for _, char := range s {
		if char >= 'a' && char <= 'z' {
			charCounts[char-'a']++
		}
	}

	// Count the frequency of those frequencies
	freqCounts := make(map[int]int)
	for _, count := range charCounts {
		if count > 0 {
			freqCounts[count]++
		}
	}

	if len(freqCounts) == 1 {
		return "YES"
	}

	// If there are more than 2 different frequencies, we can't fix it by removing just 1 char.
	if len(freqCounts) > 2 {
		return "NO"
	}

	var keys []int
	for k := range freqCounts {
		keys = append(keys, k)
	}

	f1, f2 := keys[0], keys[1]
	count1, count2 := freqCounts[f1], freqCounts[f2]

	// One of the frequencies is 1, and it occurs exactly once.
	if (f1 == 1 && count1 == 1) || (f2 == 1 && count2 == 1) {
		return "YES"
	}

	// The frequencies differ by exactly 1, and the higher frequency occurs exactly once.
	diff := int(math.Abs(float64(f1 - f2)))
	if diff == 1 {
		// Find which frequency is the larger one
		maxFreqCount := count1
		if f2 > f1 {
			maxFreqCount = count2
		}

		if maxFreqCount == 1 {
			return "YES"
		}
	}

	return "NO"
}

/*
 * Problem: https://www.hackerrank.com/challenges/richie-rich/problem
 */
func highestValuePalindrome(s string, n int32, k int32) string {
	chars := []byte(s)
	length := int(n)
	left := 0
	right := length - 1

	mismatches := make([]bool, length)

	for left < right {
		if chars[left] != chars[right] {
			maxChar := chars[left]
			if chars[right] > maxChar {
				maxChar = chars[right]
			}

			chars[left] = maxChar
			chars[right] = maxChar
			mismatches[left] = true // Mark that we spent 1 'k' here
			k--
		}
		left++
		right--
	}

	// If k is negative, it wasn't possible to make a palindrome even with min changes
	if k < 0 {
		return "-1"
	}

	// Second pass: Use remaining k to maximize the value (change to '9')
	left = 0
	right = length - 1

	for left <= right {
		if left == right {
			if k > 0 {
				chars[left] = '9'
			}
		} else {
			if chars[left] != '9' {
				// If this index was a mismatch we fixed in pass 1:
				// We already deducted 1 'k'. To make them '9', we need to change them again.
				// This effectively costs 1 *additional* k (total 2 for this pair, but 1 already paid).
				if mismatches[left] {
					if k >= 1 {
						chars[left] = '9'
						chars[right] = '9'
						k--
					}
				} else {
					// If this pair was originally matching (not '9'):
					// We need to change both to '9', costing 2 'k'.
					if k >= 2 {
						chars[left] = '9'
						chars[right] = '9'
						k -= 2
					}
				}
			}
		}
		left++
		right--
	}

	return string(chars)
}

/*
 * Problem: https://www.hackerrank.com/challenges/maximum-palindromes/problem
 */
const (
	MOD   = 1000000007
	LIMIT = 100005 // Max length of string s is 10⁵
)

var (
	// Precomputed factorials and modular inverse factorials
	fact    [LIMIT]int64
	invFact [LIMIT]int64
	// Prefix sum array for character frequencies: freq[char][index]
	freq [26][LIMIT]int32
)

// initialize precomputes factorials and prefix sums for the input string.
func initialize(s string) {
	// power calculates (base^exp) % MOD efficiently.
	power := func(base, exp int64) int64 {
		var res int64 = 1
		base %= MOD
		for exp > 0 {
			if exp%2 == 1 {
				res = (res * base) % MOD
			}
			base = (base * base) % MOD
			exp /= 2
		}
		return res
	}

	n := len(s)

	// Precompute Factorials and Inverse Factorials
	fact[0] = 1
	invFact[0] = 1

	for i := 1; i <= n; i++ {
		fact[i] = (fact[i-1] * int64(i)) % MOD
	}
	// Compute modular inverse of n! using Fermat's Little Theorem
	invFact[n] = power(fact[n], MOD-2)
	// Compute remaining inverses backwards
	for i := n - 1; i >= 1; i-- {
		invFact[i] = (invFact[i+1] * int64(i+1)) % MOD
	}

	// Prefix Sums for character frequencies
	// We iterate 1-based to make range calculations easier (r - (l-1))
	for i := range n {
		charIndex := s[i] - 'a'
		for c := range 26 {
			// Copy previous value
			freq[c][i+1] = freq[c][i]
		}
		freq[charIndex][i+1]++
	}
}

func answerQuery(l, r int32) int32 {
	var odds int32
	var totalPairs int32
	var denominators int64 = 1

	// Iterate over all alphabets to find counts in the range [l, r]
	for c := range 26 {
		count := freq[c][r] - freq[c][l-1]

		pairs := count / 2
		remainder := count % 2

		totalPairs += pairs
		odds += remainder

		// If we have pairs, they contribute to the denominator of the multinomial coefficient
		if pairs > 0 {
			denominators = (denominators * invFact[pairs]) % MOD
		}
	}

	// Formula: (TotalPairs! / (pairA! * pairB! * ...)) * max(1, oddCounts)

	// Calculate numerator: TotalPairs!
	numerator := fact[totalPairs]

	// Calculate permutations of the halves
	permutations := (numerator * denominators) % MOD

	// Multiply by the number of choices for the center character
	// If there are no odd characters, we don't multiply (or multiply by 1)
	centerOptions := int64(odds)
	if centerOptions == 0 {
		centerOptions = 1
	}

	result := (permutations * centerOptions) % MOD
	return int32(result)
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

	// Problem: Gemstones
	input1 := []string{"abcdde", "baccd", "eeabg"}
	fmt.Println(gemstones(input1))
	input2 := []string{"aba", "bba", "aabb"}
	fmt.Println(gemstones(input2))

	fmt.Println("--------------------------")

	// Problem: Alternating Characters
	fmt.Println(alternatingCharacters("AAAA"))     // 3
	fmt.Println(alternatingCharacters("BBBBB"))    // 4
	fmt.Println(alternatingCharacters("ABABABAB")) // 0
	fmt.Println(alternatingCharacters("AAABBB"))   // 4

	fmt.Println("--------------------------")

	// Problem: Alternating Characters
	fmt.Println(beautifulBinaryString("0101010"))    // 2
	fmt.Println(beautifulBinaryString("01100"))      // 0
	fmt.Println(beautifulBinaryString("0100101010")) // 3

	fmt.Println("--------------------------")

	// Problem: The Love-Letter Mystery
	fmt.Println(theLoveLetterMystery("abc"))   // 2
	fmt.Println(theLoveLetterMystery("abcba")) // 0
	fmt.Println(theLoveLetterMystery("abcd"))  // 4

	fmt.Println("--------------------------")

	// Problem: Palindrome Index
	fmt.Println(palindromeIndex("aaab")) // 3
	fmt.Println(palindromeIndex("baa"))  // 0
	fmt.Println(palindromeIndex("bcbc")) // 0

	fmt.Println("--------------------------")

	// Problem: Anagram
	fmt.Println(anagram("aaabbb")) // 3
	fmt.Println(anagram("ab"))     // 1
	fmt.Println(anagram("abc"))    // -1
	fmt.Println(anagram("mnop"))   // 2

	fmt.Println("--------------------------")

	// Problem: Making Anagrams
	fmt.Println(makingAnagrams("cde", "abc"))                                            // 4
	fmt.Println(makingAnagrams("absdjkvuahdakejfnf", "djfladfhiawasdkjvalskufhafkjnsd")) // 17

	fmt.Println("--------------------------")

	// Problem: Game of Thrones - I
	fmt.Println(gameOfThrones("aaabbbb"))           // YES
	fmt.Println(gameOfThrones("cdefghmnopqrstuvw")) // NO
	fmt.Println(gameOfThrones("cdcdcdcdeeeef"))     // YES

	fmt.Println("--------------------------")

	// Problem: Two Strings
	fmt.Println(twoStrings("hello", "world"))    // YES
	fmt.Println(twoStrings("hi", "world"))       // NO
	fmt.Println(twoStrings("aardvark", "apple")) // YES

	fmt.Println("--------------------------")

	// Problem: String Construction
	fmt.Println(stringConstruction("abcd")) // 4
	fmt.Println(stringConstruction("abab")) // 2

	fmt.Println("--------------------------")

	// Problem: Sherlock and the Valid String
	fmt.Println(isValid("aabbccddeefghi"))    // NO
	fmt.Println(isValid("abcdefghhgfedecba")) // YES

	fmt.Println("--------------------------")

	// Problem: Highest Value Palindrome
	fmt.Println(highestValuePalindrome("3943", 4, 1))   // "3993"
	fmt.Println(highestValuePalindrome("092282", 6, 3)) // "992299"
	fmt.Println(highestValuePalindrome("0011", 4, 1))   // "-1"

	fmt.Println("--------------------------")
}
