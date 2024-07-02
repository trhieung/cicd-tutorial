# cicd-tutorial

## help cmd
docker compose up -d --build

docker compose down

### db cml
PGPASSWORD=postgres psql -h localhost -p 5432 -U postgres

cmd                     |   purpose
-----------------------------------------------------------------
\dn                     |   List all scheme
\dt (or \dt *.*)        |   Table in in all schemas
\dt public.*            |   List all table in scheme name=public

