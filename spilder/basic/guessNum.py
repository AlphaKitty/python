import random


def main(num, random_num):
    if random_num == 0.1:
        random_num = random.randint(0, 1000)
    if int(num) == random_num:
        print("good job!")
    else:
        if int(num) > random_num:
            num = input("try a smaller one:")
            main(num, random_num)
        else:
            num = input("try a bigger one:")
            main(num, random_num)


if __name__ == '__main__':
    t1 = (1, 2, 3, '24', '5')
    print(t1)
    main(input("input a number between 0 to 1000:\n"), 0.1)
