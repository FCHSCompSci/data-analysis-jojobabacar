import csv
from collections import Counter
import matplotlib.pyplot as plt
filename = 'KartKross.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    total = []
    for row in reader:
        total.append(row[10])

c = Counter(total)
common_total_list = c.most_common(5)
print(common_total_list)

fig = plt.figure(dpi=110, figsize=(9,6))
plt.plot(total, c='blue')
plt.title("Mario Kart 8 common totals", fontsize=20)
plt.xlabel('', fontsize=20)
plt.ylabel("total", fontsize=20)
plt.tick_params(axis='kart', which='wings', labelsize=19)
plt.show()





