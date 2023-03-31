DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS words;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS user_tags;
DROP TABLE IF EXISTS word_tags;
DROP TABLE IF EXISTS lesson_tags;
DROP TABLE IF EXISTS exercise_tags;
DROP TABLE IF EXISTS user_completed_exercises;
DROP TABLE IF EXISTS user_completed_lessons;

-- TODO: Check if all these tables fields are in the same orders, as everywhere else!
-- That is important!
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  role TEXT NOT NULL DEFAULT 'user',
  username TEXT UNIQUE NOT NULL,
  email TEXT UNIQUE NOT NULL,
  -- remember_token TEXT,
  password TEXT NOT NULL
);

CREATE TABLE exercises (
  id INTEGER PRIMARY KEY,
  question TEXT NOT NULL,
  answer TEXT NOT NULL,
  type TEXT NOT NULL DEFAULT 'write',
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

CREATE TABLE tags (
    id INTEGER NOT NULL,
    tag VARCHAR(20),
    PRIMARY KEY (id)
);

CREATE TABLE lesson_tags (
    lesson_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY (lesson_id) REFERENCES lessons (id),
    FOREIGN KEY (tag_id) REFERENCES tags (id)
);

CREATE TABLE user_tags (
    user_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (tag_id) REFERENCES tags (id)
);

CREATE TABLE exercise_tags (
    exercise_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY (exercise_id) REFERENCES exercises (id),
    FOREIGN KEY (tag_id) REFERENCES tags (id)
);

CREATE TABLE word_tags (
    word_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY (word_id) REFERENCES words (id),
    FOREIGN KEY (tag_id) REFERENCES tags (id)
);


CREATE TABLE user_completed_lessons (
  user_id INTEGER,
  lesson_id INTEGER,
  -- completed_at DATETIME,
  times_completed INTEGER NOT NULL DEFAULT 0,
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
INSERT INTO exercises (type, question, answer, hint) VALUES
("choose one", "What is the Quenya word for 'star'?", "$<elen$>", "Think of the constellation Orion."),
("choose one", "What is the Quenya word for 'tree'?", "$<alda$>", "This word is also the name of a character in The Silmarillion."),
("choose one", "What is the Quenya word for 'water'?", "$<nen$>", "This word appears in many names of locations in Middle-earth."),
("choose one", "What is the Quenya word for 'love'?", "$<melme$>", "This word shares the same root as the name of the Vala associated with love."),
("choose one", "What is the Quenya word for 'sun'?", "$<anar$>", "This word appears in the name of the royal family of Gondor."),
("choose one", "What is the Quenya word for 'moon'?", "$<isil$>", "This word appears in the name of the elf princess who loved Beren.");

-- Inserting two lessons using the exercises
INSERT INTO lessons (title, exercise_ids) VALUES
("Quenya Vocabulary Lesson 1", "1,2,3"),
("Quenya Vocabulary Lesson 2", "4,5,6");

-- Inserting test user
INSERT INTO users (username, email, password, role) VALUES
('testuser', 'testuser@example.com', 'pbkdf2:sha256:260000$wD3bnaiOGoYvvNBc$6a16990013fa70b1037e991650ad74f80962e7cbee270e0f2768fa49d39b6650', 'user'), -- password
('adminuser', 'admin@admin.com', 'pbkdf2:sha256:260000$PwEWzufrvo5oeX2l$2dfea3cf9eb0d44897e177e04ac6283e2b7a249b7fe8e5f46a6f2fbdd0157307', 'admin'); -- adminpass

-- Inserting some words too
INSERT INTO words (english_meaning, english_translation, quenya_tengwar, quenya_transcription) VALUES
("star", "a celestial body that produces light", "$<elen$>", "elen"),
("tree", "a perennial plant with a single stem or trunk", "$<alda$>", "alda"),
("water", "a transparent, odorless, tasteless liquid", "$<nen$>", "nen"),
("love", "an intense feeling of affection and connection", "$<melme$>", "melme"),
("sun", "the star around which the Earth orbits", "$<anar$>", "anar"),
("moon", "the natural satellite of the Earth", "$<isil$>", "isil"),
("a", "the first letter of the English alphabet", "$<a$>", "anca"),
("b", "the second letter of the English alphabet", "$<b$>", "umbar"),
("c", "the third letter of the English alphabet", "$<c$>", "quesse"),
("d", "the fourth letter of the English alphabet", "$<d$>", "ando"),
("sword", "a weapon with a long metal blade and hilt", "$<anga$>", "anga"),
("rose", "a flowering shrub with thorns", "$<lote$>", "lótë"),
("mountain", "a large natural elevation of the earth's surface", "$<oron$>", "oron"),
("horse", "a large four-legged mammal", "$<rocco$>", "rocco");
