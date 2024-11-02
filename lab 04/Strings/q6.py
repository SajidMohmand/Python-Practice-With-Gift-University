'''9.6 Pig Latin
Write a program that accepts a sentence as input and converts each word to “Pig Latin.” In one
version, to convert a word to Pig Latin you remove the first letter and place that letter at the end
of the word. Then you append the string “ay” to the word. Here is an example:
English: I SLEPT MOST OF THE NIGHT
Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY'''

def piglatin_converter(sentence):
    list = sentence.split(' ')

    for i in range(len(list)):
        if len(list[i]) == 1:
            list[i] += 'AY'
        else:
            list[i] = list[i][1:len(list[i])] + list[i][0:1] + "AY"

    return ' '.join(list)

sentence = 'I SLEPT MOST OF THE NIGHT'
print(sentence)
print("After Converting")
print(piglatin_converter(sentence))