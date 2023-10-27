# -*- coding: utf-8 -*-
"""DLtest4-02 じゃんけん判定の学習.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12LfTZfQ0BAOngzMEfnCgZC6O2ia9Lxz6

# **4.02 じゃんけん判定の学習**

# 【データの準備と確認】

リスト4-8
"""

!pip install japanize-matplotlib
import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np
import keras
from keras import layers

"""リスト4-9"""

hand_name = ["グー", "チョキ", "パー"]
judge_name = ["あいこ", "勝ち", "負け"]

hand_data = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
judge_data = [0, 1, 2, 2, 0, 1, 1, 2, 0]

x_train = x_test =  np.array(hand_data)
y_train = y_test = np.array(judge_data)

print("学習データ（問題）：")
print(x_train)
print(f"学習データ（答え）：{y_train}")

"""# 【モデルを作って学習】

リスト4-10
"""

model = keras.models.Sequential()
model.add(layers.Dense(8, activation="relu", input_dim=2))
model.add(layers.Dense(8, activation="relu"))
model.add(layers.Dense(3, activation="softmax"))
model.summary()

"""リスト4-11：（リストB'）"""

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])
history = model.fit(x_train, y_train, epochs=1000,  #1000
                    validation_data=(x_test, y_test))
test_loss, test_acc =model.evaluate(x_test, y_test)
print(f"テストデータの正解率は{test_acc:.2%}です。")

"""リスト4-12：（リストC）"""

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

リスト4-13
"""

pre = model.predict(x_test)
for i in range(3):
    print(f"{pre[i][0]:.0%} {pre[i][1]:.0%} {pre[i][2]:.0%}")

"""リスト4-14"""

for i in range(len(x_test)):
    hand1 = hand_name[x_test[i][0]]
    hand2 = hand_name[x_test[i][1]]
    index = np.argmax(pre[i])
    judge = judge_name[index]
    print(f"私は「{hand1}」、相手は「{hand2}」なので、{judge}")