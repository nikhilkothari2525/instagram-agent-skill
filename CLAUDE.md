# CLAUDE.md

Instructions for any Claude session working inside this repo.

## What this repo is

The MYERAPAIRS fork of Jake Schincariol's
[instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill),
a pack of thirteen Claude skills for Instagram, under the MIT licence.
MYERAPAIRS is a women's footwear shop in Mandsaur, India, on Instagram as
@myerapairsofficial. The fork keeps the upstream skills and adds MYERAPAIRS
brand rules on top of them.

## This repo is public

Anything committed here can be read by anyone on GitHub. Never commit:

- Customer data of any kind: handles, names, phone numbers, addresses, DMs,
  comments, order details, screenshots.
- Credentials, tokens, passwords, environment variable values, server paths,
  internal hostnames or IP addresses.
- ERP internals: file paths, route names, environment variable names,
  permission names, schema names, and any weakness or bug found in the ERP.
- Exact stock counts, cost prices, supplier details, godown details, staff
  names.

Working files and logs go in `~/.claude/instagram/`, outside git. Check the
staged diff for any of the above before every commit. If you are not sure
something is safe to commit, leave it out and ask.

## The brand files

| file | read it for |
| --- | --- |
| `myerapairs/rules.md` | how work is done, what needs approval, status words. Read first. |
| `myerapairs/voice.md` | how MYERAPAIRS sounds and what it never says |
| `myerapairs/product-facts.md` | which product facts may be used, and the ERP check |

Skills find these at `../../myerapairs/` from their own folder, so keep
`skills/` and `myerapairs/` side by side at the root. The repo copy of
`voice.md` wins over `~/.claude/instagram/voice.md`. Skills propose edits to
`myerapairs/voice.md`; they never create or overwrite a `voice.md`.

## Skills stay draft-only

Every skill ends with a draft that a person posts or sends by hand after the
owner, or a manager he names, signs off. Keep it that way. Do not add anything
that posts, sends, replies, follows, likes, comments, logs in to Instagram,
drives a logged-in browser or calls Instagram or Meta APIs.

## Live actions belong in the ERP

Anything that acts on the live Instagram account or on business data (a
publishing queue, the DM inbox, tasks, stock, orders) belongs in the ERP
project, not here. This repo stays a skill pack. Do not copy ERP code,
configuration or internal names into it.

## Editing upstream skills

Add MYERAPAIRS sections to a skill rather than rewriting it. Keep the upstream
text where it does not conflict with `myerapairs/rules.md`.

## Tests

From the repo root:

```bash
python3 -m unittest discover -s tests
```

Standard library only, no network. When you report results, use the status
words in `myerapairs/rules.md` (verified live, built and tested, built,
untested, planned, not available).

## Credit and licence

Keep `LICENSE` exactly as it is: MIT, copyright Jake Schincariol. Keep the
credit to Jake Schincariol in `README.md` and in the plugin metadata under
`.claude-plugin/`.
