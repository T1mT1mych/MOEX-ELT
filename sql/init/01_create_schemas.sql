-- Создает 4 схемы для 4 слоев: raw, staging, core, marts. 
-- Скрипт идемпотентный (т.е. его можно выполнять несколько раз без ошибок)

CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS core;
CREATE SCHEMA IF NOT EXISTS marts;