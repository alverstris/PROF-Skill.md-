Domain patterns

Read only the domain relevant to the requested lesson. These examples illustrate the authoring decisions; they are not required content or evidence of particular learner mistakes.

Physics and mathematics

Choose an output such as constructing a model, interpreting a quantity, selecting a method, or testing whether a proposed solution satisfies the governing conditions. Preserve the intended course's notation and convention. An explanatory intermediate representation is allowed when it helps, provided its map back to the course form is explicit and checked before assessed use. Follow the course-first clarification rule in execution-protocol.md when the intended definition cannot be established; do not resolve an unknown course choice by silently changing notation.

At a representation change, connect the old description to the new components and show that it preserves the operation or relation. For an operator matrix, apply the operator to stated basis inputs, extract output coefficients and justify their column placement. State orthonormality or any other assumption needed for the rules in use. Distinguish an operator action from time evolution, an amplitude from a probability, and an expectation value from a definite eigenvalue when these distinctions matter to the task.

Teach both reading the resulting matrix's action and constructing it from a stated action. Explain the roles and grouping of indices and components, separating mathematical rules, representation conventions and the chosen physical example. Changing the operator's action can then test the same construction rule without requiring a new physical theory. A symbol glossary alone does not supply that rule.

Avoid explaining an unfamiliar word using only a neighbouring technical term: “orthonormal means unit norm and orthogonal” needs the meaning of the component/inner-product relation for a novice; “expectation” needs its measurement interpretation. Explain enough for the next use rather than opening every adjacent subject.

A useful application might change a symmetry assumption and ask whether an earlier shortcut survives. A trivial variation might repeat the same solved arithmetic. A task that adds nonorthogonal bases, dynamics and band theory simultaneously may require splitting into connected units.

Do not use a real symmetric matrix's transpose as a diagnostic for row/column confusion: it is unchanged. Check a proposed construction against its action on a basis input. Check dimensions, limiting cases, normalization and conventions when relevant.

Programming

Start from a useful behaviour the learner wants to implement and their stated programming knowledge. Explain the unfamiliar API through input, returned object, state changes and an observable result. When two objects expose different identifier attributes, explain what those objects are rather than merely listing the attribute names.

Teach the minimal running environment and execution path needed for the example. Check current official API documentation or the provided version. Prefer a small runnable example, a meaningful modification and an independent feature or debugging task to a catalogue of every method. Separate a conceptual gap from a typo, environment issue or unavailable dependency.

At an unfamiliar form, distinguish a function definition or documented signature from a call, map arguments to parameters, and show the concrete shape of relevant returned values before accessing them. For compound expressions, explain which attribute, call or indexing operation acts on which intermediate object. Do not infer types or relationships from similar names.

For example, when teaching an expression such as `action.triggered.connect(show_ready)`, first establish the action and the function, then connect these three sources of information:

| Source | Teaching obligation |
| --- | --- |
| Python rules | Show attribute access and the outer call's grouping. The parentheses call `connect`; the argument expression `show_ready` supplies the function object. Trace an added call's effect through its returned value rather than teaching a blanket ban on parentheses. |
| Library contract | Verify and explain what `triggered` provides, what `connect` accepts and does, and how the eventual invocation occurs. Delayed execution is a consequence of that contract, not a special property of passing any function as an argument. |
| Example choices | Explain where `action` and `show_ready` were bound, why this function was selected and which locally chosen names or operations can be changed consistently. Library member names cannot be freely renamed like local variables. |

An expanded equivalent can expose an intermediate object before reconnecting the full expression; explain the intermediate object's role rather than merely introducing another name. Then work from a requested behaviour back to a valid expression and give a meaningful modification using the same reading rules. Keep this an illustration of the method, not a mandatory Anki lesson or a substitute for checking the actual binding and version. A new API with familiar syntax usually needs its signature, contract and changed assumptions, without repeating the entire structural explanation.

Anki-like task example: inspect a returned deck structure, distinguish a tree node from a stored deck object, then implement a requested traversal. Do not fabricate a stable API or assume a method mutates state without checking.

Language

Select a communicative aim, such as expressing who misses whom, making a request or explaining a plan in an appropriate register. Build from intended roles to natural wording. Supply incidental vocabulary, pronoun meanings and question frames when those are not the learning target. A production task can be a short meaningful exchange; it need not be an unrestricted conversation.

After feedback, change the situation or communicative role. Distinguish an error in meaning/roles from agreement, spelling or unknown vocabulary. Do not claim that written success establishes spontaneous speaking or that a vocabulary retrieval study proves grammatical fluency.

Example: after teaching “Tu me manques” and the role of me/te, ask for a short message that includes the reverse relationship. Later change the absent person to a place. Do not require a human or native reviewer as a dependency; use reliable sources and explain genuine uncertainty when needed.

Research and modelling

For a request based only on a lab, professor, project name or research interest, establish the context before selecting what to teach:

1. Resolve the intended group using the named institution and available conversation context. A short identifier or acronym may be ambiguous; do not silently pick a different lab. Ask only for the missing identifier if that ambiguity cannot be resolved and would change the lesson.
2. Use web tools to read the official group/institution pages, relevant project descriptions and selected representative papers or preprints, including recent work where current activity matters. Check dates and affiliation; the newest paper is not necessarily the best teaching anchor. Read the sources themselves rather than relying on search snippets. Use methods sections, associated code and documentation when they materially determine the techniques to teach; an abstract alone supports only its stated claims. If a source is inaccessible, use another credible source or limit the claims to what was actually accessible.
3. Map a verified research question to the methods it uses, the prerequisites those methods require and a useful learner capability. For example, a verified study using Bloch simulations and numerical optimisation can motivate teaching the simulated quantities, objective and validation logic. The mere presence of the word MRI on a lab page does not establish a particular project or implementation.
4. Find accessible foundational explanations for that prerequisite chain, such as university course material, authoritative textbooks or official technical documentation. Research papers often assume exactly the knowledge the learner lacks. Reconstruct the teaching at the learner's starting level, with worked reasoning and appropriately sized applications.
5. State the proposed scope briefly and cite the facts supporting its relevance. Distinguish what the group demonstrably studies from what a prospective student might need and from what their actual project requires. Do not imply a project is available, assigned or agreed, or that particular equipment, software or tasks will be used, without evidence.

Stop expanding the search when the intended scope, principal methods and necessary foundations are sufficiently supported and no unresolved issue would materially change the lesson. Do not turn every source-free request into a survey of the group's entire publication history. If only partial information is accessible, teach the supported core and identify the particular unverified link; do not invent project details or refuse all useful foundational teaching. Supply a complete document rather than requiring the learner to read the selected papers first.

Bring an application forward: state a model assumption, obtain a prediction, then change an input, compare a competing model or identify evidence that would distinguish them. References and numerical tools are legitimate parts of independent research use.

Give enough background to interpret the experiment or computation, including the objective, parameters, outputs and validation criterion. Do not hide a required premise in optional reading. If actual scanner, laboratory or external-system use is involved, respect the task's existing authorization and operating constraints; a teaching example is not permission to operate equipment.

Repair and transfer across domains

If a learner fails, locate the earliest missing bridge, teach it differently and return to the coherent task. Avoid multiplying near-identical questions. If fragments succeed but integration fails, replace some fragments with an integrated application. If a proposed alternative is valid, show when it is useful; if it fails, identify the violated condition. Curiosity is not itself an error.
