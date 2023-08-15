import sys
input = lambda: sys.stdin.readline().rstrip()

class Node:
 
    def __init__(self, data):
 
        self.data = data
         
        # left node for 0
        self.left = None
         
        # right node for 1
        self.right = None
 
# Class for implementing Trie
class Trie:
 
    def __init__(self):
 
        self.root = Node(0)
 
    # Insert pre_xor to trie with given root
    def insert(self, pre_xor):
 
        self.temp = self.root
 
        # Start from msb, insert all bits of pre_xor
        # into the Trie
        for i in range(31, -1, -1):
 
            # Find current bit in prefix sum
            val = pre_xor & (1<<i)
 
            if val :
                 
                # Create new node if needed
                if not self.temp.right:
                    self.temp.right = Node(0)
                self.temp = self.temp.right
 
            if not val:
                 
                # Create new node if needed
                if not self.temp.left:
                    self.temp.left = Node(0)
                self.temp = self.temp.left
 
        # Store value at leaf node
        self.temp.data = pre_xor
 
    # Find the maximum xor ending with last number
    # in prefix XOR and return the XOR of this
    def query(self, xor):
 
        self.temp = self.root
 
        for i in range(31, -1, -1):
 
            # Find the current bit in prefix xor
            val = xor & (1<<i)
 
            # Traverse the trie, first look for opposite bit
            # and then look for same bit
            if val:
                if self.temp.left:
                    self.temp = self.temp.left
                elif self.temp.right:
                    self.temp = self.temp.right
            else:
                if self.temp.right:
                    self.temp = self.temp.right
                elif self.temp.left:
                    self.temp = self.temp.left
 
        return xor ^ self.temp.data
 
    # Returns maximum XOR value of subarray
    def maxSubArrayXOR(self, n, Arr):
 
        # Insert 0 in the trie
        self.insert(0)
 
        # Initialize result and pre_xor
        result = -float('inf')
        pre_xor = 0
 
        # Traverse all input array element
        for i in range(n):
 
            # Update current prefix xor and
            # insert it into Trie
            pre_xor = pre_xor ^ Arr[i]
            self.insert(pre_xor)
 
            # Query for current prefix xor
            # in Trie and update result
            result = max(result, self.query(pre_xor))
 
        return result
 
# Driver code
if __name__ == "__main__":
 
    for aa in range(int(input())):
        n=int(input())
        # n,m=map(int,input().split())
        li=list(map(int,input().split()))
        trie = Trie()
        print(trie.maxSubArrayXOR(n, li))

