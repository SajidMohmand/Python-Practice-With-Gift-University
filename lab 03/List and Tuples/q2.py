''' Driver’s License Exam
The local driver’s license office has asked you to create an application that grades the written
portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here are the
correct answers:
1. A 6. B 11. A 16. C
2. A 7. B 12. A 17. C
3. A 8. B 13. A 18. C
4. A 9. B 14. A 19. C
5
5. A 10. B 15. A 20. C
Your program should store these correct answers in a list. The program should read the student’s
answers for each of the 20 questions from a text file and store the answers in another list. (Create
your own text file to test the application.) After the student’s answers have been read from the file,
the program should display a message indicating whether the student passed or failed the exam. (A
student must correctly answer 15 of the 20 questions to pass the exam.) It should then display the
total number of correctly answered questions, the total number of incorrectly answered questions,
and a list showing the question numbers of the incorrectly answered questions.'''


def evaluation(stu_ans,ans):

    correct_ans = []
    incorrect_ans = []

    for i in range(0,20):
        if stu_ans[i].upper() == ans[i]:
            correct_ans.append(ans[i])
        else:
            incorrect_ans.append(ans[i])
    
    if len(correct_ans) >= 15:
        print('Congratulations!!! You Pass')
    else:
        print("!Sorry You Fail in Test.")
    print("Total Correct Answers : ",len(correct_ans))
    print("Total incorrect Answers : ",len(incorrect_ans))

def test(ans):
    stu_ans = []

    for i in range(1,21):
        stu_ans.append((input(f"Enter {i} answer : ")))

    evaluation(stu_ans,ans)

answers = ['A','A','A','A','A','B','B','B','B','B','A','A','A','A','A','C','C','C','C','C']
test(answers)
