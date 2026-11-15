# Configuration Status Accounting - Inventory Tracker

**Author:** Kolade Afolabi

This record tracks every branch, commit and release of the project and shows
which commit belongs to which maintenance task. Replace each `<hash>` with the
short hash from your own `git log --oneline` output before committing.

## Configuration items

| Item | Description |
| --- | --- |
| `inventory.py` | Item record and inventory data |
| `app.py` | Main script and report output |
| `utils/helpers.py` | Calculations and formatting helpers |
| `tests/test_inventory.py` | Unit tests |
| `requirements.txt` | Dependencies |
| `README.md` | Project documentation |
| `changelog.txt` | Exported Git log |

## Branches

| Branch | Created from | Purpose | Status |
| --- | --- | --- | --- |
| `main` | - | Released code | Active, holds v1.0 |
| `dev` | `main` (initial commit) | Maintenance tasks | Merged into `main` |

## Commits mapped to maintenance tasks

| Commit | Branch | Maintenance task | Files changed | Summary |
| --- | --- | --- | --- | --- |
| `<hash>` | `main` | Baseline | all | Initial commit: inventory tracker starter code |
| `<hash>` | `dev` | Corrective | `app.py`, `utils/helpers.py` | Fix total stock value and lowest stock item |
| `<hash>` | `dev` | Adaptive | `inventory.py`, `app.py`, `utils/helpers.py` | Update for Python 3.12, add Item dataclass and low-stock alert |
| `<hash>` | `dev` | Perfective | `app.py`, `utils/helpers.py` | Format report as a table and export to CSV |
| `<hash>` | `dev` | Preventive | `inventory.py`, `app.py`, `utils/helpers.py`, `tests/`, `README.md` | Refactor into helpers, add docstrings and unit tests |
| `<hash>` | `dev` | Documentation | `changelog.txt`, `STATUS_ACCOUNTING.md` | Add change log and status accounting record |
| `<hash>` | `main` | Release | - | Merge dev: maintenance tasks for v1.0 |

## Releases

| Tag | Commit | Contents |
| --- | --- | --- |
| `v1.0` | `<hash>` (merge commit on `main`) | Starter code plus corrective, adaptive, perfective and preventive maintenance |

## Commands used for status accounting

```bash
git log --oneline                         # one line per commit
git log --oneline --graph --decorate --all   # branch structure
git log --pretty=format:"%h | %an | %ad | %s" --date=short   # commits, authors, dates
git log --stat                            # files changed by each commit
git branch -a                             # all branches
git tag -n                                # releases
git show v1.0 --stat                      # what the release points to
git shortlog -sn                          # commits per author
git diff --stat <initial-hash> v1.0       # audit: total change since the baseline
```
