import time

# Naive string matching algorithm
def naive_string_matching(text, pattern):
    """Naive string matching algorithm implementation."""
    n = len(text)
    m = len(pattern)
    matches = []
    
    for i in range(n - m + 1):
        # Check for pattern match
        if text[i:i + m] == pattern:
            matches.append(i)  # Store the starting index of the match

    return matches

# Rabin-Karp algorithm
def rabin_karp(text, pattern, d=256, q=101):
    """Rabin-Karp string matching algorithm implementation."""
    n = len(text)
    m = len(pattern)
    matches = []

    # Compute hash values for pattern and first window of text
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    h = 1

    # The value of h would be "pow(d, m-1)%q"
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate the hash value for pattern and text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check the hash values of current window of text and pattern
        if p == t:
            # Check for characters one by one
            if text[i:i + m] == pattern:
                matches.append(i)  # Store the starting index of the match

        # Calculate hash value for next window of text
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            # We might get negative value of t, converting it to positive
            if t < 0:
                t += q

    return matches

def main():
    # Input from user
    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search for: ")

    # Naive String Matching
    start_time = time.time()
    naive_matches = naive_string_matching(text, pattern)
    naive_time = time.time() - start_time
    print("\nNaive String Matching Results:")
    print(f"Pattern found at indices: {naive_matches}")
    print(f"Time taken (Naive): {naive_time:.6f} seconds")

    # Rabin-Karp Algorithm
    start_time = time.time()
    rabin_matches = rabin_karp(text, pattern)
    rabin_time = time.time() - start_time
    print("\nRabin-Karp Algorithm Results:")
    print(f"Pattern found at indices: {rabin_matches}")
    print(f"Time taken (Rabin-Karp): {rabin_time:.6f} seconds")

if __name__ == "__main__":
    main()
