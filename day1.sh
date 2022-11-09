#!/bin/sh

awk 'last && $0 > last {n++} {last=$0} END{ print(n) }'
