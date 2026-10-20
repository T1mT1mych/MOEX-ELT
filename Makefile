# Команды для выполнения в терминале
# Запуск: make <цель>, например: make up
# Без цели (make) будет выполнена цель по умолчанию (up)

.PHONY: up down ps logs psql sandbox

DB_NAME ?= moex_db

# Поднимает контейнеры в фоне
up:
	docker compose up -d

# Останавливает и удаляет контейнеры с сохранением данных в volumes
down:
	docker compose down

# Показывает список запущенных контейнеров
ps:
	docker compose ps

# Показывает логи контейнеров
logs:
	docker compose logs

# Подключается к базе данных через psql. Выйти "\q"
psql:
	docker exec -it moex-db psql -U postgres -d $(DB_NAME)

# Пересоздаёт схему sandbox в базе данных, удаляя все таблицы и данные в ней
sandbox:
	docker exec -i moex-db psql -U postgres -d $(DB_NAME) -v ON_ERROR_STOP=1 < sql/sandbox/first_steps.sql