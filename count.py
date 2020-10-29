def get_token(easy):
    dict={}
    for item in easy:
        item = item.split(',')
        for i in item:
            if "Purpose" in i:
                aaa = i.split(' ') #Seperate words
                for word in aaa:
                    if word == '':
                        continue
                    if word in dict: #Count words and put in dictionary
                        dict[word] += 1
                    else:
                        dict[word] = 1
    #Sort dictionary from the highest value to the lease value
    mf = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    print(mf[1:11])

if __name__ == "__main__":
    with open("Compile.txt")as fp:
        get_token(fp)