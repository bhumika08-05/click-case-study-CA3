# Linked Pull Requests for Issue #3362

Issue: pallets/click#3362, HelpFormatter.write_usage breaks options at a hyphen

## Summary
Three pull requests were opened against this issue. All three were closed
without merging, and all carry the label "rejected AI". None received a
formal review.

## PR #3385: Avoid hyphen breaks in usage option tokens
- Author: cyphercodes
- Opened: Apr 27
- Status: Closed (closed by davidism on Apr 27, locked on May 12)
- Files changed: 3 (names to be added)
- Idea: Stop write_usage from wrapping hyphenated option tokens at internal
  hyphens when the whole token fits on the next line. Adds a regression test
  and a changelog entry.
- Reviewer comments: None

## PR #3388: Don't break usage option tokens at internal hyphens
- Author: charlieleith
- Opened: Apr 29
- Status: Closed
- Files changed: (to be added)
- Idea: wrap_text builds a textwrap.TextWrapper with break_on_hyphens=True by
  default. That suits prose but not tokens like --enable-verbose-logging.
- Reviewer comments: None visible

## PR #3399: Avoid breaking HelpFormatter usage args on hyphens
- Author: MackDing
- Opened: May 2
- Status: Closed
- Files changed: (to be added)
- Idea: Add explicit wrapper controls so write_usage does not break inside
  hyphenated names, while other wrap_text callers keep existing behavior.
  Adds a regression test.
- Reviewer comments: None visible

## Observations
- All three PRs identify the same root cause: write_usage goes through
  wrap_text, and TextWrapper breaks on hyphens by default.
- The maintainers' response was about the contributions being AI-generated,
  not about the technical idea, so there is no feedback on a preferred fix.
