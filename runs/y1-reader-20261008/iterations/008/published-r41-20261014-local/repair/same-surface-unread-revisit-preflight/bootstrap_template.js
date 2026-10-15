// Explicitly authorized once: load only the sealed non-subject operating instruction and operational adapter.
const KEY = "__STORE_KEY__";
if (load(KEY) !== undefined) throw new Error("reader bootstrap already present; preserve it and stop");
const r = await tools.exec_command({cmd: "__VERIFY_COMMAND__ 'bootstrap' '__CORE_SHA256__'", max_output_tokens: 18000});
if (r.exit_code !== 0 || r.session_id) throw new Error("reader bootstrap identity verification failed: " + r.output);
let p;
try { p = JSON.parse(r.output.trim()); } catch (_) { throw new Error("bootstrap output missing/truncated; preserve failure and stop"); }
if (!p || Object.keys(p).sort().join(",") !== "instruction,mode,schema,seal" || p.schema !== "prof-reader-reuse-proof-v1" || p.mode !== "bootstrap" || typeof p.instruction !== "string") throw new Error("invalid bootstrap proof shape");
if (!p.seal || p.seal.schema !== "prof-reader-invoker-store-v1" || p.seal.binding_sha256 !== "__CORE_SHA256__" || typeof p.seal.adapter_source !== "string" || typeof p.seal.invoker_source !== "string") throw new Error("invalid bootstrap seal");
store(KEY, p.seal);
text(p.instruction);
text({bootstrap_verified: true, binding_sha256: p.seal.binding_sha256, bootstrap_sha256: p.seal.bootstrap_sha256, short_call_sha256: p.seal.short_call_sha256, invoker_sha256: p.seal.invoker_sha256, subject_retrieval: false});
