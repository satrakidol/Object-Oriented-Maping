* create virtual environment, activate and install requirements

```bash
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

* run

```bash
cp .env.example .env

python -m flask --app main run
gunicorn main:app --bind 0.0.0.0:5000
```


## docker
```bash
docker build -t myflask .

docker run --env-file=.env --net=host -v $(pwd)/dbdata:/data/dbdata myflask
```

### docker-compose

```bash
docker-compose up --build
```
## Links

* [SQLite Viewer for VSCode](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer)
* [SQLAlchemy basic Relationships](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)
* [SQLAlchemy ORM tutorial](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
* [PostgreSQL VSCode Extension](https://marketplace.visualstudio.com/items?itemName=ckolkman.vscode-postgres)
