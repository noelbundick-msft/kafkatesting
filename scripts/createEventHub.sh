#!/bin/bash
set -euo pipefail
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

set -o allexport; source .env; set +o allexport
az group create -g "${AZURE_RESOURCE_GROUP}" -l westus3
az deployment group create -g "${AZURE_RESOURCE_GROUP}" -f "${SCRIPT_DIR}/eh-kafka.bicep"
