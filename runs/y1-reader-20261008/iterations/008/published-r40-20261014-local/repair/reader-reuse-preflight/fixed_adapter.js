// Paste this entire fixed adapter into functions.exec. Change STEP_ID only.
// The reader receives the bound adapter, not an invitation to modify its body.
const STEP_ID = "B001";
const PYTHON = "C:/Users/alver/AppData/Local/Programs/Python/Python314/python.exe";
const LAUNCHER = "C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r39/reader-reuse-candidate/fixed_launcher.py";
const RECEIPT = "C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r39/reader-reuse-candidate/record_receipt.py";
const ROUTE_SHA256 = "4847813692f422ef930c19cd3fd91505279f0d2ee16a47e2ec5a30ea1d1b1e41";

function requireValue(ok, message) { if (!ok) throw new Error(message); }
function utf8(s) {
  const out = [];
  for (const c of s) {
    const n = c.codePointAt(0);
    if (n < 128) out.push(n);
    else if (n < 2048) out.push(192 | (n >> 6), 128 | (n & 63));
    else if (n < 65536) out.push(224 | (n >> 12), 128 | ((n >> 6) & 63), 128 | (n & 63));
    else out.push(240 | (n >> 18), 128 | ((n >> 12) & 63), 128 | ((n >> 6) & 63), 128 | (n & 63));
  }
  return out;
}
const B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
function encode64(a) {
  let s = "";
  for (let i = 0; i < a.length; i += 3) {
    const v = (a[i] << 16) | ((a[i+1] || 0) << 8) | (a[i+2] || 0);
    s += B64[(v >>> 18) & 63] + B64[(v >>> 12) & 63] + (i+1 < a.length ? B64[(v >>> 6) & 63] : "=") + (i+2 < a.length ? B64[v & 63] : "=");
  }
  return s;
}
function decode64(s) {
  requireValue(typeof s === "string" && /^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/.test(s), "malformed base64 result");
  const out = [];
  for (let i = 0; i < s.length; i += 4) {
    const v = (B64.indexOf(s[i]) << 18) | (B64.indexOf(s[i+1]) << 12) | ((s[i+2] === "=" ? 0 : B64.indexOf(s[i+2])) << 6) | (s[i+3] === "=" ? 0 : B64.indexOf(s[i+3]));
    out.push((v >>> 16) & 255);
    if (s[i+2] !== "=") out.push((v >>> 8) & 255);
    if (s[i+3] !== "=") out.push(v & 255);
  }
  return out;
}
function sha256(input) {
  const k = [0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
  const h = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
  const a = input.slice(); const bitLength = a.length * 8; a.push(128);
  while (a.length % 64 !== 56) a.push(0);
  for (let i = 7; i >= 0; --i) a.push(Math.floor(bitLength / 2 ** (i * 8)) & 255);
  const rr = (x, n) => (x >>> n) | (x << (32-n));
  for (let p = 0; p < a.length; p += 64) {
    const w = new Array(64);
    for (let i=0;i<16;i++) w[i] = ((a[p+i*4]<<24)|(a[p+i*4+1]<<16)|(a[p+i*4+2]<<8)|a[p+i*4+3])|0;
    for (let i=16;i<64;i++) { const x=w[i-15], y=w[i-2]; w[i]=((rr(x,7)^rr(x,18)^(x>>>3))+w[i-16]+(rr(y,17)^rr(y,19)^(y>>>10))+w[i-7])|0; }
    let [aa,b,c,d,e,f,g,hh]=h;
    for (let i=0;i<64;i++) { const t1=(hh+(rr(e,6)^rr(e,11)^rr(e,25))+((e&f)^((~e)&g))+k[i]+w[i])|0; const t2=((rr(aa,2)^rr(aa,13)^rr(aa,22))+((aa&b)^(aa&c)^(b&c)))|0; hh=g;g=f;f=e;e=(d+t1)|0;d=c;c=b;b=aa;aa=(t1+t2)|0; }
    const v=[aa,b,c,d,e,f,g,hh]; for(let i=0;i<8;i++) h[i]=(h[i]+v[i])|0;
  }
  return h.map(n=>(n>>>0).toString(16).padStart(8,"0")).join("");
}
requireValue(sha256(utf8("abc")) === "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad", "adapter hash self-check failed");

async function recordReceipt(payload) {
  const encoded = encode64(utf8(JSON.stringify(payload)));
  const result = await tools.exec_command({cmd: `& '${PYTHON}' '${RECEIPT}' '${encoded}'`, max_output_tokens: 1500});
  requireValue(result.exit_code === 0 && !result.session_id, `receipt failure: ${result.output}`);
  const parsed = JSON.parse(result.output.trim());
  requireValue(parsed.ok === true, "receipt was not accepted");
  return parsed;
}

async function readerStep(stepId) {
  requireValue(typeof stepId === "string" && /^[A-Za-z][A-Za-z0-9_-]{0,63}$/.test(stepId), "only a single step ID is accepted");
  // No caller-selected subject filename, interpreter position, offset, or length.
  const result = await tools.exec_command({cmd: `& '${PYTHON}' '${LAUNCHER}' '${stepId}'`, max_output_tokens: 25000});
  requireValue(result.exit_code === 0 && !result.session_id, `launcher rejected/failed: ${result.output}`);
  let packet;
  try { packet = JSON.parse(result.output.trim()); }
  catch (_) { throw new Error("launcher output missing/truncated; preserve input failure, do not improvise access"); }
  requireValue(packet.schema === "sasis-step-result-v1" && packet.route_sha256 === ROUTE_SHA256 && packet.requested_step === stepId, "launcher output identity mismatch");
  if (packet.kind === "text") {
    const bytes = decode64(packet.bytes_b64);
    requireValue(bytes.length === packet.byte_length && sha256(bytes) === packet.sha256 && sha256(utf8(packet.text_utf8)) === packet.sha256, "text result extent/hash mismatch");
    text({step_id: stepId, file_id: packet.file_id, start: packet.start, byte_length: packet.byte_length, sha256: packet.sha256, baseline_revisit: packet.baseline_revisit});
    text(packet.text_utf8);
    await yield_control();
    await recordReceipt({stage: "text_output_delivered", route_sha256: ROUTE_SHA256, step_id: stepId, sha256: packet.sha256, byte_length: packet.byte_length, display_mechanism: "functions.text_then_yield_control"});
    return;
  }
  requireValue(packet.kind === "figure" && packet.complete_image_staged === true && packet.view_required === true && packet.cursor_after === packet.cursor_before, "invalid held figure packet");
  const common = {route_sha256: ROUTE_SHA256, step_id: stepId, nonce: packet.image_nonce, input_path: packet.image_path, input_sha256: packet.sha256, tool_name: "functions.view_image"};
  await recordReceipt({...common, stage: "view_invocation"});
  let viewed, match, imageBytes, displayMime;
  try {
    viewed = await tools.view_image({path: packet.image_path, detail: "original"});
    match = /^data:(image\/(?:png|jpeg|webp)|application\/octet-stream);base64,([A-Za-z0-9+/=]+)$/.exec(viewed.image_url || "");
    requireValue(match && viewed.detail === "original", "view tool returned no original complete image result; figure remains pending");
    imageBytes = decode64(match[2]);
    if (imageBytes.slice(0,8).join(",") === "137,80,78,71,13,10,26,10") displayMime = "image/png";
    else if (imageBytes[0] === 255 && imageBytes[1] === 216 && imageBytes[2] === 255) displayMime = "image/jpeg";
    else if (imageBytes.slice(0,4).join(",") === "82,73,70,70" && imageBytes.slice(8,12).join(",") === "87,69,66,80") displayMime = "image/webp";
    requireValue(displayMime && (match[1] === "application/octet-stream" || match[1] === displayMime), "view result MIME/signature mismatch; figure remains pending");
    requireValue(imageBytes.length === packet.byte_length && sha256(imageBytes) === packet.sha256 && displayMime === packet.mime_type,
      "actual view tool result differs from complete identified figure; figure remains pending");
  } catch (err) {
    await recordReceipt({...common, stage: "view_failed", error: String(err)});
    throw err;
  }
  const resultHash = sha256(imageBytes);
  await recordReceipt({...common, stage: "view_result", result_image_sha256: resultHash, result_image_bytes: imageBytes.length, result_mime_type: match[1], display_mime_type: displayMime, result_detail: viewed.detail});
  // The bytes are unchanged. Only a generic transport MIME is made explicit.
  image("data:" + displayMime + ";base64," + match[2], "original");
  text({step_id: stepId, figure_input_sha256: packet.sha256, displayed_tool_result_sha256: resultHash, semantic_inspection_claim: false});
  await yield_control();
  await recordReceipt({...common, stage: "image_output_delivered", result_image_sha256: resultHash, display_mechanism: "functions.image_then_yield_control", semantic_inspection_claim: false});
}

await readerStep(STEP_ID);
