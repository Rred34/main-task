import sys

def circular_path(n, m):
    path = []
    start = 1  
    
    while True:
        path.append(start)
        
        
        end = (start + m - 1) % n
        if end == 0:
            end = n

        start = end
        
        
        if start == 1:
            break
    
    return path

def main():
    if len(sys.argv) != 5:
        print("Использование: python task1.py n1 m1 n2 m2")
        sys.exit(1)

    n1, m1, n2, m2 = map(int, sys.argv[1:5])
    path1 = circular_path(n1, m1)
    path2 = circular_path(n2, m2)
    print(''.join(map(str, path1)) + ''.join(map(str, path2)))

if __name__ == "__main__":
    main()