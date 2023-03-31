import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 设置 x_name 和 y_name
x_name = "k"
y_name = "r^2"

# 生成数据
X = np.array([0, 1, 2, 3, 4])
Y = np.array([17/2, 24/2, 30.5/2, 35/2, 39/2])
Y = Y ** 2

# 计算线性回归参数
slope, intercept, r_value, p_value, std_err = linregress(X, Y)

# 拟合结果
Y_pred = slope * X + intercept

# 绘制数据点
plt.scatter(X, Y, label='Data Points')

# 绘制拟合线
plt.plot(X, Y_pred, color='red', label='Linear Regression')

# 设置轴标签
plt.xlabel(f"${x_name}$")
plt.ylabel(f"${y_name}$")

# 设置标题
plt.title(f"${y_name} = {slope:.4f} * {x_name} + {intercept:.4f}$")

# 显示图例
plt.legend()

# 在图像下方显示拟合曲线参数
plt.figtext(0.15, 0.1, (
    f"Slope: {slope:.4f}  "
    f"Intercept: {intercept:.4f}\n"
    f"R-value: {r_value:.4f}  "
    f"P-value: {p_value:.4f}  "
    f"Std. Error: {std_err:.4f}"
))

# 调整布局以适应文本和标题
plt.subplots_adjust(top=0.9, bottom=0.25)

# 显示图形
plt.show()
