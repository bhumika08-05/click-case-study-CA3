import click

OPTIONS = [
    "--enable-verbose-logging",
    "--output-file-path",
    "--max-retry-count",
    "--disable-cache-mode",
    "--config-file-location",
    "--user-auth-token",
    "--auto-update-interval",
    "--force-overwrite-existing",
    "--network-timeout-seconds",
    "--debug-trace-enabled",
]


def make_usage():
    formatter = click.HelpFormatter(width=65)
    formatter.write_usage("program", " ".join(OPTIONS))
    return formatter.getvalue()


def test_options_are_not_split_at_hyphens():
    """Issue #3362: every option must stay whole in the usage line."""
    usage = make_usage()
    for option in OPTIONS:
        assert option in usage, f"{option} was split across lines"


def test_usage_tokens_match_options():
    """Splitting the output on whitespace should give back the options."""
    tokens = make_usage().split()[2:]  # skip "Usage:" and "program"
    assert tokens == OPTIONS