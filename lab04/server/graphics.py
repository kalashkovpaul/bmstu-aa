import matplotlib.pyplot as plt
fig1 = plt.figure(figsize=(10, 7))
plot = fig1.add_subplot()
connections = [12, 40, 80, 120, 160, 200]
threads16 = [550, 546, 543, 533, 514, 506]
threads8 = [544, 434, 397, 360, 319, 220]
threads1 = [537, 291, 189, 147, 117, 86]
plot.plot(connections, threads16, label = "Реализация в 16 потоков")
plot.plot(connections, threads8, ":", label="Реализация в 8 потоков")
plot.plot(connections, threads1, "--", label="Реализация в 1 поток")

plt.legend()
plt.grid()
plt.title("Временные характеристики обработки запросов сервером")
plt.ylabel("Количество обработанных запросов в секунду (rps)")
plt.xlabel("Количество открытых соединений, шт.")

plt.show()