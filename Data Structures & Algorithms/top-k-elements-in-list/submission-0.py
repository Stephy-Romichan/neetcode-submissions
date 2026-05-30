class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        out = []
        
        # 1. Count ALL frequencies ONCE outside the while loop
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            
        # 2. Loop k times to find the top k elements
        while k > 0:
            # Find the key (number) with the maximum value (frequency)
            max_num = max(freq, key=freq.get)
            
            # Append that number to your output
            out.append(max_num)
            
            # Delete it from the dictionary so the next loop finds the NEXT highest
            del freq[max_num]
            
            k -= 1
            
        return out
