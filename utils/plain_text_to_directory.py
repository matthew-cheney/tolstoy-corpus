
ptFile = 'working_files/albert_plain_text.txt'
outDir = 'final_source_files/Albert'

with open(ptFile, 'r') as f:
    pt = f.read()

chapters = pt.split('CHAPTER-BREAK')

import os

if not os.path.isdir(outDir):
    os.mkdir(outDir)

# Print title page
with open(f'{outDir}/_title.txt', 'w') as f:
    print(chapters[0].strip(), file=f)

# Print chapters
for i, chapter in enumerate(chapters[1:-1]):
    with open(f'{outDir}/chapter_{i:02d}.txt', 'w') as f:
        print(chapter.strip(), file=f)

# Print footnotes
with open(f'{outDir}/_footnotes.txt', 'w') as f:
    print(chapters[-1].strip(), file=f)
