import numpy as np

sigmoid = (
    lambda x: 1.0 / (1 + np.exp(-x)),
    lambda x: x * (1.0 - x)
)

relu = (
    lambda x: np.maximum(0, x),
    lambda x: 1 * (x > 0)
)


class NeuralNetwork:
    HIDDEN_LAYER_SIZE = 4

    def __init__(self, x, y, activation1, activation2):
        self.input = x
        input_size = self.input.shape[1]
        self.weights1 = np.random.rand(self.HIDDEN_LAYER_SIZE, input_size)
        self.weights2 = np.random.rand(1, self.HIDDEN_LAYER_SIZE)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = 0.5
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

    def learn(self):
        for i in range(5000):
            self.feedforward()
            self.backprop()


def get_error(y, output):
    return np.linalg.norm(y - output)

def compare_activations(X, y):
    nn = NeuralNetwork(X, y, sigmoid, sigmoid)
    nn.learn()
    print(f"sigmoid - sigmoid {get_error(y, nn.output)}")

    nn = NeuralNetwork(X, y, sigmoid, relu)
    nn.learn()
    print(f"sigmoid - relu {get_error(y, nn.output)}")

    nn = NeuralNetwork(X, y, relu, relu)
    nn.learn()
    print(f"relu - relu {get_error(y, nn.output)}")

    nn = NeuralNetwork(X, y, relu, sigmoid)
    nn.learn()
    print(f"relu - sigmoid {get_error(y, nn.output)}")


def main():
    print("xor")
    X = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]
                  ])

    y = np.array([[0], [1], [1], [0]])

    compare_activations(X, y)

    print("and")
    y = np.array([[0], [0], [0], [1]])
    compare_activations(X, y)

    print("or")
    y = np.array([[1], [1], [1], [1]])
    compare_activations(X, y)



if __name__ == "__main__":
    main()
