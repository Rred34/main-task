import sys

def min_moves_to_equal_elements(nums, max_moves=20):
    if len(nums) == 0:
        return 0, 
    
    nums_sorted = sorted(nums)
    n = len(nums_sorted)
    if n % 2 == 1:
        median = nums_sorted[n // 2]
       
        moves = sum(abs(num - median) for num in nums)
        
        if moves <= max_moves:
            return moves, f"{moves}"
        else:
            return None, f"{max_moves} ходов недостаточно для приведения всех элементов массива к одному числу"
    else:
        
        median1 = nums_sorted[n // 2 - 1]
        median2 = nums_sorted[n // 2]
        
        moves1 = sum(abs(num - median1) for num in nums)
        moves2 = sum(abs(num - median2) for num in nums)
        
        moves = min(moves1, moves2)
        
        if moves <= max_moves:
            return moves, f"{moves}"
        else:
            
            min_moves = float('inf')
            best_target = None
            
            for target in range(median1, median2 + 1):
                current_moves = sum(abs(num - target) for num in nums)
                if current_moves < min_moves:
                    min_moves = current_moves
                    best_target = target
            
            if min_moves <= max_moves:
                return min_moves, f"{min_moves}"
            else:
                return None, f"{max_moves} ходов недостаточно для приведения всех элементов массива к одному числу"

def read_array_from_file(filename):
    nums = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:  
                    try:
                        nums.append(int(line))
                    except ValueError:
                        print(f"Предупреждение: строка '{line}' не является целым числом, пропускаем")
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)
    
    return nums

def main():
    if len(sys.argv) < 2:
        print("Использование: python task4.py <имя_файла>")
        print("Пример: python task4.py numbers.txt")
        sys.exit(1)
    filename = sys.argv[1]
    nums = read_array_from_file(filename)
    
    if not nums:
        print("Файл не содержит чисел или пуст")
        sys.exit(1)
    
    
    result, message = min_moves_to_equal_elements(nums)
    
    print(message)

if __name__ == "__main__":
    main()