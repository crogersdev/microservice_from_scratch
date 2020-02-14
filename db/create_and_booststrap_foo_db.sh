docker run
    docker run -d -P --name microservice_from_scratch_db \
    -e POSTGRES_PASSWORD=foo \
    -p 5432:5432 \
    postgres;

export PGPASSWORD=foo; psql -h 127.0.0.1 -U postgres -c "CREATE DATABASE foo;"
export PGPASSWORD=foo; psql -h 127.0.0.1 -U postgres -d foo << EOF
DROP TABLE foo;
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