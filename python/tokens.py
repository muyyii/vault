import re

TOKEN_RX = r"""(?xm)
    (?P<string> ".*?"|'.*?'             )|
    (?P<float>  \d*(\d\.|\.\d)\d*       )|
    (?P<int>    \d+                     )|
    (?P<id>     [_a-zA-Z][_a-zA-Z0-9]*  )|
    (?P<punct>  [(){}:\[\]=.,+*/-]      )|
    (           \#.*$                   )|
    (           \s+                     )
    """

def tokens(text):
    for match in re.finditer(TOKEN_RX, text):
        if match.lastgroup:
            yield (match.lastgroup, match[0])

TEXT = """
    x = 124 + "hello #99" # ignore me!
    print(hello.by[0] + 3.14, 'single')
    """

for kind, text in tokens(TEXT):
    print(f"{kind:7}: {text=}")


# This is a really interesting lexical analyzer or tokenizer 
# code is a copy from https://twitter.com/nedbat/status/1545772259402338304 
