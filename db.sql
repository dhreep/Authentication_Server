CREATE TABLE IF NOT EXISTS Login
(
  Username VARCHAR NOT NULL,
  Password VARCHAR NOT NULL,
  IP VARCHAR NOT NULL,
  Key NUMERIC,
  PRIMARY KEY (Username),
  UNIQUE (IP)
);