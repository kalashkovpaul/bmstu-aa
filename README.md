# Algorithm analysis course, BMSTU IU7, V semester, 2022


## **Lection 4, 22.09.11**

Есть матрица n на n из 0 и 1, в ней есть один или несколько (ладно, пусть 1) квадрат наибольшего размера, состоящий из 1
Найти наибольший квадрат из единиц за один обход по матрице - координаты и размер
Матрицу можно (!) портить, меняя значения внутри. Можно просматривать k фиксированных соседей

### Терминология
1. Вход алгоритма - D.

    D = (cli | i = 1, m; |cli| = beta бит)
2. Длина входа

    n (как правило n != |D| = m)

    n = mu_t(D)

    Т - умнжоение матриц nxn,

    m = 2n^2 + 1,

    mu_T(D) = n = sqrt((|D| - 1) / 2) - так исторически слоожилось
3. D_n - сколько наборов входных данных при определённой длине входа

    D_n = {D | mu_T(D) = n}

    Если beta = 16, n = 10

    |D_10| = 2^(16^10)

4. Универсальные характеристики

    V(D) = V_D(D) + V_R(D) + V_доп(D) + V_exe, где

        V_D - объём начальных данных;

        V_R - объём возвращаемых данных;

        V_доп -  объём дополнительных данных;

        V_exe - объём данных под программу

    f_A(D) - трудоёмкости - число элементарных операций принятой модели вычислений, заданных
5. f_A(n)

    a) f_{A}^{V}(n) equiv (by def) = min_{D in D_n} {f_A(D)} - лучший случай

    b) f_{A}^{^}(n) equiv (by def) = max_{D in D_n}{f_A(D)} - худший случай

        forall D in D_n f_A(D) <= f_{A}^{^}(n)
    c) Страшная и безполезная формула - взять фотку у Лёши Авсюнина - формула мат.ожидания и того, что средняя трудоёмкость это сумма трудоёмкостей, умноженных на их мат.ожидания

**Пример:** Суммирование элементов массива Sum(A, n ; S)
```
 s <- 0
 for i <- 1 to n
    s <- s + A[i]
```
Ууууу, что такое цикл? Переписать надо
```
next:
    i <- 1
    ...
    i <- i + 1
    if i <= n goto(next)
```

f_{A}^{^}(n) =f_{A}^{V} = f_{A}(n) = 1 + 1 + n(3 + 3) = 6n + 2
Задача: можно ли не 6n, а меньше?

**Пример 2** Умножение матриц Mult.Matr(A, B, n; C)
```
Mult.Matr(A, B, n; C)
    for i <- to n
        for j <- to n
            s <- 0
            for k <- to n
                s <- s + A[i, k] * B[k, j]
                C[i, j] <- s
```
f_A(n) = 1 + n(3 + 1 + n(3 + 1 + 1 + n(3 + 7) + 3)) = 10n^3 + 8n^2 + 4n + 1


## **Лекция, 17 ноября 2022** Рекурсивные функции в математике

### Рекурсивные функции

1. Три ипостаси термина:

    a) рекурсивная функция в Теории алгоритмов - Чёрч, Клини - можно почитать;

    b) рекурсивная функция в математике;

    c) рекурсивная функция в программировании;

2. Способы задания функций:

    Функция (по А.Н. Колмогорову) - это отношение, униморфное по второй координате.

    Если есть 2 множества ``А``, ``В``, оператор декартого произведения ``A x B = {(a, b) | a in A, b in B}``, а отношение ``R`` на ``А, В`` - подмножество декартого произведения ``A x B``.

    Отношение ``R in F`` (униморфных) тогда и только тогда, когда из ``(a, b), (a', b') in R => b = b'``, то есть одному значению функции - только один аргумент. Арксинус - не функция

    a) табличный
    |x |f(x)|
    |--|----|
    |x1| f1 |
    |x2| f2 |
    | .| .  |
    | .| .  |
    | .| .  |

    b) элементарные функции:

    - полиномы;

    - тригонометрические функции;

     Проблемы: ``th(x)`` - элементарен? А интеграл, не берущийся в элементарных функциях?

    c) рекурсивный способ

    ```
    f(n), n in N or '0', далее одна система
    {f(0) = f_0
    {f(1) = f_1
    {...           => рекуррентное соотношение
    {f(m) =f_m
    {f(n+1) = g(f(n), ..., f(0), n, c), n >= m
    ```

    Задача: решить рекуррентное соотошение => ``f(n)``

