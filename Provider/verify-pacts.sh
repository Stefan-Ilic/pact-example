#!/bin/sh

pact-verifier --provider-base-url=http://localhost:8080 --pact-url=../Consumer1/consumer_1-provider.json
pact-verifier --provider-base-url=http://localhost:8080 --pact-url=../Consumer2/consumer_2-provider.json
pact-verifier --provider-base-url=http://localhost:8080 --pact-url=../Consumer3/consumer_3-provider.json