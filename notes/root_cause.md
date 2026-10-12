# Root Cause: pallets/click#3362

`HelpFormatter.write_usage` builds the usage string and passes it through
`wrap_text`, which creates a `textwrap.TextWrapper`. `TextWrapper` has
`break_on_hyphens=True` by default. That is the right behavior for prose, but
in a usage line each argument is a long option such as
`--enable-verbose-logging`, and an internal hyphen is part of the token, not a
natural break point. When the line is too long, the wrapper splits the option
at a hyphen (for example `--max-` on one line and `retry-count` on the next)
instead of moving the whole token to the next line.

Evidence: reproduced on Click 8.6.0.dev0 (see `reproduction/`). The three
linked PRs (#3385, #3388, #3399) identify the same cause.