3. Примеры:

    a) Система -  по сути, ``f(n) = n``
    ```
    f(1) = 1
    f(n) = f(n - 1) + 1, n >= 2
    ```
    b) Система - по сути, ``f(n) = n^2``
    ```
    f(1) = 1
    f(n + 1) = f(n) + 2n + 1, n >= 1
    ```
    c) Для куба: ``f(n) = n^3``
    ```
    f(1) = 1
    f(n + 1) = f(n) + 3n^2 + 3n + 1
    ```
    d) ``f(n) = 2^n``
    ```
    f(0) = 1
    f(n) = 2 * f(n - 1)
    ```
    e) А это что?
    ```
    С полной предысторией
    f(0) = 1
    f(n) = f(n - 1) + f(n - 2) + ... + f(0) + 1
    А это f(n) = 2^n
    Но ведь так непохоже...
    ```
    f) Фибоначчи
    ```
    f(1) = 1
    f(2) = 1
    f(n) = f(n - 1) + f(n - 2)
    ```
    g) ``f(n) = n!``
    ```
    f(0) = 1
    f(n) = n * f(n - 1)

    Почему 0! это 1? Сказка...

    Был такой математик, Уалес - он задумался, почему факториал только длял целых чисел... Можно ли предложить функцию, которая совпадает с факториалом во всех целых точках и распространяется также и для действительных?
    Ответ - Леонард Эйлер - то, что потом назвали гамма-функцией
    Г(s) = \intergal{0}{\inf}{t^{s-1}e^{_t}dt}
    Функция под интеграолм для s = 3 - питон, съевший слонёнка
    Чем больше s, тем ближе слонёнок к жирафу
    Интегрируем по частям...
    Г(s + 1) = sГ(s)
    Г(4) = 3Г(3) = 3*2*Г(2) = 3*2*1*Г(1)
    Г(1) = \integral{0}{\inf}{e^{_t}dt} = 1
    Итого - гамма-функция во всех целых точках совпадает с факториалом со смещением на 1, т.е. Г(n + 1) = n!
    Отсюда 0! = Г(1) = 1
    Сегодня абсолютно все программные продукты считают логарифм гамма-функции
    ```

__Производящие функции__

Есть последовательность чисел
```
a_0, a_1, a_2, ..., a_n, ... => a_0 + a_1 z + a_2 z^2 + a_3 z^3 + ... =>? G(z)
G(0) = a_0
G'(0) = [a_1 + 2a_2 z + 3a_3 z^2 + ...]  = a_1
G''(0) = 2! a_2

a_k = \frac{1}{k!}D^{(k)}G(z) |z=0

G -  производящая функция последовательности a

1 + z + z^2 + ... = \frac{1}{1 - z}
e^z = \sum{\frac{1}{k!}z^k}, поэтому экспонента - производящая функция 1/k!
```

4. \beta_{1}(n)
    |n_(1)|0|1|2|3|4|5|6|7|8|9|
    |-|-|-|-|-|-|-|-|-|-|-|
    |n_(2)|0|1|11|10|100|101|110|111|1000|1001|
    |\beta_{1}(n)|0|1|1|2|1|2|2|3|1|2|

    Это счастье может быть ограничено сверху логарифмом, т.е. \beta_1 = O(\log{2}{n})

    Система:
    ```
    \beta_1(0) = 0
    \beta_1(1) = 1
    \beta_1(n) = \beta_1(n/2), n mod 2 = 0
    \beta_1(n) = \beta_1(n/2) + 1, n mod 2 = 1
    ```
    Данное рекуррентное соотношение не имеет решения в элементарных функциях



