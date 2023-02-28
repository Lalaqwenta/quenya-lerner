DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS words;
DROP TABLE IF EXISTS completed_exercises;

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
  hint TEXT,
  user_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE words (
  id INTEGER PRIMARY KEY,
  english_meaning TEXT NOT NULL,
  english_translation TEXT NOT NULL,
  quenya_tengwar TEXT NOT NULL,
  quenya_transcription TEXT NOT NULL
);

CREATE TABLE completed_exercises (
  user_id INTEGER,
  exercise_id INTEGER,
  PRIMARY KEY (user_id, exercise_id),
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (exercise_id) REFERENCES exercises (id)
);
