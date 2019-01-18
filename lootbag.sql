PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Children;
DROP TABLE IF EXISTS Toys;

CREATE TABLE 'Children' (
  'ChildId' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'Name'  TEXT NOT NULL,
  'Good' INTEGER NOT NULL DEFAULT 1 CHECK (Delivered BETWEEN 0 AND 1),
  'Delivered' INTEGER NOT NULL DEFAULT 0 CHECK (Delivered BETWEEN 0 AND 1)
);

INSERT INTO 'Children' VALUES (null, 'Bob', 1, 0 );
INSERT INTO 'Children' VALUES (null, 'Sue', 0, 0 );
INSERT INTO 'Children' VALUES (null, 'Mike', 1, 0 );
INSERT INTO 'Children' VALUES (null, 'Greg', 1, 1 );
INSERT INTO 'Children' VALUES (null, 'Fred', 1, 0 );
INSERT INTO 'Children' VALUES (null, 'Steve', 0, 0 );
INSERT INTO 'Children' VALUES (null, 'Sam', 1, 0 );
INSERT INTO 'Children' VALUES (null, 'Will', 1, 1 );

CREATE TABLE 'Toys' (
  'ToyId' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'ToyName'  TEXT NOT NULL,
  'ChildId' INTEGER NOT NULL,
  FOREIGN KEY('ChildId')
  REFERENCES 'Children' ('ChildId')
  ON DELETE CASCADE
 );


INSERT INTO 'Toys' VALUES (null, 'boat', 1);
INSERT INTO 'Toys' VALUES (null, 'doll', 2);
INSERT INTO 'Toys' VALUES (null, 'truck', 3);
INSERT INTO 'Toys' VALUES (null, 'car', 4);
INSERT INTO 'Toys' VALUES (null, 'watch', 2);
INSERT INTO 'Toys' VALUES (null, 'table', 5);
INSERT INTO 'Toys' VALUES (null, 'pills', 4);
INSERT INTO 'Toys' VALUES (null, 'cup', 5);
INSERT INTO 'Toys' VALUES (null, 'hat', 3);


-- `sqlite3 database.db < createdb.sql`