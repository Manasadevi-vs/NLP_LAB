#Q8 Slang Replacement (Object Standardization)
import re
text = input().lower()
d = {"u":"you","r":"are","btw":"by the way","idk":"i do not know"}
print(" ".join(d.get(w,w) for w in re.findall(r'\b\w+\b', text)))

#8a Slang + Emoji + Normalize
import re
t = input().lower()
d = {"u":"you","lol":"laughing","brb":"be right back","🙂":"smile"}
t = " ".join(d.get(w,w) for w in re.findall(r'\w+|🙂', t))
print(re.sub(r'([!?.])\1+', r'\1', t))

#8b Lowercase + Slang + Punctuation
import re
t = input().lower()
d = {"u":"you","r":"are","idk":"i do not know"}
t = " ".join(d.get(w,w) for w in re.findall(r'\b\w+\b', t))
print(re.sub(r'([!?.])\1+', r'\1', t))
