# Kafka Exercise Mono-Repo

Учебный монорепозиторий (этап 0): только каркас сервисов и инфраструктура запуска.

## Быстрый старт

1) Установить зависимости:

```
make install
```

2) Поднять сервисы в Docker:

```
make up
```

3) Проверить health эндпоинты:

```
curl http://localhost:8001/health
curl http://localhost:8002/health
curl http://localhost:8003/health
curl http://localhost:8004/health
```

Остановить окружение:

```
make down
```

## Полезные команды

```
make lint
make test
```
