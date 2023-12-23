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
	fmt.Println("Part 1:", solveDay08Part1(input))
	fmt.Println("Part 2:", solveDay08Part2(input))
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

func solveDay08Part1(input []string) int {
	// first line contains steps
	steps := input[0]

	// second line should be empty
	if input[1] != "" {
		log.Fatalf("expected empty line after steps")
	}

	// remaining lines contain nodes of the graph to be built
	graph := buildGraph(input[2:])

}

// each graph node has a left and right child
type node struct {
	name  string
	left  *node
	right *node
}

func buildGraph(input []string) map[string]*node {
	// each line is of the form: LNL = (QBG, JKT)
	// where LNL is the parent node, QBG and JKT are the children
	// and the line is saying that QBG is the left child and JKT is the right child
	// so we need to parse each line and build the graph
	graph := make(map[string]*node)
	for _, line := range input {

	}

}

func solveDay08Part2(input []string) int {

}
