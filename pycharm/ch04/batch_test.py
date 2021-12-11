import sys, os

sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
print(x_train.shape)
print(t_train.shape)
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)  # 6 萬中挑 10 筆
x_batch = x_train[batch_mask]  # 建立一個用 batch 的 index 取 x_train 裡的 element
t_batch = t_train[batch_mask]