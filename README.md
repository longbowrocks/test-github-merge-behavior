# test-github-merge-behavior
GitHub PR diffs are based on common ancestor, not line-by-line diff.

This repo will allow me to experiment and find the most maintainable way to have two long-lived branches share *some* changes.

My test cases are below.

### Latest is trunk, branches are older versions

```
$> git checkout -b product_version_1
$> git push
$> git checkout main
$> vim source_code.py
$> git commit -am "update to version 2"
$> vim source_code.py
$> git commit -am "bugfix"
```

Ran the above commands, then created a PR to merge changes from `main` into `product_version_1`.

Result:

### Latest is trunk, each version also has a branch (including trunk version)

### Oldest is trunk, new versions get new branches
