DROP TABLE IF EXISTS products_categories, products, categories, manufacturers, vendors;

CREATE TABLE vendors (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
	website VARCHAR(50)
);

CREATE TABLE manufacturers (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    website TEXT
);

CREATE TABLE categories (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Создание таблицы "Товары".
CREATE TABLE products (
    id BIGSERIAL PRIMARY KEY, -- первичный ключ
    name TEXT NOT NULL, -- название товара
    price INT CHECK(price > 0), -- цена (гарантируется, что цена > 0)
    vendor_id BIGINT REFERENCES vendors(id), -- ссылка на продавца
    manufacturer_id BIGINT REFERENCES manufacturers(id) -- ссылка на производителя
);
-- Создание индекса для ускорения поиска по названию товара.
CREATE INDEX product_name_idx ON products(name);

CREATE TABLE products_categories (
    id BIGSERIAL PRIMARY KEY,
    product_id BIGINT REFERENCES products(id),    
    category_id BIGINT REFERENCES categories(id)
);

-- Очистка всех таблиц перед наполнением тестовыми данными.
TRUNCATE TABLE products_categories, categories, manufacturers, vendors, products;

-- Наполнение таблиц тестовыми данными.
INSERT INTO categories(name) VALUES
    ('Музыкальные инструменты'), ('Профессиональное музыкальное оборудование'), ('Любительское музыкальное оборудование');
INSERT INTO vendors(name) VALUES('Музторг'), ('4 четверти');
INSERT INTO manufacturers(name, website) VALUES
    ('Fender', 'fender.com'), ('Gibson','gibson.com'), ('Roland', 'roland.com');
INSERT INTO products(name, price,  vendor_id, manufacturer_id) VALUES
    ('Fender Stratocaster', 3500000, 2, 1),
    ('Fender Telecaster', 3900000, 2, 1),
    ('Fender Bullet', 1200000, 2, 1),
    ('Gibson Les Paul', 5700000, 1, 2);
INSERT INTO products_categories(product_id, category_id) VALUES
    (1, 1), (1, 2), (3, 1), (3, 3);
	
