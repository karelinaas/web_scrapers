# Сравнение времени отработки библиотек для http-запросов: requests, aiohttp, httpx
Для видео на канале IT POP: 

---

### О приложении

Репозиторий представляет собой main-скрипт, запускающий в зависимости от передаваемого параметра тот или иной веб-скрэпер.

- требуется Python 3.12 + `poetry`
- установка зависимостей: `poetry install`
- запуск с помощью команды `poetry run python main.py`

Запуск скрипта без аргументов (или с `all`) запустит поочередно все скрэперы. Аргументы для запуска отдельных скрэперов:

- `aiohttp` – на основе библиотеки [aiohttp](https://github.com/aio-libs/aiohttp)
- `httpx` – на основе библиотеки [httpx](https://github.com/encode/httpx)
- `requests` – на основе библиотеки [requests](https://pypi.org/project/requests/)
- `requests_multi` – на основе библиотеки [requests](https://pypi.org/project/requests/) + с использованием мультитрединга

Пример:

```shell
poetry run python main.py httpx
```

### Структура репозитория

- main-скрипт [main.py](main.py)

- Модуль [scrapers](scrapers) содержит базовый абстрактный класс для всех скрэперов, а также его конкретные реализации.

- Модуль [demo_utils](demo_utils) содержит вспомогательные методы для вывода информации о работе скрэперов на экран (время выполнения и др.).

- Файл [constants.py](constants.py) содержит константы для настройки работы выполнения:
  - `BASE_URL` – базовый url сервиса, к эндпоинтам которого обращаемся
  - `GET_REQUESTS_URLS` – список эндпоинтов, получаемых http-методом GET; для всех скрэперов, кроме `scrapers.requests_based.RequestsBasedScraper`, умножается на 6
  - `POST_REQUESTS_DATA` – список кортежей: эндпоинт и отправляемые по нему данные, для отправки http-методом POST; для всех скрэперов, кроме `scrapers.requests_based.RequestsBasedScraper`, умножается на 10
  - `MAX_WORKERS` – кол-во воркеров для `ThreadPoolExecutor` (для `requests_multi`)
