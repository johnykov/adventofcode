import re

pattern = ur'''
    (?imsx)             # ignore case, multiline, dot-matches-newline, verbose
    <p.*?>              # match first marker
    (?P<text>.*?)       # non-greedy match anything
    </p.*?>             # match second marker
'''
# https://stackoverflow.com/a/25355753/2011031
print(re.findall(pattern, '<p>hello</p>'))
print(re.findall(pattern, '<p>hello</p> and <p>goodbye</p>'))
print(re.findall(pattern, 'before <p>hello</p> and <p><i>good</i>bye</p> after'))
print(re.findall(pattern, '<p itemprop="xxx"> some text <br/> another text </p>'))