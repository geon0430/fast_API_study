#!/bin/bash/i
curl -X GET http://192.168.10.10:10002/tudo -H "accept:application/json"
curl -X POST http://192.168.10.10:10002/tudo -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"id":1,"item":"First tudo is to finish this book!"}'
