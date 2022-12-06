# yamdb_final
yamdb_final

![example workflow](https://github.com/DanilBelyaev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание
Api_yamdb - проект, в котором пользователи могут делиться отзывами о художественных произведениях при помощи API. В данном репозитории выполнена настройка Continuous Integration и Continuous Deployment (CI и CD) для проекта.


### Используемые технологии

1. Python 3.7.9 
2. Django 3.2.15
3. Django REST framework (https://ilyachch.gitbook.io/django-rest-framework-russian-documentation/overview/readme)
4. SQLite3 (https://pythonru.com/osnovy/sqlite-v-python)
5. Docker (https://www.docker.com)
6. nginx (https://nginx.org/ru/)
7. GIT (https://github.com/git-guides)
8. Яндекс Облако (https://cloud.yandex.ru/?utm_source=yandex-s&utm_medium=cpc&utm_campaign=Search_RU_Other_All_LGEN_Brand_cloud|62006544&utm_content=4569625732|&utm_term=яндекс%20облако|12696174758&etext=2202.CHqAmnRpD76g7K1u7TrkLhQ-QETV8neZB_mOCH4eu7BxYnpndXpieGFkb3BuY3Z5.a6341bc960772459c252bd404366e1d189b53448&yclid=7207798833538192605)



### Документация и возможности API:
К проекту подключен redoc. Для просмотра документации используйте эндпойнт `redoc/`

[Добавлена менеджмент команда, для выгрузки данных в БД, из csv.](#описание-команды-для-заполнения-базы-данными)

### Шаблон наполнения .env (не включен в текущий репозиторий) расположенный infra/.env
В данном файле не стоит меньше параметры DB_HOST, DB_PORT, DB_ENGINE.

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Автоматизация развертывания серверного ПО
Для развертывания API на серверах используется среда Docker, а также docker-compose. Docker позволяет устаналивать приложение со всем его окружением и зависимостями в контейнер, который может быть перенесён на любую систему, а также предоставляет среду по управлению контейнерами. Соответствущие Dockerfile и docker-compose могут быть найдены в корне проекта и в папке infra соответственно.

IP: 158.160.14.6

Для ознакомления с функционалом api можно обратиться к файлу README.md в репозитории https://github.com/DanilBelyaev/infra_sp2

### Автор проекта
Беляев Данил, студент яндекс практикума 39-ой когорты (email: danil.belyaev08@gmail.com)
