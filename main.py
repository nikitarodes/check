import asyncio
from telethon import TelegramClient

# сюда свои данные апи вводи
api_id = ...
api_hash = ...

# создаем нового клиента тг
client = TelegramClient('session_name', api_id, api_hash)

#заход в систему
client.start()

# переменные
search_query = ''
filename = ''

# функция для поиска сообщений в одном диалоге
async def search_dialog(dialog, search_query, filename):
    async for message in client.iter_messages(dialog.id, filter=lambda m: search_query in m.message):
        # сохраняем результаты 
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f'ID чата: {dialog.id}\n')
            file.write(f'ID сообщения: {message.id}\n')
            file.write(f'Автор: {message.sender.first_name}\n')
            file.write(f'Текст сообщения: {message.text}\n\n')

# основной цикл работы
while True:
    # очистка экрана
    print('\033[H\033[J')

    # запрашиваем ввод от пользователя
    print('=' * 50)
    print('Поиск сообщений в Телеграм')
    print('=' * 50)
    search_query = input('Введите текст для поиска: ')
    print(f'Ищем сообщения по запросу: {search_query}')

    # создаем текстовый файл для сохранения результатов
    filename = input('Введите имя файла для сохранения результатов: ')
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f'Результаты поиска для запроса: {search_query}\n\n')

    # список всех диалогов пользователя
    dialogs = client.get_dialogs()

    # запускаем функцию поиска сообщений в каждом диалоге
    tasks = [search_dialog(dialog, search_query, filename) for dialog in dialogs]
    asyncio.run(asyncio.gather(*tasks))

    # окончание поиска и сохранения результатов
    print('-' * 50)
    print(f'Результаты поиска сохранены в файле: {filename}')
    print('-' * 50)

    # запрашиваем продолжение поиска
    continue_search = input('Хотите выполнить еще один поиск? (Да/Нет): ')
    if continue_search.lower() != 'да':
        break

    # запрашиваем имя файла для сохранения результатов второго поиска
    filename = input('Введите имя файла для сохранения результатов второго поиска: ')

# заверщенре скрипта
print('\033[H\033[J')
print('=' * 50)
print('Завершение работы скрипта')
print('=' * 50)

# закрываем соединение
client.disconnect()
#enitns
