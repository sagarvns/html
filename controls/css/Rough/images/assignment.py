import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("annotations2.csv")
# print(data)
# print(data["Nodule_diameter_mm"])
data = list(data["Nodule_diameter_mm"])

maxvalue = int(max(data) // 5 + 1)

x = [x for x in range(len(data))]
print(x)
x = [5 * x for x in range(maxvalue)]
print(x)
print(data)
# plt.plot(x, data)
# plt.scatter(x, data)
plt.title("Frequency Distribution")
colors = ["red", "green", "blue"]
colorno = 0
# plt.plot(kind='hist',data=data,title="Title")
plt.xlabel("Radius")
plt.ylabel("Frequency")
N, bins, patches = plt.hist(data, label="Frequency Distribution", bins=x, edgecolor="white")
plt.bar_label(patches)
n = len(patches)

for i in range(0, n):
    patches[i].set_facecolor(colors[colorno])
    colorno = (colorno + 1) % len(colors)
plt.savefig("s:\\graph.png")
plt.show()





















