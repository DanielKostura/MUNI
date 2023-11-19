def oneElement(left, right, znak, n, s):
    if left == n and right == n:
        s.add(znak)
    
    if left > right:
        znak += ")"
        oneElement(left, right+1, znak, n, s)
        znak = znak[:-1]

    if n > left:
        znak += "("
        oneElement(left+1, right, znak, n, s)

    return s
    
    

def generateParenthesis(n: int) -> set[str]:
    s = set()
    s = oneElement(0, 0, "", n, s)
    return s


print(generateParenthesis(1)) # {'()'}
print(generateParenthesis(2)) # {'()()', '(())'}
print(generateParenthesis(3)) # {'()()()','(())()','()(())','(()())', '((()))'}