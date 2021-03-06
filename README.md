# python_tasks
Сюда буду выкладывать решения задач по программированию на языке python, которые мне попались на просторах интернета.

(stepik_bio_cake)
В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования достанется большой и вкусный пирог. В команде биологов a человек, а в команде информатиков — b человек.
Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.
Напишите программу, которая помогает найти это число.
Программа должна считывать размеры команд (два положительных целых числа a и b, каждое число вводится на отдельной строке) и выводить наименьшее число d, которое делится на оба этих числа без остатка.

(stepik_mailru_group_storage)
Key-value хранилище
На этой неделе мы с вами реализуем собственный key-value storage. Вашей задачей будет написать скрипт, который принимает в качестве аргументов ключи и значения и выводит информацию из хранилища (в нашем случае — из файла).
Запись значения по ключу
> storage.py --key key_name --val value
Получение значения по ключу
> storage.py --key key_name
Ответом в данном случае будет вывод с помощью print соответствующего значения
> value
или
> value_1, value_2
если значений по этому ключу было записано несколько. Метрики сохраняйте в порядке их добавления. Обратите внимание на пробел после запятой.
Если значений по ключу не было найдено, выводите пустую строку или None.
Для работы с аргументами командной строки используйте модуль argparse. Вашей задачей будет считать аргументы, переданные вашей программе, и записать соответствующую пару ключ-значение в файл хранилища или вывести значения, если был передан только ключ. Хранить данные вы можете в формате JSON с помощью стандартного модуля json. Проверьте добавление нескольких ключей и разных значений.
Файл следует создавать с помощью модуля tempfile.

Шифр простой замены (stepik_mailru_group_simple_cripto)
Напишите программу для дешифровки сообщений, зашифрованных шифром простой замены . На вход программе подается зашифрованная строка и таблица дешифровки.
Таблица дешифровки - это последовательность символов, каждый из которых соотносится с соответствующим (по порядку) символом оригинального алфавита. Для наглядности, можно записать таблицу дешифровки и алфавит друг под другом:
cdefghijklmnopqrstuvwxyzab  # таблица дешифровки
abcdefghijklmnopqrstuvwxyz  # оригинальный алфавит
Такое расположение показывает соответствие букв из зашифрованного текста буквам оригинального текста. Например: символ j в зашифрованном тексте соответствует h оригинального.
Расшифруйте сообщения и выведите его на печать. Программа должна быть не чувствительна к регистру букв (все буквы исходного сообщения должны быть переведены в нижний регистр).

Лотерея. (stepik_mailru_group_lottery)
Вы работаете в компании организующей лотереи. Номер лотерейного билета имеет вид - «002345 AZ» (порядковый номер билета, состоящий из 6 цифр, и серии из двух заглавных букв латинского алфавита).
Напишите программу, которая генерирует номера билетов победителей. На вход программе подается: количество победителей, и номер последнего проданного билета.  Программа должна генерировать указанное количество уникальных номеров (если количество проданных билетов позволяет сделать это) и напечатать их в формате — Победитель номер 1 - «002345 AZ». Победители могут выводится в любом порядке.
Гарантируется, что все номера билетов с номерами от «000001» по номер  последнего проданного билета (включительно) будут участвовать в розыгрыше и номер серии в текущем розыгрыше лотереи уникален. Если количество проданных билетов меньше или равно количеству запланированных победителей в розыгрыше, выигравшими считаются все номера проданных билетов.


