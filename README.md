# Yandex Music Discord RPC

[![N|Solid](https://i.imgur.com/sDQBibw.png)](https://i.imgur.com/sDQBibw.png)

Yandex Music Discord RPC - простой RPC для Discord, показывающий, что вы слушаете на данный момент в Yandex Music (Яндекс.Музыка). 

## Функции

- Показывает название трека, исполнителя
- Показывает обложку сингла/альбома
- При наведении на логотип Yandex Music - показывает длительность трека
- Кнопка "Слушать" переводит Вас на страницу с треком

## Установка

- `git clone https://github.com/lodo4nik/Yandex-Music-Discord-RPC`
    >Замечание: Если отсутствует git, скачайте архив
- `cd Yandex-Music-Discord-RPC`
- `pip install -r requirements.txt`
- Указываем acces_token в файл `config.py`
- `python3 main.py

## Важно
- У Вас должен быть установлен Discord

## FAQ
> **Где получить acces_token?** 
Об этом можно узнать в документации библиотеки [Yandex Music API](https://yandex-music.readthedocs.io/en/main/token.html)

>**С какой задержкой обновляется трек?**
По умолчанию - 3 секунды. Указать свою задержку можно в `main.py`

>**Остались вопросы?**
Напишите в Discord: `лодка#4433`

## Лицензия
**Yandex Music Discord RPC** распространяется под лицензией GPL-3.0. Подробнее в файле [LICENSE](https://github.com/lodo4nik/Yandex-Music-Discord-RPC/blob/main/LICENSE)__
**Yandex Music API** - LGPL-3__
**Яндекс.Музыка** - [Ссылка](https://yandex.ru/legal/music_mobile_agreement/)

>**Оригинальный код написан NeyQ и распространяется под лицензией Apache**. Ссылка на репозиторий: https://github.com/NeynQ/Discord-YM-RPC