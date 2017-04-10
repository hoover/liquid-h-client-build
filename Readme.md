# Pre-built Hypothesis client
This repository contains the build of the [Hypothesis
client](https://github.com/hypothesis/client) for inclusion in the [Liquid app
bundle](http://github.com/Liquidinvestigations/setup).

### Building the client
```shell
git clone https://github.com/hypothesis/client.git
cd client
make
cd ..
rm -rf build
cp -a client/build ./
rm build/boot.js
```
