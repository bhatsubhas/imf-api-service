#!/usr/bin/bash

while [ $# -gt 0 ]
do
    case $1 in
        --verbose)
          VERBOSE=1
          shift
          ;;
    *)
        echo "Unknown option: $1"
        echo "Usage: $0 [--verbose]"
        exit 1
        ;;
     esac
done

info() {
    echo "$1"
    echo ""
}

verbose() {
    if [ -n "$VERBOSE" ]
    then
        echo "📜 $1"
        echo ""
    fi
}

if [ -f .env ]
then
    verbose "Found .env file, sourcing it"
    source .env
else
    verbose "No .env file found, expecting env variables to be set"
fi

if [ -z "$DTRACK_SERVER" ]
then
    info "DTRACK_SERVER environment variable not set"
    exit 1
fi

if [ -z "$PROJECT_ID" ]
then
    info "PROJECT_ID environment variable not set"
    exit 1
fi

if [ -z "$API_KEY" ]
then
    info "API_KEY environment variable not set"
    exit 1
fi

verbose "Generating bom.json file"
venv/bin/cyclonedx-py venv ./venv/ > bom.json
verbose "Generated bom.json file"

if [ -e payload.json ]
then
    verbose "Cleanup existing payload.json"
    rm -f payload.json
fi

cat << EOF > payload.json
{
   "project": "$PROJECT_ID",
   "bom": "$(cat bom.json |base64 -w 0)"
}
EOF
verbose "Created new payload.json"

info "🛸 Pushing the sbom to Dependency tracker"
curl -s -X "PUT" "http://${DTRACK_SERVER}/api/v1/bom" \
     -H "Content-Type: application/json" \
     -H "X-Api-Key: $API_KEY" \
     -d @payload.json && echo ""

if [ $? -gt 0 ]
then
    info "⛔ Failed to push sbom to Dependency tracker"
    verbose "Removing generated bom.json and payload.json files"
    rm -rf bom.json payload.json
    exit 1
fi
info "✅ Pushed the sbom to Dependency tracker"
