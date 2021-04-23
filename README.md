Assignment

### Run unittest for Boyer-Moore

- The procedure is the same

```bash
$ PIPENV_VENV_IN_PROJECT=true pipenv shell
```

```bash
$ pipenv install --dev
```
- and run tests
```bash
$ pipenv run unittest
```

### SQL Test

```bash
$ docker-compose up db
```
- Connect to test database on Postgresql server using psql

```bash
$ docker-compose exec db psql -U postgres test
```

- Execute SQL file

```bash
$ docker-compose exec db psql -v ON_ERROR_STOP=1 -U postgres test -a -f "sql/schema.sql"
```

- Testing using database

```bash
$ docker-compose up dbtest
```
