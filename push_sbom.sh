#!/usr/bin/bash

venv/bin/cyclonedx-py venv ./venv/ > bom.json
echo "Generated bom.json file"

if [ -z "$DTRACK_SERVER" ]
then
    echo "DTRACK_SERVER environment variable not set"
    exit 1
fi

if [ -z "$PROJECT_ID" ]
then
    echo "PROJECT_ID environment variable not set"
    exit 1
fi

if [ -z "$API_KEY" ]
then
    echo "API_KEY environment variable not set"
    exit 1
fi

if [ -e payload.json ]
then
    rm -f payload.json
    echo "Cleanup existing payload.json"
fi

cat << EOF > payload.json
{
   "project": "$PROJECT_ID",
   "bom": "$(cat bom.json |base64 -w 0)"
}
EOF
echo "Created new payload.json"

echo "🛸 Pushing the sbom to Dependency tracker"
curl -s -X "PUT" "http://${DTRACK_SERVER}/api/v1/bom" \
     -H "Content-Type: application/json" \
     -H "X-Api-Key: $API_KEY" \
     -d @payload.json && echo ""

if [ $? -gt 0 ]
then
    echo "❌ Could not push sbom"
    exit 1
fi
echo "✅ Pushed the sbom to Dependency tracker"
