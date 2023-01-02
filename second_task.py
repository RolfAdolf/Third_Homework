def python_palindrome(s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]


def palindrome(s: str) -> bool:
    n = len(s)

    s = s.lower()

    left = 0
    right = n - 1

    while True:

        while ( left < n ) and ( not s[left].isalnum() ):
            left += 1
        while ( right >= 0 ) and ( not s[right].isalnum() ):
            right -= 1

        if left >= right:
            return True
        elif s[left] != s[right]:
            return False 
        
        left += 1
        right -= 1


# Выбор функции. True - "питонячая" версия.
pth = True

if __name__ == "__main__":
    if pth:
        print( python_palindrome( input() ) )
    else:
        print( palindrome( input() ) )