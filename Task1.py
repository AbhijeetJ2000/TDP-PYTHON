def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    return length*width

if __name__ == '__main__':
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = calculate_area(length, width)
    print(area)


