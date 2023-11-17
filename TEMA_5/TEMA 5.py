import numpy as np

data = np.loadtxt("seeds_dataset.txt")
np.random.shuffle(data)
features = data[:, :7]
labels = data[:, 7:].flatten()

min_val = np.min(features, axis=0)
max_val = np.max(features, axis=0)
features = (features - min_val) / (max_val - min_val)

train_features = features[: int(len(features) * 0.8)].astype(np.float32)
test_features = features[int(len(features) * 0.8) :].astype(np.float32)
train_labels = (labels[: int(len(labels) * 0.8)] - 1).astype(np.float32)
test_labels = (labels[int(len(labels) * 0.8) :] - 1).astype(np.float32)


class NeuralNet:
    def __init__(self, input_size, hidden_size1, hidden_size2, output_size):
        self.hidden1 = np.random.randn(input_size, hidden_size1)
        self.hidden2 = np.random.randn(hidden_size1, hidden_size2)
        self.output = np.random.randn(hidden_size2, output_size)

    def forward(self, x):
        x = np.dot(x, self.hidden1)
        x = relu(x)
        x = np.dot(x, self.hidden2)
        x = relu(x)
        x = np.dot(x, self.output)
        x = softmax(x)
        return x


input_size = 7
hidden_size1 = 5
hidden_size2 = 5
output_size = 3
learning_rate = 0.01
epochs = 100


def relu(x):
    return np.maximum(0, x)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / np.sum(e_x, axis=1, keepdims=True)


def relu_derivative(x):
    return np.where(x > 0, 1, 0)


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


def softmax_derivative(x):
    p = softmax(x)
    return p * (1 - p)


def cross_entropy_loss(y_true, y_pred):
    m = y_true.shape[0]
    log_likelihood = -np.log(y_pred[range(m), y_true])
    loss = np.sum(log_likelihood) / m
    return loss


def main():
    model = NeuralNet(input_size, hidden_size1, hidden_size2, output_size)

    test_input = np.random.randn(1, input_size)
    print("Input Data:", test_input)

    predicted_output = model.forward(test_input)

    predicted_class = np.argmax(predicted_output) + 1

    print("Predicted Class Label:", predicted_class)

    loss = cross_entropy_loss(np.array([predicted_class - 1]), predicted_output)
    print("Loss:", loss)


main()
