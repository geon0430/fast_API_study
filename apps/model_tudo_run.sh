#!/bin/bash

#chapter2
#curl -X POST  http://192.168.10.10:10002/tudo \
#	-H 'accept: application/json'\
#       	-H 'Content-Type: application/json'\
#       	-d '{"id": 1, "item": "Validation models help with input type"}'

#curl -X GET http://192.168.10.10:10002/tudo/1  \
#	-H 'accept: application/json'\
#       	-H 'Content-Type: application/json'\
#       	-d '{"id": 1, "item": "example schema!"}'

#curl -X PUT http://192.168.10.10:10002/tudo/1  \
#	-H 'accept: application/json'\
#       	-H 'Content-Type: application/json'\
#       	-d '{ "item": "next chapter"}'

#curl -X POST http://192.168.10.10:10002/tudo  \
#       	-H 'accept: application/json'\
#        -H 'Content-Type: application/json'\
#        -d '{"id": 1, "item": "example schema!"}'

#curl -X DELETE http://192.168.10.10:10002/tudo/1  \
#        -H 'accept: application/json'\

#curl -X GET http://192.168.10.10:10002/tudo/1  \
#        -H 'accept: application/json'\

# chapter 3
#curl -X POST http://192.168.10.10:10002/tudo  \
#               -H 'accept: application/json'\
#        -H 'Content-Type: application/json'\
#        -d '{"id": 1, "item": "this tudo will be retrieved without exposing my id!"}'

curl -X GET http://192.168.10.10:10002/tudo/12  \
        -H 'accept: application/json'

##
