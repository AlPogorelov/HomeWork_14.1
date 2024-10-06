# Проект "Домашее задание к уроку 14.1"

## Описание:

Проект содержит модули с реализованными классами Category и Product.
Так же в модуле `utils.py` реализована функция принимающая путь в json файлу и содание
объектов подходящего класса из списка словарей.

В проекте реализованы абстрактный класс BaseProduct который является родительским для класса Product,
Product родительским для классов Smartphone и LawnGrass.

Реализован миксин-класс MixinLogProduct который при создании объекта класса Product или его подклассов
в консоль будет выведена информация о объекте.

При создании пролукта с нулевым количеством возникает ошибка `'Товар с нулевым количеством не может быть добавлен'`.
При подсчете средней цены котегирри товара с пустым списком продуктов выводится `0`

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/AlPogorelov/HomeWork_14.1.git
```
## Тестирование:
Все модули и функции протестированы.