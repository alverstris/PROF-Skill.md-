const STEP_ID = "B001";
const cached = load("prof.reader.d008.r40.synthetic.preflight1");
if (typeof STEP_ID !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,63}$/.test(STEP_ID)) throw new Error("exactly one plain STEP_ID is accepted");
if (!cached || typeof cached !== "object" || Array.isArray(cached) || cached.schema !== "prof-reader-reuse-store-v1" || cached.binding_sha256 !== "240cdd7882e1c760003b948b0201a4c4a5448e9682a16393be5de3de5579d4d1") throw new Error("missing/stale reader bootstrap; preserve failure and stop");
const r = await tools.exec_command({cmd: "$v='C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r40/reader-preparation/synthetic-preflight-r40/verify_reuse.py'; if ((Get-FileHash -LiteralPath $v -Algorithm SHA256).Hash.ToLowerInvariant() -ne '31a821375e9bfd377040aa16a2236f67f0895b30753c9fb268a19c889de320a5') { throw 'verifier identity mismatch' }; & 'C:/Users/alver/AppData/Local/Programs/Python/Python314/python.exe' $v 'step' '240cdd7882e1c760003b948b0201a4c4a5448e9682a16393be5de3de5579d4d1' '" + STEP_ID + "'", max_output_tokens: 18000});
if (r.exit_code !== 0 || r.session_id) throw new Error("reader operational identity verification failed: " + r.output);
let p;
try { p = JSON.parse(r.output.trim()); } catch (_) { throw new Error("verification output missing/truncated; preserve failure and stop"); }
if (!p || Object.keys(p).sort().join(",") !== "mode,schema,seal,step_id" || p.schema !== "prof-reader-reuse-proof-v1" || p.mode !== "step" || p.step_id !== STEP_ID || JSON.stringify(cached) !== JSON.stringify(p.seal)) throw new Error("cached adapter/binding identity mismatch; preserve failure and stop");
// Only the exact verified operational source enters eval; STEP_ID is a parameter, never source text.
await eval("(async function(STEP_ID) {\n" + p.seal.adapter_source + "\n})(STEP_ID)");
