# Applied-Linear-Algebra-KSE-lab_1
# Лабораторна робота №1
#### Лінійні трансформації
---
### Перед початком виконання роботи
- Можу порадити хороше відео, яке допоможе освіжити знання про лінійні трансформації і в результаті швидше впоратись з лабораторною) [Тут](https://www.youtube.com/watch?v=kYB8IZa5AuE&ab_channel=3Blue1Brown) згадуються основи основ, проте з дуже гарною візуалізацією. [Те ж відео](https://www.youtube.com/watch?v=fuBsMED8GOw&ab_channel=3Blue1BrownUA),  тільки у перекладі.
- Рекомендована мова програмування – **Python**. Зверніть увагу, що лабораторна робота розроблена під Python, і інші мови програмування можуть не забезпечити достатній функціонал для виконання всіх частин.
- Код пишеться з нуля)
- Щодо обмежень використання сторонніх бібліотек. Дана робота поділена на дві частини:
  - У першій частині дозволено використовувати лише NumPy для роботи з матрицями та matplotlib, або подібні бібліотеки, для візуалізації ***!!!НІЯКИХ ГОТОВИХ ФУНКЦІЙ ДЛЯ ЛІНІЙНИХ ТРАНСФОРМАЦІЙ ЗІ СТОРОННІХ БІБЛІОТЕК!!!***
  - У другій частині можна використовувати будь-що ~~окрім темної магії~~. Головне, щоб це працювало.
 
### Перша частина *(4 бали)*
1. Для початку потрібно створити і візуалізувати об'єкти, на яких буде відображатись виконана лінійна трансформація у двовимірному просторі. Ваше завдання – створити **два різні** об'єкти. Це можуть бути як фігури, так і просто набір векторів (бажано уникати симетричних зображень, щоб трансформації були більш помітні). *(0,5 бали)*

Наприклад:
    ```
    batman = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
    ```

2. Наступним кроком потрібно реалізувати функції, що будуть виконувати певні лінійні трансформації:
- обертати об'єкт на певний кут *(0,5 бали)*;
- маштабувати об'єкт з певним коефіцієнтом *(0,5 бали)*;
- віддзеркалювати об'єкт відносно певної осі *(0,5 бали)*;
- робити нахил певної осі координат *(0,5 бали)*;
- та універсальну функцію, що буде виконувати трансформацію з переданою у функцію кастомною матрицею трансформації *(0,25 балів)*.

Після кожної трансформації необхідно виводити результуюче зображення та його матрицю.

3. Поексперементувати з різними матрицями трансформації, зробити висновки, які елементи матриці на що впливають *(0,5 бали)*.
4. Спробувати виконати лінійні трансформації у тривимірному просторі, створивши принаймі одну тривиміну фігуру, та виконавши принаймі дві різні трансформації *(0,75 балів)*.

### Друга частина *(2 бали)*
1. Обрати бібліотеку із вже готовими функціями для лінійних трансформацій *(Рекомендую OpenCV, вона має найширший інструментарій; [Корисне посилання 1](https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html), [Корисне посилання 2](https://medium.com/@conghung43/image-projective-transformation-with-opencv-python-f0028aaf2b6d))*
2. За допомогою інструментарію бібліотеки реалізувати всі лінійни трансформації з пункту 2 попередньої частини на тих самих фігурах, створених у двовимірному просторі. Порівняти результати, отримані за допомогою готових бібліотек, з результатами роботи власних функцій *(1 бал)*.
3. Взяти довільне зображення, зчитати його за допомогою ``image = cv2.imread('image.jpg')`` та виконати 2-3 лінійні трансформації над цим зображенням. Вивести результуючі зображення *(1 бал)*.

---
### Теоретичні запитання *(2 бали)*
#### Відповіді прикріпити до репозиторію в текстовому форматі.
1. Що таке лінійні трансформації? *(0,25 бала)*
2. Як і в яких галузях застосовуються лінійні трансформації? *(0,25 бала)*
3. Що таке матриця лінійної трансформації та як її можна інтерпретувати? *(0,25 бала)*
4. Які особливості та властивості має матриця обертання? *(0,25 бала)*
5. Чи залежить фінальний результат від порядку трансформацій? Провести експерименти з фігурами або зображеннями з частин 1-2.  *(0,25 бала)*
6. Була здійснена якась довільна лінійна трансформація; як знайти матрицю лінійної трансформації, що поверне все до початкового вигляду? Чи завжди можна здійснити обернену трансформацію? *(0,25 бала)*
7. Модуль визначника матриці трансформації менше 1, які висновки можна зробити про дану трансформацію (як змінюється простір при даній трансформації)? А якщо більше 1? Дорівнює 1? Дорівнює 0? *(0,5 бала)*

### Оцінювання
  - Перша частина - 4 бали
  - Друга частина - 2 бали
  - Перша частина "захист" - 3 бали
  - Друга частина "захист" - 1 бал
  - Теоретичні запитання - 2 бали
