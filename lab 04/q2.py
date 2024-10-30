''' Find winner of election
Given an array of names of candidates in an election. A candidate name in the array represents a
vote cast to the candidate. Print the name of candidates received Max vote. If there is tie, print a
lexicographically smaller name.
input = [‘john’,‘johnny’,‘jackie’,‘johnny’, ‘john’,‘jackie’,‘jamie’,‘jamie’,
‘john’,‘johnny’,‘jamie’,‘johnny’, ‘john’]
Output : John.
We have four Candidates with name as ‘John’, ‘Johnny’, ‘jamie’, ‘jackie’. The candidates John and
Johny get maximum votes. Since John is alphabetically smaller, we print it.'''


def election(votes):
    records = {}

    for vote in votes:
        if vote in records:
            records[vote] = records[vote]+1
        else:
            records[vote] = 1
    print(records)

input = ['john','johnny','jackie','johnny', 'john','jackie','jamie','jamie',
'john','johnny','jamie','johnny', 'john']
election(input)