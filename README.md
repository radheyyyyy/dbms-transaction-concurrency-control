# 💳 Bank Transaction Concurrency System

A web-based banking system built using Flask and MySQL that demonstrates **transaction management** and **concurrency control** concepts in DBMS.

---

## 🚀 Features

- 💰 Money transfer between accounts
- 🔄 Transaction management (COMMIT / ROLLBACK)
- 🔒 Concurrency control using row-level locking (`FOR UPDATE`)
- ⚠️ Error handling (invalid user, insufficient balance)
- 🌐 Simple frontend using HTML

---

## 🧠 Concepts Covered

- ACID Properties
- Transaction Management
- Concurrency Control
- Row-Level Locking
- Database Consistency

---

## 🛠️ Technologies Used

- Python (Flask)
- MySQL
- HTML (Frontend)

---

## 🗄️ Database Setup

Run the following SQL queries in MySQL:

```sql
CREATE DATABASE bank_db;
USE bank_db;

CREATE TABLE accounts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    balance INT
);

INSERT INTO accounts (name, balance) VALUES
('Raj', 1000),
('Amit', 1000);