(stepik_mailru_group_classes_car)
Вам необходимо создать свою иерархию классов для данных, которые описаны в таблице.
BaseCar
Car(BaseCar)
Truck(BaseCar)
SpecMachine(BaseCar)
У любого объекта есть обязательный атрибут car_type. Он означает тип объекта и может принимать одно из значений: car, truck, spec_machine.
Также у любого объекта из иерархии есть фото в виде имени файла — обязательный атрибут photo_file_name.
В базовом классе нужно реализовать метод get_photo_file_ext для получения расширения файла (“.png”, “.jpeg” и т.д.) с фото. Расширение файла можно получить при помощи os.path.splitext.
Для грузового автомобиля необходимо разделить характеристики кузова на отдельные составляющие body_length, body_width, body_height. Разделитель — латинская буква x. Характеристики кузова могут быть заданы в виде пустой строки, в таком случае все составляющие равны 0. Обратите внимание на то, что характеристики кузова должны быть вещественными числами.
Также для класса грузового автомобиля необходимо реализовать метод get_body_volume, возвращающий объем кузова в метрах кубических.
Далее необходимо реализовать функцию, на вход которой подается имя файла в формате csv. Файл содержит данные аналогичные строкам из таблицы. Вам необходимо прочитать этот файл построчно при помощи модуля стандартной библиотеки csv. Затем проанализировать строки и создать список нужных объектов с автомобилями и специальной техникой. Функция должна возвращать список объектов.
Не важно как вы назовете свои классы, главное чтобы их атрибуты имели имена:
car_type
brand
passenger_seats_count
photo_file_name
body_width
body_height
body_length
carrying
extra
И методы:
get_photo_file_ext и get_body_volume
У каждого объекта из иерархии должен быть свой набор атрибутов и методов.
У класса легковой автомобиль не должно быть метода get_body_volume в отличие от класса грузового автомобиля.
Функция, которая парсит строки входного массива, должна называться get_car_list.
Для проверки работы своей реализации функции get_car_list и всех созданных классов вам необходимо использовать следующий csv-файл:
cars_week3.csv
Первая строка в исходном файле — это заголовок csv, который содержит имена колонок.
Нужно пропустить первую строку из исходного файла. Обратите внимание на то, что исходный файл с данными содержит некорректные строки, которые нужно пропустить. Если возникают исключения в процессе создания объектов из строк csv-файла, то требуется их корректно обработать стандартным способом. Проверьте работу вашего кода с входным файлом, прежде чем загружать задание для оценки.

(stepik_bio_spiral_matrix)
Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):

(stepik_bio_update_dictionary)
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value.
Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2∗key. Если и ключа 2∗key нет, то нужно добавить ключ 2∗key в словарь и сопоставить ему список из переданного элемента [value].
Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.

(stepik_bio_special_func)
Имеется реализованная функция f(x), принимающая на вход целое число x, которая вычисляет некоторое целочисленое значение и возвращает его в качестве результата работы.
Функция вычисляется достаточно долго, ничего не выводит на экран, не пишет в файлы и зависит только от переданного аргумента x.
Напишите программу, которой на вход в первой строке подаётся число n — количество значений x, для которых требуется узнать значение функции f(x), после чего сами эти n значений, каждое на отдельной строке. Программа должна после каждого введённого значения аргумента вывести соответствующие значения функции f на отдельной строке.
Для ускорения вычисления необходимо сохранять уже вычисленные значения функции при известных аргументах.
Обратите внимание, что в этой задаче установлено достаточно сильное ограничение в две секунды по времени исполнения кода на тесте.

(stepik_bio_school)
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк

(stepik_bio_orfog)
Простейшая система проверки орфографии основана на использовании списка известных слов. Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.
Напишем подобную систему.
Через стандартный ввод подаётся следующая структура: первой строкой — количество d записей в списке известных слов, после передаётся  d строк с одним словарным словом на строку, затем — количество l строк текста, после чего — l строк текста.
Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.

(stepik_bio_money_box)
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
Класс должен иметь следующий вид
class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        # положить v монет в копилку
При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True﻿.

(stepik_bio_gc)
GC-состав является важной характеристикой геномных последовательностей и определяется как процентное соотношение суммы всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности.
Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).

(stepik_bio_buffer_from_five)
Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из этой последовательности, затем сумму второй пятерки, и т. д.
Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части. Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.
Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок последовательных элементов по мере их накопления.
Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.
Класс должен иметь следующий вид
class Buffer:
    def __init__(self):
        # конструктор без аргументов
    def add(self, *a):
        # добавить следующую часть последовательности
    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены