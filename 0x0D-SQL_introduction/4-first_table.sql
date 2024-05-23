-- Ensure the existence of the first_table in the current database
CREATE TABLE IF NOT EXISTS first_table (
    id SERIAL PRIMARY KEY,
	name TEXT
);
