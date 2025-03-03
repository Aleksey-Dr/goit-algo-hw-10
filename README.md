# Обчислення визначеного інтеграла методом Монте-Карло та перевірка результату / Calculating the definite integral using the Monte-Carlo method and checking the result

## <img src="https://img.shields.io/badge/Завдання 2 / Task 2-512BD4?style=for-the-badge"/>
Обчислити значення визначеного інтеграла функції f(x) = x^2 методом Монте-Карло на інтервалі [0, 2]. Перевірити точність результатів за допомогою аналітичного методу через функцію `quad` з бібліотеки SciPy.
___

Calculate the value of the definite integral of the function f(x) = x^2 using the Monte-Carlo method on the interval [0, 2].
Check the accuracy of the results using the analytical method via the `quad` function from the SciPy library.

## <img src="https://img.shields.io/badge/Порівняльний аналіз результатів / Comparative analysis of results-ECD53F?style=for-the-badge"/>
- Метод Монте-Карло: 2.6684
- Метод `quad`: 2.666666666666667 (з похибкою 2.960594732333751e-14)

Метод Монте-Карло дав близьке значення до точного результату, але з певною похибкою. Чим більше випадкових точок буде використовуватись у методі Монте-Карло, тим точніший результат буде отримано. Метод `quad` надає високу точність і підходить для точного обчислення інтегралів.
___

- Monte-Carlo method: 2.6684
- `quad` method: 2.66666666666667 (with an error of
2.960594732333751e-14)

The Monte-Carlo method gave a value close to the
exact result, but with some error. The
more random points are used in the
Monte-Carlo method, the more accurate the result will be. The `quad` method provides high accuracy and is
suitable for exact calculation of integrals.

## <img src="https://img.shields.io/badge/Висновки / Conclusions-007054?style=for-the-badge"/>
- Метод Монте-Карло є ефективним для обчислення інтегралів у випадках, коли важко або неможливо знайти аналітичне рішення. Проте, для точніших результатів, таких як у нашому прикладі, метод `quad` є більш надійним.
___

- The Monte-Carlo method is effective for calculating integrals in cases where it is difficult or impossible to find an analytical solution. However, for more precise results, such as in our example, the quad method is more reliable.