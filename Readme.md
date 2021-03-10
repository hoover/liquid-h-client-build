# Pre-built Hypothesis client
This repository contains the build of the [Hypothesis
client](https://github.com/hypothesis/client) for inclusion in the [Liquid app
bundle](http://github.com/Liquidinvestigations/node).


## List of changes

Check the git history, there hasn't been a rebuild for this client in 3 years.

Changes done include:
- removing of facebook and twitter links (with sed)

    find . -type f -exec sed -i "s/www.facebook.com/::invalid::/g" {} \;
    find . -type f -exec sed -i "s/mailto:?subject/::invalid::/g" {} \;
    find . -type f -exec sed -i "s/plus.google.com/::invalid::/g" {} \;
    find . -type f -exec sed -i "s/twitter.com/::invalid::/g" {} \;


- replace instances of upstream domain name with our template (with sed, see bake.py on how the templates are filled)

## Building

First clone upstream and checkout the ancient version that we run:

```bash
git clone https://github.com/hypothesis/client

git checkout 1b956cf64
```

Then you'd need a time machine to flip back to 2018, since 2021 tooling on debian 10 doesn't seem to work anymore...



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
