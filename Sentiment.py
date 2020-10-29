from textblob import TextBlob
def senti(purposes):
    purpose_max = -100#Store a max value
    purpose_min = 100#Store a min value
    purpose_max_str = " " #Create an empty str for max
    purpose_min_str = " " #Create an empty str for min
    for sentence in purposes:
        if "Purpose" in sentence:
            blob = TextBlob(sentence)
            sent_pos = blob.sentiment[0]
            sent_neg = blob.sentiment[0]
            if sent_pos > purpose_max:
                purpose_max = sent_pos
                purpose_max_str = sentence
            if sent_neg < purpose_min:
                purpose_min = sent_neg
                purpose_min_str = sentence
    print("The best idea is:",purpose_max_str,"The worst idea is:",purpose_min_str)

if __name__ == "__main__":
    with open("Compile.txt")as c:
        senti(c)