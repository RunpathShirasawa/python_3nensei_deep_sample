import numpy as np
import matplotlib.pyplot as plt

def fillscolors(data):
    return "#ffc2c2" if data > 0 else "#c6dcec"
def dotscolors(data):
    return "#ff0e0e" if data > 0 else "#1f77b4"

def plot_perceptron(func, X1, X2):
    plt.figure(figsize=(6, 6))
    XX, YY = np.meshgrid(
        np.linspace(-0.25, 1.25, 200),
        np.linspace(-0.25, 1.25, 200))
    XX = np.array(XX).flatten()
    YY = np.array(YY).flatten()
    fills = []
    colors = []
    for i in range(len(XX)):
        fills.append(func(XX[i], YY[i]))
        colors.append(fillscolors(fills[i]))
    plt.scatter(XX, YY, c=colors)
    
    dots = []
    colors = []
    for i in range(len(X1)):
        dots.append(func(X1[i], X2[i]))
        colors.append(dotscolors(dots[i]))
    plt.scatter(X1, X2, c=colors)
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()
