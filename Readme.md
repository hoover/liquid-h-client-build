# Pre-built Hypothesis client
This repository contains the build of the [Hypothesis
client](https://github.com/hypothesis/client) for inclusion in the [Liquid app
bundle](http://github.com/Liquidinvestigations/node).

### Running the server
This will bake the Hypothesis client for hypothesis.liquid.example.org and
start an nginx server on port 8000:
```shell
docker run \
  --env LIQUID_DOMAIN=liquid.example.org \
  --env LIQUID_HTTP_PROTO=https \
  --publish 8000:80 \
  liquidinvestigations/h-client
```
