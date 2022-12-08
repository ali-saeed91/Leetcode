class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        print(dominoes)
        out =""
        while dominoes != out:
            out = dominoes
            dominoes = dominoes.replace("R.L", "nnn")
            dominoes = dominoes.replace("R.", "RR")
            dominoes = dominoes.replace(".L", "LL")
        dominoes = dominoes.replace("nnn","R.L")
        return (dominoes)
        