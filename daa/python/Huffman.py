import heapq
from collections import defaultdict, namedtuple

# Define a Huffman Tree Node
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for heap ordering based on frequency
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(frequency):
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Pop two nodes with the lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Merge nodes and add them back to the heap
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

# Function to generate Huffman codes
def generate_codes(node, prefix="", codebook={}):
    if node is None:
        return codebook

    # If leaf node, assign code
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        # Traverse left and right children with updated prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook

# Huffman Encoding Function
def huffman_encoding(data):
    # Calculate frequency of each character
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    # Build Huffman Tree
    root = build_huffman_tree(frequency)

    # Generate Huffman Codes
    huffman_codes = generate_codes(root)

    # Encode data
    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, huffman_codes

# Example usage
data = "this is an example of a huffman tree"
encoded_data, huffman_codes = huffman_encoding(data)

print("Encoded Data:", encoded_data)
print("Huffman Codes:", huffman_codes)
