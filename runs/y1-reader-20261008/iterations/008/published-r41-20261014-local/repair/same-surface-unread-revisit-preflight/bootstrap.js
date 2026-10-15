// Explicitly authorized once: load only the sealed non-subject operating instruction and operational adapter.
const KEY = "prof.reader.r41.unread_revisit.supplement1";
if (load(KEY) !== undefined) throw new Error("reader bootstrap already present; preserve it and stop");
const r = await tools.exec_command({cmd: "$v='C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r41/same-surface-unread-revisit-preflight/verify_reuse.py'; if ((Get-FileHash -LiteralPath $v -Algorithm SHA256).Hash.ToLowerInvariant() -ne 'cc729e4da5147be6e33fb379d67f7daf8f701cb9d159dba1f5b41d6c1ca9d495') { throw 'verifier identity mismatch' }; & 'C:/Users/alver/AppData/Local/Programs/Python/Python314/python.exe' $v 'bootstrap' 'fc7c189d364f94312fdf8daa781e0b1bcce24771942fd6fef7e9396d96d23188'", max_output_tokens: 18000});
if (r.exit_code !== 0 || r.session_id) throw new Error("reader bootstrap identity verification failed: " + r.output);
let p;
try { p = JSON.parse(r.output.trim()); } catch (_) { throw new Error("bootstrap output missing/truncated; preserve failure and stop"); }
if (!p || Object.keys(p).sort().join(",") !== "instruction,mode,schema,seal" || p.schema !== "prof-reader-reuse-proof-v1" || p.mode !== "bootstrap" || typeof p.instruction !== "string") throw new Error("invalid bootstrap proof shape");
if (!p.seal || p.seal.schema !== "prof-reader-invoker-store-v1" || p.seal.binding_sha256 !== "fc7c189d364f94312fdf8daa781e0b1bcce24771942fd6fef7e9396d96d23188" || typeof p.seal.adapter_source !== "string" || typeof p.seal.invoker_source !== "string") throw new Error("invalid bootstrap seal");
store(KEY, p.seal);
text(p.instruction);
text({bootstrap_verified: true, binding_sha256: p.seal.binding_sha256, bootstrap_sha256: p.seal.bootstrap_sha256, short_call_sha256: p.seal.short_call_sha256, invoker_sha256: p.seal.invoker_sha256, subject_retrieval: false});
