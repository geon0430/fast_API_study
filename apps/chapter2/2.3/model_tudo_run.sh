#!/bin/bash/
curl -X POST http://192.168.10.10:10002/tudo -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"id": 1, "item": "SomeName"}'
