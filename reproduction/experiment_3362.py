import textwrap

text = "--enable-verbose-logging --output-file-path --max-retry-count"

print("Default (break_on_hyphens=True):")
print(textwrap.fill(text, width=40))

print()
print("With break_on_hyphens=False:")
print(textwrap.fill(text, width=40, break_on_hyphens=False))