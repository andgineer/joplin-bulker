#!/usr/bin/env bash
#
curl -X POST http://localhost:41184/auth
echo

if [ $? -eq 0 ]; then
    echo "Use the 'auth_token' as 'token' in you API calls"
else
    echo "Please enable Web Clipper service - see in README.md how."
fi
