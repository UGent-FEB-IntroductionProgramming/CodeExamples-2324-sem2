# Find gcd for integers m and n 
def gcd(m, n):
    gcd = 1
    
    if m % n == 0:
        return n
    
    for k in range((max(m, n) // 2), 0, -1):
        if m % k == 0 and n % k == 0:
            gcd = k
            break
    return gcd
  
def main():   
    # Prompt the user to enter two integers
    m = int(input("Enter first integer: "))
    n = int(input("Enter second integer: "))
    
    print("The greatest common divisor for", m,
        "and", n, "is", gcd(m, n))

main() # Call the main function
