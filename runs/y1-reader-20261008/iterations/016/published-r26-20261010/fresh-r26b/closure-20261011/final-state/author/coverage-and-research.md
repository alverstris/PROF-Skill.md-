D016 author record — r26 fresh generation

Product: complete repository-native Markdown teaching, original mathematical figures, separate hints and full solutions. No bold/italic prose or Markdown headings in learner files. Explicit SASIS self-iteration: generated teaching must never be patched.

Input admission: input-admission.json and package-verification.json bind actual published r26 bytes, complete operational baseline and original six-page source. No earlier output/diagnosis was admitted before generation.

Declared capability and source map:
- C1: Build and interpret rectangle sums. Original PDF2, Figure1 and Example1; PDF3 Figure2. Use area = width × height, sum notation and monotonicity from baseline Mathematics splitlines36,48,96,132–152,434. Lesson PartA, P1.
- C2: Recover the x² limit from square layers and enclosing pyramids. Original PDF3 Figure3 and PDF4 first result. Pyramid volume is introduced as a geometry fact; similar-triangle sections and explicit height bands justify containment. Baseline similarity and volume scaling at36,48 support the representation; sum-of-squares at723 supplies a legitimate shorter check. Lesson PartB and Figure2.
- C3: Connect the x result, rectangle limits and area derivatives. Original PDF4 Example2, Figure4, derivative pattern. Baseline arithmetic sums136–152, differentiation256–308 and FTC336. Lesson PartC and PartD.
- C4: Construct/read a general equal-width sampled sum, state its existence condition, interpret the definite integral and sample independence. Original PDF5 Figure5 and definition. Baseline336 grants rectangle limits in well-behaved cases; newly explicit continuity condition and a usable algebraic check connect it here. Lesson PartD, Figure3, P2.
- C5: Distinguish signed integral, geometric area, average and units. Original PDF2 opening purpose and PDF5 area description need nonnegative qualification; baseline386,FM30 at737,Physics899 support exact distinctions. Lesson PartE, P3, P5.
- C6: Construct principal and simple-interest debt from a borrowing rate, including time-of-borrowing weight and discrete approximation. Original PDF5–6 Example3. Baseline unit reasoning36,574,879,899 and rate/area connections386,604 support accumulation; simple-interest law is explicitly introduced as the source's model. Lesson PartF, P4.

Original source observations:
- PDF1 is the OCW cover; PDF2–6 are teaching pages1–5. All pages were read as text and inspected as full raster images.
- PDF3 calls the comparison solids “prisms” but applies one-third base-area times height and draws pyramids. The teaching will identify square-based pyramids and establish their containment by the side lengths of every horizontal section, not only the appearance of a sketch.
- PDF6 labels total borrowed with dollars per year. Rate×time has dollars; the teaching will state that dimensional correction locally.
- PDF5's unrestricted area wording applies geometrically when f is nonnegative and bounds run left to right. The teaching will retain signed integration for changing sign.
- The fixed 12-month sum cannot itself have Δt→0. The teaching will first identify the monthly model, then replace12 by n and Δt by1/n for the continuous limit.

Supplemental official research:
Query: site.ocw.mit.edu definite integral continuous function Riemann sum partition single variable calculus.
Source: Gilbert Strang, Calculus, Chapter5, `5.5, MIT OCW RES.18-001 hosted PDF, https://ocw.mit.edu/courses/res-18-001-calculus-fall-2023/mitres_18_001_f17_ch05.pdf .
Actually inspected retrieved text: PDF27–30, especially printed pp256–258 (tool lines2647–2772), with adjacent context from printed254–259 returned by the tool. Screenshot calls returned references without visible raster payload here, so no visual inspection of this supplementary PDF is claimed.
Findings used: continuous functions on a finite closed interval have a common finite Riemann-sum limit; tags can be chosen anywhere in their own subintervals; continuity is sufficient rather than necessary, as a bounded step function shows. This supports a short introduced existence theorem, not a formal real-analysis proof requirement. The lecture remains the source of examples and geometry. No claims rely on nonprimary search hits.
Continuity operationalisation: f(u+h)→f(u) as h→0 within the interval, with one-sided endpoint approach. For the first polynomial case, difference2uh+h²→0 supplies a check. No formal epsilon-delta argument is required by the declared baseline.

Applicable teaching duties: T1–T12 all apply to this durable-study document. T5–T8 apply across C1–C6, with P1 early supported practice, P2 sample independence, P3 signed/average discrimination, P4 timing-weight construction and P5 later retrieval plus physical transfer. Hints and complete solutions must remain separate. No student observation or mastery claim is made.

Verification plan after freeze: full fresh SASIS reading; independent technical calculations before proposed answers; complete source/PROF audit; exact saved-figure inspection; actual GitHub expression, styling and navigation checks; affected earlier-case review; state helper topic/global checks. Pending evidence is not a pass.
