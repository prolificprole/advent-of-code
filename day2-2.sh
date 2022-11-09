#!/bin/sh

awk '/forward/{y+=$2;z+=aim*$2} /up/{aim-=$2} /down/{aim+=$2} END{print(z*y)}'
