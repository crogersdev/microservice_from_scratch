Run these commands from the `ops` folder.

Build the web app docker image:

`$ ./build_foo_docker_image.sh`

Run the stack:

`$ docker-compose up`

Bootstrap the database (only needs to happen once), found in the `db` folder:

`$ ./bootstrap_foo_db.sh`

Test:

`$ curl http://127.0.0.1/foo/1` to get a Foo

`$ curl -X POST http://127.0.0.1:5501/foo --data '{"foo": "foo_attr"}'` to create a new Foo

More to comegit