import sys
ss = list(sys.argv[1])
numRows = int(sys.argv[2])

slist = []
count = 0
while len(ss):
    # 縦
    if count%2 == 0:
        moji = ss[:numRows]
        if len(ss) != numRows:
            slist.append(ss[:numRows] + [" "]*(numRows-len(ss)))
        else: 
            slist.append(ss[:numRows])
        del ss[:numRows]
    # 斜め
    else:
        end = numRows-2
        for i in range(1,end+1):
            if len(ss) != 0:
                slist.append([" "]*(numRows-i-1) + ss[:1] + [" "]*(i))
                del ss[:1]
    count+=1

for i in range(numRows):
    for j in slist:
        print(j[i],end = "")
    print()
