# GrabberTelegramm
pip install telethon

# Получение / Регистрация API Telegram. https://my.telegram.org/
Если вы впервые регаете api телеграма, запустите скрипт
у вас спросит номер телефона от аккаунта, введите его и затем код отправленный вам в приложение, эта процедура делается всего один раз.

Здесь же создается еще один файл в данном случае myGrab.session
название файла берется из

``client = TelegramClient('myGrab', api_id, api_hash)``

этот файл всегда должен находится в одной директории со скриптом
и как только появится "Граббер запущен" - Закройте скрипт и запустите его только через пару часов.
иначе ваш аккаунт может отлететь в **БАН.**

После этого запускайте и держите скрипт рабочим хоть 24/7

Если ваш канал публичный т.е имеется ссылка в виде @fisting, Вместо ID просто вставляем его туда за кавычки
my_channel_id = '@fisting'
