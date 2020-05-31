import numpy as np
import matplotlib.pyplot as plt
import math
import time
import argparse


sigmoid = (
    lambda x: 1./(1 + np.exp(-x)),
    lambda x: x * (1. - x)
)

relu = (
    lambda x: np.maximum(0, x),
    lambda x: 1. * (x > 0)
)

tanh = (
    lambda x: np.tanh(x),
    lambda x: (1. / np.cosh(x))**2
)


class NeuralNetwork:
    def __init__(self, x, y, activation1, activation2, eta=0.1, layer_size=4):
        self.input = x
        input_size = self.input.shape[1]
        self.weights1 = np.random.rand(layer_size, input_size)
        self.weights2 = np.random.rand(1, layer_size)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = eta
        self.activation1, self.activation_derivative1 = activation1
        self.activation2, self.activation_derivative2 = activation2

    def feedforward(self):
        self.layer1 = self.activation1(np.dot(self.input, self.weights1.T))
        self.output = self.activation2(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.y - self.output) * \
            self.activation_derivative2(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)

        delta1 = self.activation_derivative1(self.layer1) * \
            np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def learn(self, rounds):
        for i in range(rounds):
            self.feedforward()
            self.backprop()


def test_sin():
    x = np.linspace(0, 2, 21)
    y = np.sin(x * (3*np.pi/2))
    x_reshaped = np.reshape(x, (len(x), 1))
    y_reshaped = np.reshape(y, (len(y), 1))
    big_x = np.linspace(0, 2, 101) # sinus
    big_x = big_x / max(big_x)
    big_x_reshaped = np.reshape(big_x, (len(big_x), 1))
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_title('Oryginał')
    ax1.scatter(x, y)

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.set_title('Aproksymowane')

    network = NeuralNetwork(x_reshaped, y_reshaped, sigmoid, tanh, 0.1, 20)
    for i in range(5000):
        network.learn(100)
        network.input = big_x_reshaped
        network.feedforward()
        ax2.clear()
        ax2.set_xlabel(f"{i*100} iteracji")
        ax2.scatter(big_x_reshaped, network.output.flatten())
        network.input = x_reshaped
        plt.pause(0.016)
    plt.show()


def test_square():
    x = np.linspace(-50, 50, 26)
    x = x / max(x)
    y = x**2

    x_reshaped = np.reshape(x, (len(x), 1))
    y_reshaped = np.reshape(y, (len(y), 1))


    big_x = np.linspace(-50, 50, 101)
    big_x = big_x / max(big_x)

    big_x_reshaped = np.reshape(big_x, (len(big_x), 1))

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_title('Oryginał')
    ax1.scatter(x, y)

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.set_title('Aproksymowane')

    network = NeuralNetwork(x_reshaped, y_reshaped, sigmoid,
                            sigmoid, 0.1, 20)
    for i in range(5000):
        network.learn(100)
        network.input = big_x_reshaped
        network.feedforward()
        ax2.clear()
        ax2.set_xlabel(f"{i*100} iteracji")
        ax2.scatter(big_x_reshaped, network.output.flatten())
        network.input = x_reshaped
        plt.pause(0.016)
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='test neural nets for sin and x^2')
    parser.add_argument('--func', dest='func', required=True)
    args = parser.parse_args()

    if args.func == "sin":
        test_sin()
    else:
        test_square()
