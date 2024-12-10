def safetyReport(report:list) -> bool:
    if report[0]>report[1]: #descending
        i=1
        safe=1
        while i<len(report) and safe:
            if abs(report[i]-report[i-1])<=3 and report[i]<report[i-1]:
                i+=1
            else:
                safe=0
    else:
        i=1
        safe=1
        while i<len(report) and safe:
            if abs(report[i]-report[i-1])<=3 and report[i]>report[i-1]:
                i+=1
            else:
                safe=0
    return safe


if __name__ == '__main__':
    with open('Input02.txt') as f:
        arrayRaw = f.readlines()
        
numbersString = [ x.replace("\n","").split(" ") for x in arrayRaw]

reports = [[float(level) for level in report] for report in numbersString]

#First star
safeReport = 0
for r in reports:
    safe = safetyReport(r)
    if safe:
        safeReport += 1
        
print(safeReport)

#First star variant
safeReport = list(filter(safetyReport, reports))
print(len(safeReport))

#Second star
safeReport = 0
for r in reports:
    safe = safetyReport(r)
    if safe:
        safeReport += 1
    i = 0
    while i<len(r) and not safe:
        if i==0:
            safe = safetyReport(r[1:])
        elif i==len(r)-1:
            safe = safetyReport(r[:len(r)-1])
        else:
            safe = safetyReport(r[0:i]+r[i+1:])
        
        if safe:
            safeReport += 1
        else:
            i += 1
            
print(safeReport)
