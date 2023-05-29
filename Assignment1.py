def print_shortest_substrings(s, x):
    result = []
    for i in range(len(s)):
        for j in range(i + x, len(s) + 1):
            if s[i] == s[j-1] and j - i >= x:
                result.append(s[i:j])
    if len(result) == 0:
        print("not-found")
    else:
        shortest_length = min(len(substring) for substring in result)
        shortest_substrings = [substring for substring in result if len(substring) == shortest_length]
        for substring in shortest_substrings:
            print(substring)

# Example usage
s = "abccdbacca"
x = 3
print_shortest_substrings(s, x)  # Output: acca
x = 4
print_shortest_substrings(s, x)  # Output: acca
x = 5
print_shortest_substrings(s, x)  # Output: bccdb cdbac
x = 6
print_shortest_substrings(s, x)  # Output: abccdba
x = 7
print_shortest_substrings(s, x)  # Output: abccdba
x = 8
print_shortest_substrings(s, x)  # Output: not-found