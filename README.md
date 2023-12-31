# BITLY
## Описание
Проект создан для сокращения или подсчета кликов по ссылке. Для получения сокращенной ссылки необходимо передать программе ссылку для сокращения. В ином случае, если вы хотите узнать сколько раз переходили по вашей ссылке, необходимо передать сокращенную ссылку.
## Установка
Скачайте необходимые файлы, затем используйте `pip`(или `pip3`, если есть конфликт с Python2) для установки зависимостей и установить зависимости. Зависимости можно установить командой, представленной ниже.

Установите зависимости командой:

```
pip install -r requirements.txt
```
## Пример запуска скрипта
Для запуска скрипта у вас уже должно быть установлен Python3.

Дляполучения сокращенной ссылки, необходимо написать команду в таком формате:

```
python main.py --url https://translate.google.ru
```
После аргумента `--url` необходимо указать ссылку для работы кода, документацию можно найти на сайте [Сократить ссылку BITLY](https://gist.github.com/dvmn-tasks/58f5fdf7b8eb61ea4ed1b528b74d1ab5)

Для получения количества кликов, необходимо написать команду в таком формате:

```
python main.py --url bit.ly/3uujaSR
```
## Переменные окружения
Часть настроек проекта береться из переменных окружения. Переменные окружения - это переменные, значения которых присвайваются программе Python извне. Чтобы их определить создайте файл .env рядом с main.py и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Пример  сожержания файла .env:

```
BITLY_TOKEN=21ecde8d68b8de54395928e7e4199dd8e27f9e78
```

Получить токен BITLINK можно на сате [BITLY](https://bitly.com/a/oauth_apps).

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
