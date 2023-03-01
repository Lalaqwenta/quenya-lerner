DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS words;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS lesson_tags;

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  email TEXT UNIQUE NOT NULL,
  remember_token TEXT,
  password TEXT NOT NULL
);

CREATE TABLE exercises (
  id INTEGER PRIMARY KEY,
  question TEXT NOT NULL,
  answer TEXT NOT NULL,
  hint TEXT
);

CREATE TABLE words (
  id INTEGER PRIMARY KEY,
  english_meaning TEXT NOT NULL,
  english_translation TEXT NOT NULL,
  quenya_tengwar TEXT NOT NULL,
  quenya_transcription TEXT NOT NULL
);

CREATE TABLE lessons (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  exercise_ids TEXT NOT NULL,
  FOREIGN KEY (exercise_ids) REFERENCES exercises (id)
);

CREATE TABLE lesson_tags (
  id INTEGER PRIMARY KEY,
  tag_name TEXT NOT NULL,
  lesson_id INTEGER NOT NULL,
  FOREIGN KEY (lesson_id) REFERENCES lessons (id)
);

CREATE TABLE exercise_tags (
  id INTEGER PRIMARY KEY,
  tag_name TEXT NOT NULL,
  exercise_id INTEGER NOT NULL,
  FOREIGN KEY (exercise_id) REFERENCES exercises (id)
);

CREATE TABLE user_completed_lessons (
  user_id INTEGER,
  lesson_id INTEGER,
  PRIMARY KEY (user_id, lesson_id),
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (lesson_id) REFERENCES lessons (id)
);

CREATE TABLE user_completed_exercises (
  user_id INTEGER,
  exercise_id INTEGER,
  times_completed INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (user_id, exercise_id),
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (exercise_id) REFERENCES exercises (id)
);

-- Inserting the exercises first
INSERT INTO exercises (question, answer, hint) VALUES
("What is the Quenya word for 'star'?", "elen", "Think of the constellation Orion."),
("What is the Quenya word for 'tree'?", "alda", "This word is also the name of a character in The Silmarillion."),
("What is the Quenya word for 'water'?", "nen", "This word appears in many names of locations in Middle-earth."),
("What is the Quenya word for 'love'?", "melme", "This word shares the same root as the name of the Vala associated with love."),
("What is the Quenya word for 'sun'?", "anar", "This word appears in the name of the royal family of Gondor."),
("What is the Quenya word for 'moon'?", "isil", "This word appears in the name of the elf princess who loved Beren.");

-- Inserting two lessons using the exercises
INSERT INTO lessons (title, exercise_ids) VALUES
("Quenya Vocabulary Lesson 1", "1,2,3"),
("Quenya Vocabulary Lesson 2", "4,5,6");

-- Inserting test user
INSERT INTO users (username, email, password)
VALUES ('testuser', 'testuser@example.com', 'password');
