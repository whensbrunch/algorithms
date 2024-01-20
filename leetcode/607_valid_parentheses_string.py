def valid_parentheses(s: str) -> bool:
    print(f'Running {s}')
    left_max = left_min = 0
    for c in s:
        if c == "(":
            left_min += 1
            left_max += 1
        elif c == ")":
            left_min -= 1
            left_max -= 1
        else:
            left_min -= 1
            left_max += 1
        if left_max < 0:  
            # there's no way we could make the string valid in the best case
            return False
        if left_min < 0:
            # the string up to index_c must remain valid (i.e. go negative)
            # we can choose to have the star be the empty string instead and have left_min remain 0
            left_min = 0
        print(f"-> left min: {left_min}, left max: {left_max}")
    print(f'-> result: {left_max >= 0 and left_min <= 0}')  
    return left_max >= 0 and left_min <= 0

print("Test cases:")
test_cases = (
    '(*)',
    '((*)',
    '(**)',
    '(*))',
    '(*)))',
    '(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())'
)
for s in test_cases:
    valid_parentheses(s)


