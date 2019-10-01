import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns
# plt.style.use('seaborn')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

raw_housing_data = pd.read_csv('Boston_Housing_Red_4160_Regression.csv')
rm = raw_housing_data.RM
dis = raw_housing_data.DIS
price = raw_housing_data.Price
# ax1.scatter(rm, dis, price)
# ax1.set_xlabel('rm')
# ax1.set_ylabel('dis')
# ax1.set_zlabel('price')
# plt.show()

g = sns.pairplot(raw_housing_data)
plt.show()