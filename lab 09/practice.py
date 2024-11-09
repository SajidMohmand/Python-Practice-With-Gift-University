import matplotlib.pyplot as plt

# x = ['java','pyhton','javascript', 'dart']
# y = [80,40,40,60]

# plt.bar(x,y)
# plt.show()

day = [1,2,3,4,5,6,7]
no = [2,3,1,4,5,3,6]


colors = ["r", "b", "m", "y", "g","r","r"]
size = [300,400,500,600,700,800,900]
plt.scatter(day, no, c=colors, s=size)
plt.title('Scatter Plot', fontsize=15)
plt.xlabel('Day', fontsize=15)
plt.ylabel('No', fontsize=15)
plt.show()
