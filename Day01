if __name__ == '__main__':
    with open('Input1.txt') as f:
        arrayRaw = f.readlines()
        
numbersString = [ x.replace("\n","").split("   ") for x in arrayRaw]

list1 = [float(x[0]) for x in numbersString]
list2 = [float(x[1]) for x in numbersString]

list1 = sorted(list1)
list2 = sorted(list2)

#First star
tot=0
for i in range(len(list1)):
    tot+=abs(list1[i]-list2[i])
    
print(tot)

#Second star
count = [0]*len(list1)
curr2 = 0
for i in range(len(list1)):
    found = 0
    while curr2<len(list2) and not found:
        if i>0 and list1[i] < list2[curr2] and list1[i] == list1[i-1]:
            count[i] == count[i-1]
            found =1
        if list1[i] == list2[curr2]:
            count[i] += 1
            curr2 +=1
        elif list1[i] > list2[curr2]:
            curr2 += 1
        else:
            found = 1

tot = 0
for i in range(len(list1)):
    tot += list1[i]*count[i]
    
print(tot)

