import re 
def split_text(text): 

    pattern = r"[^\w]+" 
    words = re.split(pattern, text) 
    words = [word for word in words if word] 
    return words 
input_text = """This is a sample text,.""" 
result = split_text(input_text) 
print(result)