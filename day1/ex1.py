
def main():
    read = open("input1")
    input= read.readlines()
    list_left= []
    list_right = []
    
    for line in input:
        line = line.split("   ")
        # print(line)
        list_left.append(int(line[0]))
        list_right.append(int(line[1]))
        list_left = sorted(list_left)
        list_right = sorted(list_right)
        
    n = len(list_left)
    sum = 0
    for i in range(n):
        sum += abs(list_left[i] - list_right[i])
    print(sum)

if __name__ == "__main__":
    main()