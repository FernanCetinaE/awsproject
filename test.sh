#!/bin/sh

# Set the default URI if no argument is provided
default_uri="http://localhost:4000/api"

# Check if an argument is provided and set the URI accordingly
if [ -n "$1" ]; then
    uri="$1"
else
    uri="$default_uri"
fi

docker run -it --rm -v $(pwd):/app -v maven-repo:/root/.m2 -w /app maven:3-eclipse-temurin-8 mvn -Duri="$uri" clean test
