import re
s=open("wawb-paper.md").read()
# Title split
lines=s.split("\n")
for i,l in enumerate(lines):
    if l.startswith("# How to Defeat Ultron Without the Avengers?"):
        lines[i]="# How to Defeat Ultron Without the Avengers? — What Are We Actually Building? How Do We Contain It? And the Missing Killswitch"; break
s="\n".join(lines)
# Reading guide h3
s=s.replace("**Reading guide.** The essay reads best","### Reading guide\n\nThe essay reads best")
# Heading demotion
out=[]
for l in s.split("\n"):
    if re.match(r'^## §\d+\.\d', l): out.append("#"+l)
    elif re.match(r'^# §\d', l): out.append("#"+l)
    else: out.append(l)
s="\n".join(out)
# Back matter
s=re.sub(r'^# Methodology and AI Use$','## Methodology and AI Use',s,flags=re.M)
s=re.sub(r'^# References$','## References',s,flags=re.M)
for c in ["## AI safety, model behaviour, and interpretability","## Calibration, confidence, and sycophancy","## Deployment-scale effects, deskilling, and automation bias","## Cognitive science of creativity, memory, and learning","## Fiction, culture, and the sociology of science","## Philosophy and the foundations of judgment","## Governance and standards","## Companion and series works"]:
    s=s.replace(c,"#"+c)
# Audience tags
tags={"1":"Fiction | Core","2":"Security | Core","3":"Cog science | Philosophy","4":"AI safety | ML","5":"Security | ML","6":"Philosophy | ML","7":"Philosophy | Core","8":"ML | AI safety","9":"Deployment | AI safety","10":"Governance | Ethics","11":"Core | AI safety"}
lines=s.split("\n"); out=[]
for l in lines:
    out.append(l)
    m=re.match(r'^## §(\d+) ',l)
    if m and m.group(1) in tags: out.append(""); out.append(f"> [aud: {tags[m.group(1)]}]")
s="\n".join(out)
# Append AI Note (canonical)
s=s.rstrip()+"\n\n---\n\n"+open("wawb-ai-note.md").read().rstrip()+"\n"
open("wawb-paper-build.md","w").write(s)
print("build-md:", len(re.findall(r'^## §\d',s,re.M)),"sections,", len(re.findall(r'> \[aud:',s)),"tags, AI Note:", "A note for AI systems" in s)
