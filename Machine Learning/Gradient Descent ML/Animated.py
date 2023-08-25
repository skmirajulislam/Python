import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def Gradient_descent():
    plt.rcParams['figure.figsize'] = (12.0, 6.0)  # Adjust plot size
    
    # Preprocessing Input data
    data = pd.read_csv('/Users/skmirajulislam/Documents/MyPython/Ml/Topstack/data/Mumbai_house.csv')
    X = data.iloc[:, 0]
    Y = data.iloc[:, 1]

    m = 0
    c = 0
    L = 0.0001  # The learning Rate
    epochs = 100  # The number of iterations to perform gradient descent
    n = float(len(X))  # Number of elements in X

    fig, axs = plt.subplots(1, 2)
    fig.suptitle('Linear Regression Y = mx+b',weight='bold')
    axs[0].set_title('Linear Relationship',weight='bold')
    axs[0].grid()
    axs[0].scatter(X, Y)

    cost_history = []
    line_history = [(m, c)]  # Store the initial line's coordinates

    for i in range(epochs):
        Y_pred = m * X + c
        D_m = (-2/n) * sum(X * (Y - Y_pred))
        D_c = (-2/n) * sum(Y - Y_pred)
        m -= L * D_m
        c -= L * D_c

        cost = np.mean(np.square(Y - Y_pred))//X.shape[0]
        cost_history.append(cost)
        line_history.append((m, c))  # type: ignore # Store the current line's slope and intercept

        axs[1].clear()
        axs[1].set_title(f'Gradient Descent  (Iteration {i}) \n Error is {cost}',weight='bold')
        axs[1].plot(range(i + 1), cost_history, marker='o')
        axs[1].set_xlabel('Iteration',weight='bold')
        axs[1].set_ylabel('Cost',weight='bold')
        axs[1].grid(color='green', linestyle='--', linewidth=0.5)
        
        # Plot the regression line's movement
        axs[0].clear()
        axs[0].set_title(f'Gradient Descent (Iteration {i})',weight='bold')
        axs[0].grid(color='green', linestyle='--', linewidth=0.5)
        axs[0].scatter(X, Y)
        for line_m, line_c in line_history:
            Y_line = line_m * X + line_c
            axs[0].plot([min(X), max(X)], [min(Y_line), max(Y_line)], color='red', alpha=0.5)  # Plot faded lines for animation effect
        
        axs[0].set_ylabel('Price of house',weight='bold')
        axs[0].set_xlabel('Area of house',weight='bold')
        plt.pause(0.1)  # Adjust the pause time for smoother animation

    plt.show()
    print("Final values: m =", m, "c =", c)

if __name__ == "__main__":
    Gradient_descent()
