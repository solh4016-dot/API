-- Script SQL equivalente a `python -m app.seed_data`.
-- Úsalo si prefieres crear la base desde MySQL Workbench.
DROP DATABASE IF EXISTS fakestore_clone;
CREATE DATABASE fakestore_clone CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE fakestore_clone;

CREATE TABLE users (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	email VARCHAR(120) NOT NULL, 
	username VARCHAR(60) NOT NULL, 
	password VARCHAR(120) NOT NULL, 
	firstname VARCHAR(60) NOT NULL, 
	lastname VARCHAR(60) NOT NULL, 
	phone VARCHAR(30) NOT NULL, 
	city VARCHAR(80) NOT NULL, 
	street VARCHAR(120) NOT NULL, 
	number INTEGER NOT NULL, 
	zipcode VARCHAR(20) NOT NULL, 
	lat VARCHAR(20) NOT NULL, 
	`long` VARCHAR(20) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE INDEX ix_users_id ON users (id);
CREATE UNIQUE INDEX ix_users_username ON users (username);

CREATE TABLE products (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	title VARCHAR(255) NOT NULL, 
	price FLOAT NOT NULL, 
	description TEXT NOT NULL, 
	category VARCHAR(80) NOT NULL, 
	image VARCHAR(500) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE INDEX ix_products_category ON products (category);
CREATE INDEX ix_products_id ON products (id);

INSERT INTO users (id, email, username, password, firstname, lastname, phone, city, street, number, zipcode, lat, `long`) VALUES (1, 'john@gmail.com', 'johnd', 'm38rmF$', 'john', 'doe', '1-570-236-7033', 'kilcoole', 'new road', 7682, '12926-3874', '-37.3159', '81.1496');
INSERT INTO users (id, email, username, password, firstname, lastname, phone, city, street, number, zipcode, lat, `long`) VALUES (2, 'morrison@gmail.com', 'mor_2314', '83r5^_', 'david', 'morrison', '1-570-236-7033', 'kilcoole', 'Lovers Ln', 7267, '12926-3874', '-37.3159', '81.1496');
INSERT INTO users (id, email, username, password, firstname, lastname, phone, city, street, number, zipcode, lat, `long`) VALUES (3, 'kevin@gmail.com', 'kevinryan', 'kev02937@', 'kevin', 'ryan', '1-567-094-1345', 'Cullman', 'Frances Ct', 86, '29567-1452', '40.3467', '-30.1310');
INSERT INTO users (id, email, username, password, firstname, lastname, phone, city, street, number, zipcode, lat, `long`) VALUES (4, 'don@gmail.com', 'donero', 'ewedon', 'don', 'romer', '1-765-789-6734', 'San Antonio', 'Hunters Creek Dr', 6454, '98234-1734', '50.3467', '-20.1310');
INSERT INTO users (id, email, username, password, firstname, lastname, phone, city, street, number, zipcode, lat, `long`) VALUES (5, 'derek@gmail.com', 'derek', 'jklg*_56', 'derek', 'powell', '1-956-001-1945', 'san Antonio', 'adams St', 245, '80796-1234', '40.3467', '-40.1310');
INSERT INTO users (id, email, username, password, firstname, lastname, phone, city, street, number, zipcode, lat, `long`) VALUES (6, 'david_r@gmail.com', 'david_r', '3478*#54', 'david', 'russell', '1-678-345-9856', 'el paso', 'prospect st', 124, '12346-0456', '20.1677', '-10.6789');
INSERT INTO users (id, email, username, password, firstname, lastname, phone, city, street, number, zipcode, lat, `long`) VALUES (7, 'miriam@gmail.com', 'snyder', 'f238&@*$', 'miriam', 'snyder', '1-123-943-0563', 'fresno', 'saddle st', 1342, '96378-0245', '10.3456', '20.6419');
INSERT INTO users (id, email, username, password, firstname, lastname, phone, city, street, number, zipcode, lat, `long`) VALUES (8, 'william@gmail.com', 'hopkins', 'William56$hj', 'william', 'hopkins', '1-478-001-0890', 'mesa', 'vally view ln', 1342, '96378-0245', '50.3456', '10.6419');
INSERT INTO users (id, email, username, password, firstname, lastname, phone, city, street, number, zipcode, lat, `long`) VALUES (9, 'kate@gmail.com', 'kate_h', 'kfejk@*_', 'kate', 'hale', '1-678-456-1934', 'miami', 'avondale ave', 345, '96378-0245', '40.12456', '20.5419');
INSERT INTO users (id, email, username, password, firstname, lastname, phone, city, street, number, zipcode, lat, `long`) VALUES (10, 'jimmie@gmail.com', 'jimmie_k', 'klein*#%%*', 'jimmie', 'klein', '1-104-001-4567', 'fort wayne', 'oak lawn ave', 526, '10256-4532', '30.24788', '-20.545419');

INSERT INTO products (title, price, description, category, image) VALUES ('Disco duro portátil 2TB USB 3.0', 64.99, 'Almacenamiento externo compacto, compatible con PC, Mac y consolas. Velocidad de transferencia de hasta 5 Gbps.', 'electronics', 'https://picsum.photos/seed/producto1/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('SSD interno 1TB SATA III', 109.0, 'Unidad de estado sólido de alto rendimiento para acelerar el arranque y la carga de aplicaciones.', 'electronics', 'https://picsum.photos/seed/producto2/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Memoria USB 128GB', 18.5, 'Memoria flash compacta con carcasa metálica y conexión USB 3.2.', 'electronics', 'https://picsum.photos/seed/producto3/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Monitor curvo 27 pulgadas 144Hz', 399.99, 'Panel VA curvo Full HD con tasa de refresco de 144Hz, ideal para gaming y trabajo multitarea.', 'electronics', 'https://picsum.photos/seed/producto4/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Audífonos inalámbricos con cancelación de ruido', 129.9, 'Bluetooth 5.3, hasta 30 horas de batería y micrófono integrado para llamadas.', 'electronics', 'https://picsum.photos/seed/producto5/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Anillo de plata esterlina con circonia', 45.0, 'Anillo ajustable en plata 925 con piedra central de circonia cúbica.', 'jewelery', 'https://picsum.photos/seed/producto6/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Collar de oro laminado con dije de corazón', 78.5, 'Cadena de 45 cm con dije de corazón, acabado en oro laminado de 18k.', 'jewelery', 'https://picsum.photos/seed/producto7/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Pulsera de acero inoxidable', 32.0, 'Pulsera unisex resistente al agua y al desgaste, cierre de seguridad.', 'jewelery', 'https://picsum.photos/seed/producto8/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Aretes de perla cultivada', 59.9, 'Aretes clásicos con perla de agua dulce y base de plata.', 'jewelery', 'https://picsum.photos/seed/producto9/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Chamarra impermeable ligera para hombre', 84.0, 'Chamarra cortavientos con capucha plegable y bolsillos con cierre.', 'men''s clothing', 'https://picsum.photos/seed/producto10/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Playera de algodón manga corta', 15.99, 'Playera básica de algodón peinado, corte regular, disponible en varios colores.', 'men''s clothing', 'https://picsum.photos/seed/producto11/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Pantalón de mezclilla slim fit', 49.5, 'Jeans de corte ajustado con elástico para mayor comodidad.', 'men''s clothing', 'https://picsum.photos/seed/producto12/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Sudadera con capucha unisex', 39.0, 'Sudadera de felpa suave con bolsillo canguro y puños acanalados.', 'men''s clothing', 'https://picsum.photos/seed/producto13/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Vestido casual de verano floral', 42.0, 'Vestido ligero de tirantes con estampado floral, ideal para clima cálido.', 'women''s clothing', 'https://picsum.photos/seed/producto14/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Blusa de manga larga con botones', 27.5, 'Blusa de tela fluida con cuello camisero, versátil para oficina o diario.', 'women''s clothing', 'https://picsum.photos/seed/producto15/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Leggings deportivos de cintura alta', 24.9, 'Leggings elásticos y transpirables, con bolsillo lateral para el celular.', 'women''s clothing', 'https://picsum.photos/seed/producto16/400/400');
INSERT INTO products (title, price, description, category, image) VALUES ('Abrigo largo de lana mezclada', 119.0, 'Abrigo elegante con solapa y cinturón, forro interior suave.', 'women''s clothing', 'https://picsum.photos/seed/producto17/400/400');
