import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

plt.style.use('seaborn')
plt.tight_layout()
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [1,2,3,4,5,6,7,8,9,10]
# z = [1,2,3,4,5,6,7,8,9,10]

# ax1.plot(x,y,z)

# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.set_zlabel('z')
# plt.show()

raw_housing_data = pd.read_csv('Boston_Housing_Red_4160_Regression.csv')
rm = raw_housing_data.RM
dis = raw_housing_data.DIS
price = raw_housing_data.Price
ax1.scatter(rm, dis, price, label='Raw Data', color='blue')
raw_housing_data['adj_price'] = raw_housing_data.RM*8.56811 + raw_housing_data.DIS*0.4264625 - 32.74
# ax1.plot(rm, dis, raw_housing_data.adj_price, label='Gradient Descent', color='red')
ax1.scatter(rm, dis, raw_housing_data.adj_price, label='Gradient Descent', color='red')
print(raw_housing_data.shape)
print(raw_housing_data.describe())
fig.legend()
ax1.set_xlabel('rm')
ax1.set_ylabel('dis')
ax1.set_zlabel('price')
plt.show()
