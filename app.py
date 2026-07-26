CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50),
  email VARCHAR(100) UNIQUE,
  phone VARCHAR(20),
  password VARCHAR(255),
  balance DECIMAL(10,2) DEFAULT 0.00
);

CREATE TABLE transactions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  type VARCHAR(10), -- deposit or withdraw
  amount DECIMAL(10,2),
  date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
