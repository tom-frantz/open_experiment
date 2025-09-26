-- \gexec
-- Sends the current query buffer to the server, then treats each column of each row of the query's output (if any) as a SQL statement to be executed.
SELECT 'CREATE DATABASE flagsmith'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'flagsmith')\gexec
