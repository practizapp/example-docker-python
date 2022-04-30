# Example Express Docker

This is a hello world app that is written in [Node.js](https://nodejs.org/) using [Express](https://expressjs.com/) framework, packaged using [Docker](https://www.docker.com/).

## Running

There are 2 build modes for building this image, "development" and "production", It's up to the developers to define how their apps would behave under development environment and production environment. For example, development mode may use [SQLite](https://www.sqlite.org/) as a database whereas in production, the app will use [PostgreSQL](https://www.postgresql.org/).

Because this is just a hello world app, For the sake of simplicity, setting the build mode to "development" or "production" will not change the app behavior.

### Development

```
docker compose up --build
```

### Production

```
docker compose --file docker-compose.prod.yml up --build
```

## Customizing

Docker images can be customized using environment variables or customized during build time using build arguments.

### Environment Variables

No environment variables available.

### Build Arguments

| Key | Description |
| --- | --- |
| `NODE_VERSION` | The version of Node.js that will be used for building this image. |