-- Ejecutar en la MISMA base MySQL configurada en Render, si se prefiere migrar manualmente.
CREATE TABLE IF NOT EXISTS carts (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  date DATETIME NOT NULL,
  INDEX ix_carts_user_id (user_id),
  CONSTRAINT fk_carts_user FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE TABLE IF NOT EXISTS cart_lines (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  cart_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  INDEX ix_cart_lines_cart_id (cart_id),
  CONSTRAINT fk_cart_lines_cart FOREIGN KEY (cart_id) REFERENCES carts(id) ON DELETE CASCADE
);
