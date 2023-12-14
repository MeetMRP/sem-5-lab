import numpy as np

X1 = np.array([1, -2, 0, -1])
X2 = np.array([0, 1.5, -0.5, -1])
X3 = np.array([-1, 1, 0.5, -1])

# X1 = np.array([1, 2, 3, 4])
# X2 = np.array([4, 8, 1.2, 8])
# X3 = np.array([-1, 0, 4, 4])

X = np.array([X1, X2, X3])
W = np.array([1, -1, 0, 0.5])

d = np.array([-1, -1, 1])
c = 0.1
epochs = 10

for epoch in range(epochs):
    print(f'Epoch: {epoch+1}')
    for i in range(len(X)):
        net = np.dot(X[i], W)

        if net >= 0:
            op = 1
        else:
            op = -1

        error = d[i] - op

        dW = c * error * X[i]
        W += dW
        print(f'W{i}: {W}')
print(f"\nFinal W after {epochs} epochs:")
print(W) 