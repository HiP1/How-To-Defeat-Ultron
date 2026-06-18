import { readFileSync, writeFileSync } from 'node:fs';
const [,, file, kind] = process.argv;  // kind = 'paper' | 'appendices'
let s = readFileSync(file, 'utf8');
const css = readFileSync('overrides.css', 'utf8');

// 1. Inject override CSS before the closing </style>
s = s.replace('</style>', css + '\n  </style>');

if (kind === 'appendices') {
  // 2. Rename long appendix section ids to clean #appendix-x
  const renames = {
    'appendix-a-the-catalogue-case-by-case': 'appendix-a',
    'appendix-b-pattern-matrix': 'appendix-b',
    'appendix-c-fiction-cognition-and-recursive-safety-frames': 'appendix-c',
    'appendix-d-research-extensions': 'appendix-d',
  };
  for (const [long, short] of Object.entries(renames)) {
    s = s.replaceAll(`id="${long}"`, `id="${short}"`);
    s = s.replaceAll(`href="#${long}"`, `href="#${short}"`);
  }
  // 3. Wire back-links to the paper
  s = s.replaceAll('PAPER_URL_PLACEHOLDER', 'wawb-paper.html');
}

if (kind === 'paper') {
  // Tag the paragraph holding the final-line (setup sentence + quoted code).
  s = s.replace(
    /<p>(A note written by the author[^]*?<\/code>(?:&quot;|")?)<\/p>/,
    '<p class="final-line-p">$1</p>'
  );

  // Move the surrounding quotes inside the <code> so they share its styling.
  s = s.replace(
    /&quot;<code>(just tell it to act as Jarvis[^]*?)<\/code>&quot;/,
    '<code>&quot;$1&quot;</code>'
  );
  // Put the quoted final line on its own line beneath the colon.
  s = s.replace('put it in fewer words:  &quot;', 'put it in fewer words:<br>&quot;');
  s = s.replace('put it in fewer words: &quot;', 'put it in fewer words:<br>&quot;');
  s = s.replace('put it in fewer words:   &quot;', 'put it in fewer words:<br>&quot;');
  // 5. Wire links to the appendices file
  s = s.replaceAll('APPENDICES_URL_PLACEHOLDER', 'wawb-appendices.html');
}

writeFileSync(file, s, 'utf8');
console.log(`post-processed ${file} (${kind})`);
