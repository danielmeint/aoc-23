package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	input, err := readInput("input.txt")
	if err != nil {
		log.Fatalf("failed to read input: %v", err)
	}

	// Solution logic goes here
	fmt.Println("Part 1:", solveDay01Part1(input))
	fmt.Println("Part 2:", solveDay01Part2(input))
}

func readInput(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines, scanner.Err()
}

func solveDay01Part1(input []string) int {
	var total int
	for _, line := range input {
		// get the first and last digits
		firstDigit := getFirstDigit(line)
		lastDigit := getLastDigit(line)

		combinedNum := combine(firstDigit, lastDigit)

		total += combinedNum
	}

	return total
}

func solveDay01Part2(input []string) int {
	var total int
	for _, line := range input {
		allDigits := getAllDigits(line)
		firstDigit := allDigits[0]
		lastDigit := allDigits[len(allDigits)-1]

		combinedNum := combine(firstDigit, lastDigit)

		total += combinedNum
	}

	return total

}

func combine(digit int, digit2 int) int {
	return digit*10 + digit2
}

// Part 1
func getFirstDigit(line string) int {
	for _, char := range line {
		// check if the character is a digit
		if char >= '0' && char <= '9' {
			return int(char - '0')
		}
	}
	// if no digit is found, return 0
	return 0
}

func getLastDigit(line string) int {
	// reverse the string and get the first digit
	return getFirstDigit(reverse(line))
}

func reverse(line string) string {
	// convert the string to a rune slice
	runeSlice := []rune(line)
	// reverse the rune slice
	for i, j := 0, len(runeSlice)-1; i < j; i, j = i+1, j-1 {
		runeSlice[i], runeSlice[j] = runeSlice[j], runeSlice[i]
	}
	// convert the rune slice back to a string
	return string(runeSlice)
}

// Part 2
// "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" also count as digits

// put them in an array and convert to numerical value via index
var digitArray = []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

func getAllDigits(line string) []int {
	var digits []int
	lineLength := len(line)
	for i, _ := range line {
		// check if the character is a digit
		if line[i] >= '0' && line[i] <= '9' {
			digits = append(digits, int(line[i]-'0'))
		}
		// check if the character is a letter
		if line[i] >= 'a' && line[i] <= 'z' {
			// check if a digit is found
			for digitIndex, digitString := range digitArray {
				// check if line is long enough to contain the digit
				if i+len(digitString) <= lineLength && line[i:i+len(digitString)] == digitString {
					digits = append(digits, digitIndex+1) // add 1 to the index to get the value
				}
			}
		}
	}
	return digits
}
