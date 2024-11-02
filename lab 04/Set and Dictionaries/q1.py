'''Capital Quiz
Write a program that creates a dictionary containing the U.S. states as keys and their capitals as
values. (Use the Internet to get a list of the states and their capitals.) The program should then
randomly quiz the user by displaying the name of a state and asking the user to enter that state’s
capital. The program should keep a count of the number of correct and incorrect responses. (As
an alternative to the U.S. states, the program can use the names of countries and their capitals.)
'''

states_and_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta"
}

def quizz(states):

    a = ""

    corr_ans = 0
    incorr_ans = 0
    for key in states:
        a = input(f"{key} Enter capital (-1 to exit): ")
        if a == -1: break
        if a == states[key]:
            corr_ans += 1
        else:
            incorr_ans += 1
        
    print("Correct answer : ",corr_ans)
    print("Incorrect answer : ",incorr_ans)


quizz(states_and_capitals)