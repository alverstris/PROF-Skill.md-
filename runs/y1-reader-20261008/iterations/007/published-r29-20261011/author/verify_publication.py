"""Fetch an exact commit and compare only explicit intended file identities."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

pin, mapping_file, receipt_file = sys.argv[1:]
repo = '/workspace/scratch/f9c0b7fc7e76/prof-iteration'
mapping = json.loads(Path(mapping_file).read_text())
subprocess.run(['git', '-C', repo, 'fetch', 'origin', pin], check=True)
requests = ''.join(pin + ':' + item['path'] + '\n' for item in mapping).encode()
raw = subprocess.run(['git', '-C', repo, 'cat-file', '--batch'], input=requests, stdout=subprocess.PIPE, check=True).stdout
position = 0
verified = []
for item in mapping:
    end = raw.index(b'\n', position)
    blob, kind, size = raw[position:end].decode().split()
    assert kind == 'blob', (item['path'], kind)
    position = end + 1
    actual = raw[position:position + int(size)]
    position += int(size)
    assert raw[position:position + 1] == b'\n'
    position += 1
    intended = Path(item['local']).read_bytes()
    assert actual == intended, item['path']
    verified.append({'path': item['path'], 'bytes': len(actual), 'sha256': hashlib.sha256(actual).hexdigest(), 'git_blob': blob})
assert position == len(raw)
head = subprocess.check_output(['git', '-C', repo, 'ls-remote', 'origin', 'refs/heads/main'], text=True).split()[0]
assert head == pin, (head, pin)
receipt = {'pin': pin, 'observed_main': head, 'exact_readback': True, 'file_count': len(verified), 'files': verified}
Path(receipt_file).write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'pin': pin, 'file_count': len(verified), 'exact_readback': True}))
