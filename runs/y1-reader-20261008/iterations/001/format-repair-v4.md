D001 destination-normalisation repair, v3 to v4

The v3 GitHub response contains all249inline and39display renderer elements and restores all previously lost thin-space commands. Two renderer inputs differ after ordinary HTML parsing: P26 greater-than is still entity text, and P07 aligned row separators gain an extra backslash at source newlines. Whether GitHub's client corrects these was unverified; this is not a claim of an observed v3 visual failure.

V4 avoids those two destination-sensitive forms: TeX gt names the same greater-than relation; each aligned row separator is followed by a space and its next alignment marker on the same source line. The math rows, order, operands, relation and every prose character remain unchanged. The exact inverse transformation restores v3.

The actual frozen v4 GitHub markup must be checked before dispatching its fresh SASIS reader. Existing independent technical evidence remains applicable to these identical mathematical meanings. No substantive PROF teaching-rule edit is warranted by this format repair.
