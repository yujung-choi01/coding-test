A, B, C = map(int, input().split())

def calculate(a, b, c):
    if b == 1:
        return a % c
    
    half = calculate(a, b // 2, c)
    half_squared = (half * half) % c
    
    if b % 2 == 0:
        return half_squared
    else:
        return (half_squared * a) % c

print(calculate(A, B, C))