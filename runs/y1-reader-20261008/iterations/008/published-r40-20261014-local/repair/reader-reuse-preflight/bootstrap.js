// Explicitly authorized once: load only the sealed non-subject operating instruction and operational adapter.
const KEY = "prof.reader.reuse.synthetic.r40.candidate1";
if (load(KEY) !== undefined) throw new Error("reader bootstrap already present; preserve it and stop");
const r = await tools.exec_command({cmd: "$v='C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r39/reader-reuse-candidate/verify_reuse.py'; if ((Get-FileHash -LiteralPath $v -Algorithm SHA256).Hash.ToLowerInvariant() -ne 'cc727c2b2b0fee7e1f5cb8ca71f6eff18fc2006cdc4654bd023f94de8cac209f') { throw 'verifier identity mismatch' }; & 'C:/Users/alver/AppData/Local/Programs/Python/Python314/python.exe' $v 'bootstrap' '429f43293a9069b2bc642e646e3399363416d100eb8dc4e86ec0906351def41d'", max_output_tokens: 18000});
if (r.exit_code !== 0 || r.session_id) throw new Error("reader bootstrap identity verification failed: " + r.output);
let p;
try { p = JSON.parse(r.output.trim()); } catch (_) { throw new Error("bootstrap output missing/truncated; preserve failure and stop"); }
if (!p || Object.keys(p).sort().join(",") !== "instruction,mode,schema,seal" || p.schema !== "prof-reader-reuse-proof-v1" || p.mode !== "bootstrap" || typeof p.instruction !== "string") throw new Error("invalid bootstrap proof shape");
if (!p.seal || p.seal.schema !== "prof-reader-reuse-store-v1" || p.seal.binding_sha256 !== "429f43293a9069b2bc642e646e3399363416d100eb8dc4e86ec0906351def41d" || typeof p.seal.adapter_source !== "string") throw new Error("invalid bootstrap seal");
store(KEY, p.seal);
text(p.instruction);
text({bootstrap_verified: true, binding_sha256: p.seal.binding_sha256, bootstrap_sha256: p.seal.bootstrap_sha256, short_call_sha256: p.seal.short_call_sha256, subject_retrieval: false});
