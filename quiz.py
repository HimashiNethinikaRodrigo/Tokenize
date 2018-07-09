from nltk.tokenize import word_tokenize

s="For most languages and particular domains within them there are unusual specific tokens that we wish to recognize as terms, such as the programming languages C++ and C#, aircraft names like B-52, or a T.V. show name such as M*A*S*H - which is sufficiently integrated into popular culture that you find usages such as M*A*S*H-style hospitals."

a=word_tokenize(s)
b=type(a)
print(a)
print(b)
print(len(a))
