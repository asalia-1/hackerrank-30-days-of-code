# Enter your code here. Read input from STDIN. Print output to STDOUT
tests = input()


for num in range(int(tests)):
    even_str = ""
    odd_str = ""

    some_string = input()
    for i in range(len(some_string)):
        if i % 2 == 0:
            even_str += some_string[i]
        else:
            odd_str += some_string[i]

    print(even_str, odd_str)
