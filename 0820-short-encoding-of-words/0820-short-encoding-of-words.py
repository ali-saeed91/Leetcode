class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        encode = sorted(words, key = len, reverse = True)
        sub =""
        for i in encode:
            if i+'#' not in sub:
                sub += i+'#'
                
        return(len(sub))
                