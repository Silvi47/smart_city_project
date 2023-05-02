# smart_city_project

## Get Started

1. Create virtual environment

```bash
virtualenv env
```

2. Enter the virtual environment
For Windows

```bash
env\Scripts\activate
```

## Installation

```bash
pip install -r requirements.txt
```

## Migrating to alembic

1. Initialize alembic
```bash
alembic init alembic
```

2. Open alembic.ini file and change the syntax below to your database: 
```bash
sqlalchemy.url = driver://user:pass@localhost/dbname
```

3. Create database

4. Migrating database to alembic
```bash
alembic revision -m "create table pegawai"
```
