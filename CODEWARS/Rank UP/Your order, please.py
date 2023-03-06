# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
def order(sentence):
    txt = sentence.split()
    for x in sentence.split():
        for j in x:
            if j.isdigit():
                if int(j) == 1:
                    txt[0] = x
                elif int(j) == 2:
                    txt[1] = x
                elif int(j) == 3:
                    txt[2] = x
                elif int(j) == 4:
                    txt[3] = x
                elif int(j) == 5:
                    txt[4] = x
                elif int(j) == 6:
                    txt[5] = x
                elif int(j) == 7:
                    txt[6] = x
                elif int(j) == 8:
                    txt[7] = x
                elif int(j) == 9:
                    txt[8] = x

    return ' '.join(txt)

#
# def order(sentence):
#     if not sentence:
#         return ""
#     result = []
#     for i in range(1, 10):
#         for item in sentence.split():
#             if str(i) in item:
#                 result.append(item)  # adds them in numerical order since it cycles through i first
#
#     return " ".join(result)