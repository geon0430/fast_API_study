BASE_PATH=$(dirname $(pwd))

docker run \
	-it
	--name geon-web \
	-p 10001:8888 \
 	-p 10002:8000 \
 	-p 10003:8080 \
 	-v /ldap/home/geon:/home \
	-v -v $BASE_PATH:/workspace \
	geon-web

