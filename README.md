
# Assignment (Ahmed Nafies)

This micro-service handles the following:
* Calculating a Fibonacci number F(n) with the value of n provided by the user.
* The Ackermann function A(m,n) with values of m and n provided by the user.
* The factorial of a non-negative integer n provided by the user.

### Built with

[Fast API](https://fastapi.tiangolo.com/) - one the fastest python frameworks according to [techempower.com](https://www.techempower.com/benchmarks/#section=data-r18&hw=ph&test=db&l=zijzen-f) web framework benchmark 

## Install & Run

### using docker

```sh
$ docker-compose up --build
```
server will be running on [localhost:8000](http://localhost:8000)

### without docker

make sure that `pipenv` is installed

Install dependencies
```shs
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

server will be running on [localhost:8000](http://localhost:8000)

## Tests

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

### API documentation

* /docs - Open-API 3.0 (Swagger) documentation
* /redoc - Redoc documentation

## Future Improvements

### Factorial and Fibonacci
* storing values in an in-memory db like memcached or redis instead of global variables


### Monitoring
For now I am just returning the time taken to execute the function,
but the problem is we don't know if for example it is faster or slower than before because
we are not storing this data anywhere.

- I think is better to use APM (Application performance monitoring) with ELK (Elasticsearch, Logstash and Kibana)
There is a lot of docker images which contain ELK with APM server, however, I would need to write my own client though since clients only exist for Django and Flask.

- I am not sure if I can make it pre configured, so that when someone would clone my repo, he does not need to 
configure APM himself.

- It felt as if ELK and APM is a bit to much for just monitoring this app (it is like trying to hammer a nail with a bazooka)

- Maybe it would be easier to just use InfluxDB (time series database) with Grafana to display results. 
and it would be great if it can be pre-configured as well.

### CI/CD
I was not sure I was allowed to push to github, however, I would have used CircleCI
and lets say we deploy to Heroku, I would have used heroku for continuous deployment.

### Code documentation
I would use sphinx to generate code documentation and use readthedocs.
I think i have seen somewhere readthedocs docker image so that it can be used locally.


### Server
Using nginx as a reverse proxy.
FastAPI supports asynchronicity, so probably it is a good option to take advantage of that

### Testing
Now I have 99% test coverage, AMAZING RIGHT? no it is not.
In fact I think that there are tons of corner cases that are not covered by my tests.
I have recently read about mutation testing and in fact there is a couple of 
good packages available `cosmic ray`, `mutmut` and `mutpy`.
I am thinking about trying `mutmut` to be honest.


### Thank you note 
I know README is not the place for this
This has been one of the best code assignments I have ever got,
looks simple at the first sight but optimizing code is a fun challenge.
So Kudos to you guys.
