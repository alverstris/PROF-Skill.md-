(async function retainedReaderInvoker(STEP_ID) {
if (arguments.length !== 1) throw new Error("exactly one STEP_ID datum is accepted");
const cached = load("prof.reader.r41.unread_revisit.supplement1");
if (typeof STEP_ID !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,63}$/.test(STEP_ID)) throw new Error("exactly one plain STEP_ID is accepted");
if (!cached || typeof cached !== "object" || Array.isArray(cached) || cached.schema !== "prof-reader-invoker-store-v1" || cached.binding_sha256 !== "fc7c189d364f94312fdf8daa781e0b1bcce24771942fd6fef7e9396d96d23188") throw new Error("missing/stale reader bootstrap; preserve failure and stop");
const r = await tools.exec_command({cmd: "$v='C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r41/same-surface-unread-revisit-preflight/verify_reuse.py'; if ((Get-FileHash -LiteralPath $v -Algorithm SHA256).Hash.ToLowerInvariant() -ne 'cc729e4da5147be6e33fb379d67f7daf8f701cb9d159dba1f5b41d6c1ca9d495') { throw 'verifier identity mismatch' }; & 'C:/Users/alver/AppData/Local/Programs/Python/Python314/python.exe' $v 'step' 'fc7c189d364f94312fdf8daa781e0b1bcce24771942fd6fef7e9396d96d23188' '" + STEP_ID + "'", max_output_tokens: 18000});
if (r.exit_code !== 0 || r.session_id) throw new Error("reader operational identity verification failed: " + r.output);
let p;
try { p = JSON.parse(r.output.trim()); } catch (_) { throw new Error("verification output missing/truncated; preserve failure and stop"); }
if (!p || Object.keys(p).sort().join(",") !== "mode,schema,seal,step_id" || p.schema !== "prof-reader-reuse-proof-v1" || p.mode !== "step" || p.step_id !== STEP_ID || JSON.stringify(cached) !== JSON.stringify(p.seal)) throw new Error("cached adapter/binding identity mismatch; preserve failure and stop");
// Only the exact verified operational source enters eval; STEP_ID is a parameter, never source text.
await eval("(async function(STEP_ID) {\n" + p.seal.adapter_source + "\n})(STEP_ID)");

})
