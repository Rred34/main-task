import sys

def main():
    
    if len(sys.argv) < 3:
        print("Usage: python task2.py <circle_file> <dot_file>")
        sys.exit(1)
    
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]
    
    try:
        with open(ellipse_file, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        
        if len(lines) < 2:
            print("Error: ellipse file must contain at least 2 lines")
            sys.exit(1)
        
        x0, y0 = map(float, lines[0].split())
        rx, ry = map(float, lines[1].split())
        if rx <= 0 or ry <= 0:
            print("Error: ellipse radii must be positive")
            sys.exit(1)

        with open(points_file, 'r') as f:
            points = []
            for line in f:
                line = line.strip()
                if line:
                    x, y = map(float, line.split())
                    points.append((x, y))
        
        if not 1 <= len(points) <= 100:
            print("Error: number of points must be between 1 and 100")
            sys.exit(1)

        EPS = 1e-10
        for x, y in points:
            
            dx = x - x0
            dy = y - y0
            value = (dx * dx) / (rx * rx) + (dy * dy) / (ry * ry)
            
            
            if abs(value - 1) < EPS:
                print(0)
            elif value < 1:
                print(1)
            else:
                print(2)
                
    except FileNotFoundError:
        print("Error: file not found")
        sys.exit(1)
    except ValueError:
        print("Error: invalid number format")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()