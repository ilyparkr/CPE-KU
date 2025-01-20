def main():
    lap = 0
    total = 0
    while True:
        print(f"Rectangle No. {lap+1}")
        sym = input("Input Symbol : ")
        if sym == '':
            print(f"Totally, {total} Rectangles.")
            print('')
            return
        else:
            row = int(input("Input row: "))
            col = int(input("Input col: "))
            for _ in range(col):
                print(sym*row)
            lap += 1
            total += 1
            print('')
main()