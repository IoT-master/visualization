from matplotlib import pyplot as plt
import numpy as np
# print(plt.style.available)
plt.style.use('fivethirtyeight')
# plt.plot([1,2,3,4], [2,4,5,6], color='#444444', linestyle='--', label='blah')
# plt.barh([1,2,3,4], [2,4,5,6], color='#444444', linestyle='--', label='blah')
# plt.bar([1,3,4,5], [2, 4, 5, 5], color='#444444', linestyle='--', label='blah', width=.25)
# plt.xticks(ticks=, labels=xvar)
plt.pie([60,40], labels=['a', 'b'], 
        wedgeprops={'edgecolor': 'black'}, 
        colors=['#6A1B9A', '#fc4f30'], 
        explode=[0, .1], shadow=True, startangle=90,
        autopct='%1.1f%%')
plt.title('The Show')
plt.xlabel('The X')
plt.ylabel('The Y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()