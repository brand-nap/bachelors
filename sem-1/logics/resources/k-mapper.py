def main():
    int_list = [];
    for i in range(16):
        int_list.append(int(input(f'{i}: ')));

    print(f'\n{int_list[0]} {int_list[1]} {int_list[3]} {int_list[2]}');
    print(f'{int_list[4]} {int_list[5]} {int_list[7]} {int_list[6]}');
    print(f'{int_list[12]} {int_list[13]} {int_list[15]} {int_list[14]}');
    print(f'{int_list[8]} {int_list[9]} {int_list[11]} {int_list[10]}');

main()
