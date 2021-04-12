if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple([i for i in integer_list])))