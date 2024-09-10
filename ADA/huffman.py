import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_code_tree(node, binary_string='', code_dict=None):
    if code_dict is None:
        code_dict = {}
        
    if node is None:
        return
    
    if node.left is None and node.right is None:
        code_dict[node.char] = binary_string
    
    huffman_code_tree(node.left, binary_string + '0', code_dict)
    huffman_code_tree(node.right, binary_string + '1', code_dict)
    
    return code_dict

def huffman_encoding(frequencies):
    heap = []
    
    for char, freq in frequencies.items():
        heapq.heappush(heap, Node(char, freq))
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    root = heapq.heappop(heap)
    huffman_codes = huffman_code_tree(root)
    
    return huffman_codes

def calculate_total_bits(huffman_codes, frequencies):
    total_bits = 0
    for char, code in huffman_codes.items():
        total_bits += len(code) * frequencies[char]
    return total_bits

def get_user_input():
    frequencies = {}
    num_chars = int(input("Enter the number of unique characters: "))
    for _ in range(num_chars):
        char = input("Enter the character: ")
        freq = int(input(f"Enter the frequency of '{char}': "))
        frequencies[char] = freq
    return frequencies

if __name__ == "__main__":
    frequencies = get_user_input()
    
    huffman_codes = huffman_encoding(frequencies)
    
    print("\nCharacter with corresponding Huffman codes:")
    for char, code in huffman_codes.items():
        print(f"'{char}': {code}")
    
    total_bits = calculate_total_bits(huffman_codes, frequencies)
    print(f"\nTotal bits used: {total_bits}")
