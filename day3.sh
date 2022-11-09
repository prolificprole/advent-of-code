#!/bin/sh

awk -vFS="" '{for(i=1;i<=NF;i++) a[i]+=$i; n=NF} END{for(i=1;i<=n;i++) { v = !!(a[i] > NR/2); e = e*2+!v;g = g*2+v; } print(g*e)}'
