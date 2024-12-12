
def is_decreasing(report, n):
    new_report = report.copy()

    for i in range(n-1):
        if report[i] <= report[i+1] or report[i] - 3 > report[i+1]:
            return False
    return True
    
def is_increasing(report, n):
    new_report = report.copy()
    for i in range(n-1):
        if report[i] >= report[i+1] or report[i] < report[i+1] - 3:
            return False

                
    return True

def main():
    read = open("input1")
    reports= read.readlines()
    sum = 0
    
    for report in reports:
        report = list(map(int, report.split(" ")))
        n = len(report)
        if report[0] > report[1]:
            sum += is_decreasing(report, n)
        elif report[0] < report[1]:
            sum += is_increasing(report, n)
    print(sum)

if __name__ == "__main__":
    main()