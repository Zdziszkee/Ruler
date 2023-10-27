def draw_ruler(length):
    if 1 > length > 1000:
        print("Długość miarki musi być większa niż 0 i mniejsza od 1000")
        return
    scale = "|"
    numbers = "0"
    seperator = "     "
    for i in range(1, length + 1):
        scale += "....|"
        number = str(i)
        numbers += seperator[:-(len(number))] + number
    # Wyświetlanie miarki
    print(scale)
    print(numbers)
draw_ruler(15)
