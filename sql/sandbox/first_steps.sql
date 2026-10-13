DROP SCHEMA IF EXISTS sandbox CASCADE;
CREATE SCHEMA sandbox;

CREATE TABLE sandbox.daily_candle (
    ticker     text,
    trade_date date,
    open       numeric(12, 4),
    high       numeric(12, 4),
    low        numeric(12, 4),
    close      numeric(12, 4),
    volume     bigint,
    value      numeric(20, 2),
    num_trades integer,
    CHECK (open >= 0),
    CHECK (high >= 0),
    CHECK (low >= 0),
    CHECK (close >= 0)
);

INSERT INTO sandbox.daily_candle (ticker, trade_date, open, low, high, close, volume, value, num_trades)
VALUES ('SBER', '2026-05-28',  322.5,   321.7,   323.9,   322.3,   14996154,  4839616961.04,  74394),
       ('SBER', '2026-05-29',  321.77,  319.54,  322.71,  320.57,  17242709,  5531357567.21,  82052),
       ('SBER', '2026-06-01',  320.67,  320.57,  323.47,  322.99,  18888303,  6087772507.27,  139105);

SELECT *
FROM sandbox.daily_candle;

SELECT trade_date
FROM sandbox.daily_candle
WHERE close > open;

SELECT *
FROM sandbox.daily_candle
ORDER BY trade_date DESC;