

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs ={}
        freqt ={}
        for i in s:
            freqs[i]=freqs.get(i,0)+1
        for j in t:
            freqt[j]=freqt.get(j,0)+1
        if freqs==freqt:
            print(freqs,freqt)
            return True
        else:
            print(freqs,freqt)
            return False
                        



        