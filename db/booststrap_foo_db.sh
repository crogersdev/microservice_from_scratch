export PGPASSWORD=foo;
psql -h 127.0.0.1 -U postgres -c "DROP DATABASE IF EXISTS foo;"
psql -h 127.0.0.1 -U postgres -c "CREATE DATABASE foo;"
export PGPASSWORD=foo; psql -h 127.0.0.1 -U postgres -d foo << EOF
DROP TABLE IF EXISTS foo;
CREATE TABLE foo (
    foo_id SERIAL PRIMARY KEY,
    foo_name varchar(64),
    foo_description varchar(255)
);
INSERT INTO foo (foo_name, foo_description)
VALUES
('premier', 'the very first foo'),
('alice', 'another foo created by alice'),
('bob', 'bob''s foo'),
('charlotte', 'charlotte''s foo');
EOF