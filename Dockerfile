## based on https://github.com/hypothesis/client/blob/master/Dockerfile
FROM alpine:3.10

RUN apk update && apk add --no-cache \
  git \
  make \
  nodejs \
  npm \
  yarn \
  bash sed grep


ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true

RUN set -ex \
 && pwd \
 && git clone https://github.com/hypothesis/client -b v1.470.0 \
 && cd client \
 && make build/manifest.json \
 && rm build/boot.js

COPY bake.py remove-share-links.sh ./
RUN ./remove-share-links.sh ./client/build


## Prepare an nginx image with the build included
FROM nginx:1.17

RUN set -e \
 && apt-get update \
 && apt-get install -qqy \
     python3 \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir /h-client
WORKDIR /h-client

COPY --from=0 client/build /h-client/build

COPY remove-share-links.sh bake.py nginx.conf docker-entrypoint.sh /h-client/
RUN ./remove-share-links.sh ./build

ENTRYPOINT ["/h-client/docker-entrypoint.sh"]
