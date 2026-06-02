class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstring = ""
        for string in strs:
            lenstr = len(string)
            encodedstring += str(lenstr)+"#"+string
        print(encodedstring)
        return encodedstring
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        lenstr = len(s)

        while i < lenstr:
            # Scan forward to find '#', capturing full length (handles 10+)
            j = i
            while s[j] != '#':
                j += 1
        
            word_len = int(s[i:j])   # e.g. "10" not just "1"
            word = s[j+1 : j+1+word_len]
            decoded_list.append(word)
            i = j + 1 + word_len     # advance past '#' and the word

        return decoded_list
        
