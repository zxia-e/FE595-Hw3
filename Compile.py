import string
#open txt
#Open Tianyi Yang's text
with open('Tianyi.txt') as fp:
    data1 = fp.readlines()
#Open Mengge Geng's text
with open('Mengge.txt') as fp:
    data2 = fp.readlines()
#Open Jiefu Dong's text
with open('Jiefu.txt') as fp:
    data3 = fp.readlines()
#Open Han Luo's text
with open('Han.txt') as fp:
    data4 = fp.readlines()
allData = data1+data2+data3+data4 #Merging all files together

def convert(myString): #Remove punctuations
    mylist = myString
    for i in range (0,len(mylist)):
        mylist[i]=mylist[i].replace("\n", "")
        for c in mylist[i]:
            if c in string.punctuation:
                mylist[i] = mylist[i].replace(c,"")
    return(mylist)

newData = str(convert(allData))

if __name__ == '__main__':
    with open('Compile.txt', 'w') as fp:
        fp.write(newData)


