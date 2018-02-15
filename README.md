# Gene Splicing
Objective: Given two strings representing snippets of genes (letters ACGT), identify the shortest string that could contain them both as subsequences.

## How to Run:
1. Run the file in IDLE
2. Input gene snippets as directed

## Python Version
Python 3.6.0

## Efficiency
The program is efficient in a few ways:
1. We utilize if-else statements to check for string validity before proceeding.
2. We do not use recursion as we realized that we are most interested in superstring matches that preserve the order of characters in original strings X and Y (this means that, say X = "ATGGGTTT" and Y = "GATATGGGCCC", and even though we find that the substring "GGG" is present in the middle of both X and Y we will not merge, but instead concatenate X and Y. So we don't waste time considering this case). To do that, we look for a length-k suffix of X that matches a length-k prefix of Y with k as the longest possible length an overlap between X and Y could be. 

## Edge Cases Addressed:
* User inputs invalid strings: Empty strings and non-string character are not allowed. User will be prompted to input valid strings.
* All shortest superstrings of the same length are printed.

## Project Collaborators:
Mai Ngo, Sherri Lin

### Note:
The project can be found on [Github](https://github.com/crystallistic/csc220-coding-challenge-2).
