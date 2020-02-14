Build the docker image:

`$ docker build --rm -f "dockerfile" -t microservicefromscratch:1.0 "."`

Run the container:

`$ docker run -p 5501:5501 --name microservice_from_scratch -d microservicefromscratch:1.0`

Test:

`$ curl http://127.0.0.1/foo/1` to get a foo

More examples to come
