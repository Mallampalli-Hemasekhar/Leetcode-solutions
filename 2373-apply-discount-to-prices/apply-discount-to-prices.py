class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        word=sentence.split()
        result=[]
        for w in word:
            if w.startswith('$') and len(w) > 1 and w[1:].isdigit():
                price = int(w[1:])
                discounted = price * (100 - discount) / 100
              
                result.append(f"${discounted:.2f}")
            else:
                result.append(w)
        
        return " ".join(result)