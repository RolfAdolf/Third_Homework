def binary_system(num: int) -> str:
    if (num // 2 == 0):
        return num % 2
    
    return binary_system(num // 2) * 10 + num % 2


if __name__ == "__main__":
    print( binary_system( int( input() ) ) )