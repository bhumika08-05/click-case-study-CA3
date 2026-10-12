import click

options = [
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

f = click.HelpFormatter(width=65)
f.write_usage("program", " ".join(options))
print(f.getvalue())