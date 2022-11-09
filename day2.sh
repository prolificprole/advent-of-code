#!/bin/sh

awk '/forward/{y+=$2} /up/{z-=$2} /down/{z+=$2} END{print(z*y)}'
