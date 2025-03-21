### start steps
- clone to local dir
- make sure docker engine works
- edit all the config files in ./devcontainer(python version etc.)
- reopen in container

### install poetry

```
pip install poetry
```

### add dependancies

```
poetry add requests
poetry add --group dev pytest # so that py test
```

then we see the poetry.lock, this lock is amazing


### install

```
poetry install
poetry install --without dev
```