'''9.2 Reverse Incremental String Slicing
Sometimes, while working with Pythonn strings, we can have a problem in which we need to perform
the slice and print of strings in reverse order. This can have application in day-day programming.
So in this exercise write a program that reverse the string in incremental order.
For Example:
Orignal String : GIFT
Incremental reverse strings: ['T','TF','TFI','TFIG']
'''

def helper(s):

    revrese_s = ""
    list = []
    for c in s:
        revrese_s = c+revrese_s

    r = ""
    for char in revrese_s:
        r += char
        list.append(r)
    return list


s = "GIFT"
list = helper(s)
print(list)