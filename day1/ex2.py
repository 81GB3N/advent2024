
def main():
    read = open("input1")
    input= read.readlines()
    freq = {}
    list_left = []
    
    for line in input:
        line = line.split("   ")
        value = int(line[0])
        list_left.append(value)
        key = int(line[1])
        if key in freq:
            freq[key] += 1
        else:
            freq[key] = 1
        
    sum = 0
    for item in list_left:
        if item in freq:
            sum += item * freq[item]
    print(sum)

if __name__ == "__main__":
    main()