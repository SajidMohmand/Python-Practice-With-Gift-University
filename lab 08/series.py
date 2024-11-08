import pandas as pd

result = pd.Series(data=["Sajid","cs",213], index=["name","department","rollNo"])
# print(result)
# print(result['name'])

my_dict = {'name':"Sajid","rollNo" : 2113, "semester" : 7}

result2 = pd.Series(data=my_dict)
# print(result2)

# add_series = result + result2
# print(add_series)

# print(add_series.isnull())


# print(result.head(2))
# print(result.tail(1))

# print(result.axes)
# print(result.values)
# print(result.size)
# print(result.empty)
