def generateParenthesis(n: int) -> set[int]:
    parens = set()
    return generate('', n, n, parens)


def generate(p: int, left: int, right: int, parens: set[int]) -> set[int]:
    if left:
        generate(p + '(', left-1, right, parens)
    if right > left:
        generate(p + ')', left, right-1, parens)
    if not right:
        parens.add(p)
    return parens

print(generateParenthesis(1)) # {'()'}
print(generateParenthesis(2)) # {'()()', '(())'}
print(generateParenthesis(3)) # {'()()()','(())()','()(())','(()())', '((()))'}