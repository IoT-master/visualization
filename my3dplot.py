import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

plt.style.use('seaborn')

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
ax1.scatter(rm, dis, price)
ax1.set_xlabel('rm')
ax1.set_ylabel('dis')
ax1.set_zlabel('price')
plt.show()