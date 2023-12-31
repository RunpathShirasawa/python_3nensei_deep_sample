# -*- coding: utf-8 -*-
"""DLtest4-04 数字の画像（sklearn）の学習.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xku-7L9y0w9QuOHpiv88frk_1GS_hDGp

# **4.04 数字の画像（sklearn）の学習**

# 【データの準備と確認】

リスト4-24：（リストA）
"""

!pip install japanize-matplotlib
import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np
import keras
from keras import layers

"""リスト4-25"""

import sklearn.datasets
from sklearn.model_selection import train_test_split
digits = sklearn.datasets.load_digits()
X = digits.data
y = digits.target
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0)
x_train, x_test = x_train / 255.0, x_test / 255.0

print(f"学習データ（問題画像）　：{x_train.shape}")
print(f"テストデータ（問題画像）：{x_test.shape}")

"""リスト4-26"""

def disp_data(xdata, ydata):
    plt.figure(figsize=(12,10))
    for i in range(20):
        plt.subplot(4,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(xdata[i].reshape(8,8), cmap="Greys")
        plt.xlabel(ydata[i])
    plt.show()

disp_data(x_train, y_train)

"""リスト4-27"""

disp_data(x_test, y_test)

"""# 【モデルを作って学習】

リスト4-28
"""

model = keras.models.Sequential()
model.add(layers.Dense(128, activation="relu", input_dim=64))
model.add(layers.Dense(10, activation="softmax"))
model.summary()

"""リスト4-29：（リストB'）"""

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])
history = model.fit(x_train, y_train, epochs=10, #10
                    validation_data=(x_test, y_test))
test_loss, test_acc =model.evaluate(x_test, y_test)
print(f"テストデータの正解率は{test_acc:.2%}です。")

"""リスト4-30：（リストC）"""

param = [["正解率", "accuracy", "val_accuracy"],
          ["誤差", "loss", "val_loss"]]
plt.figure(figsize=(10,4))
for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.title(param[i][0])
    plt.plot(history.history[param[i][1]], "o-")
    plt.plot(history.history[param[i][2]], "o-")
    plt.xlabel("学習回数")
    plt.legend(["訓練","テスト"], loc="best")
    if i==0:
        plt.ylim([0,1])
plt.show()

"""## 正解率をもう少し上げるために、ニューロン数と学習回数を増やしてみましょう。

リスト4-31
"""

model = keras.models.Sequential()
model.add(layers.Dense(1024, activation='relu', input_dim=64))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dense(10, activation="softmax"))
model.summary()

"""リスト4-32：（リストB’）"""

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])
history = model.fit(x_train, y_train, epochs=10, #10
                    validation_data=(x_test, y_test))
test_loss, test_acc =model.evaluate(x_test, y_test)
print(f"テストデータの正解率は{test_acc:.2%}です。")

"""リスト4-33：（リストC）"""

param = [["正解率", "accuracy", "val_accuracy"],
          ["誤差", "loss", "val_loss"]]
plt.figure(figsize=(10,4))
for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.title(param[i][0])
    plt.plot(history.history[param[i][1]], "o-")
    plt.plot(history.history[param[i][2]], "o-")
    plt.xlabel("学習回数")
    plt.legend(["訓練","テスト"], loc="best")
    if i==0:
        plt.ylim([0,1])
plt.show()

"""# 【データを渡して予測】

リスト4-34
"""

pre = model.predict(x_test)

plt.figure(figsize=(12,10))
for i in range(20):
    plt.subplot(4,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x_test[i].reshape(8,8), cmap="Greys")

    index = np.argmax(pre[i])
    pct = pre[i][index]
    ans = ""
    if index != y_test[i]:
        ans = "x--o["+str(y_test[i])+"]"
    lbl = f"{index} ({pct:.0%}){ans}"
    plt.xlabel(lbl)
plt.show()