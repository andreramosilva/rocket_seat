CREATE TABLE IF NOT EXISTS "pets" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT,
  "type" TEXT
);

CREATE TABLE IF NOT EXISTS "people" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" TEXT,
  "last_name" TEXT,
  "age" INTEGER,
  "pet_id" INTEGER,
  FOREIGN KEY ("pet_id") REFERENCES "pets" ("id")
);

INSERT INTO "pets" ("name", "type") 
VALUES 
('Fluffy', 'cat'),
('Fido', 'dog'),
('Mr. Nibbles', 'hamster'),
('Bubbles', 'fish'),
('Spike', 'dog'),
('Whiskers', 'cat'),
('Ginger', 'cat'),
('Smokey', 'cat'),
('Sassy', 'cat'),
('Polly', 'bird');

INTERT INTO 'people' ('first_name', 'last_name', 'age', 'pet_id')
VALUES 
('John', 'Doe', 30, 1),
('Jane', 'Doe', 25, 2),
('Alice', 'Smith', 45, 3),
('Bob', 'Smith', 50, 4),
('Charlie', 'Brown', 35, 5),
('Daisy', 'Johnson', 40, 6),
('Eve', 'Williams', 55, 7),
('Frank', 'Davis', 60, 8),
('Grace', 'Martinez', 65, 9),
('Hank', 'Rodriguez', 70, 10);