
# Assignment (Ahmed Nafies)

This micro service handles the following:
* Calculating a Fibonacci number F(n) with the value of n provided by the user.
* The Ackermann function A(m,n) with values of m and n provided by the user.
* The factorial of a non-negative integer n provided by the user.

## Built with

[Fast API](https://fastapi.tiangolo.com/) - one the fastest python framework according to [techempower.com](https://www.techempower.com/benchmarks/#section=data-r18&hw=ph&test=db&l=zijzen-f) web framework benchmark 

### Build and run using docker

```sh
$ docker-compose up --build
```

### Build and run without docker

make sure that `pipenv` is installed

Install dependencies
```sh
$ pipenv install
```

run
```sh
$ pipenv run python main.py
```

or run using uvicorn

```sh
$ pipenv run uvicorn main:app
```
Or if you're developing in vscode you can just press `F5` to run the server

### Running tests with docker

```sh
docker-compose run web pytest 
```

run with coverage
```sh
docker-compose run web pytest --cov
```
### Running tests without docker

```sh
$ pipenv run pytest
```

run with coverage

```sh
$ pipenv run pytest --cov
```
