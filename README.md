# Url Shortener

The url shortener frontend is written in React with Typescript. The primary reason for react is something I'm familar with. Other alternatives on the frontend I'd have a look at with more time is Flutter and Vue. The reasoning for Typescript is the great tooling that comes with it, in my experience it removes a lot of the obvious mistakes and improves development speed. 

The backend is written in Python and uses [FastAPI](https://fastapi.tiangolo.com/) which allows for fast iterations and have gained quite a lot of traction in the Python community. One of the great things with FastAPI is the documentation that is auto-generated that comes with it.

## Running the application

You can either run the frontend and backend individually or both of them through docker compose.
For running them individually see respective sub directory README.

### Docker compose
The easiest to run the application is through [docker-compose](https://docs.docker.com/compose/).

Simply navigate to the root directory of the repository (assuming you have docker running) and run
```bash
docker-compose up
```

You can now reach the application on http://localhost:3000/
If you'd like to directly call the backend you can now find documentation under http://localhost:8080/docs 

## Shortcuts

### Database
I've intentionally not attached a "real" database such as PostgreSQL but rather just store each call in memory. This means on restart that the previous data will be lost. There are two reasons behind this decision.

1. Time, I sadly don't have the time to add it. See [another example](https://github.com/Oscmage/case/blob/main/docker-compose.yml#L22) where I've done so.
2. There is not an immediate need to get early feedback on the application to have a database. 

### Formatting and other checks

For both the backend and the frontend there are checks that I'd add to a project that is supposed to be production ready. Examples of that is formatting such as `black` and `prettier` but also `mypy` and `pylint`.

### Tests

I've done limited testing, especially on the frontend side where I'd have to freshen up the best practices.