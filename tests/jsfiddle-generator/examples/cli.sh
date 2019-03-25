#!/usr/bin/env bash
{ set +x; } 2>/dev/null

cd "$(mktemp -d)" || exit
( set -x; python -m jsfiddle_generator . ) || exit
( set -x; find "$PWD" ) || exit
( set -x; cat demo.details )
