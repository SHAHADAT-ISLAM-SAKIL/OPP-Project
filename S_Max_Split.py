def max_split(s):
    newstr=[]
    curstr = ""
    count  = 0
    for num in s:
        curstr += num
        if num == 'R':
            count += 1
        else :
            count -= 1
        if count == 0:
            newstr.append(curstr)
            curstr = ""
    print(len(newstr))
    for string in newstr:
        print(string)

s = input()
max_split(s)