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
- Needed to revert the version-update commit on `product_version_1`.
+ Those changes will no longer show up in PR diffs to update `product_version_1`
- Any merge-conflict resolutions on future PRs will be committed to `main`. Github **might** warn you and prompt you to make a new branch, but for safety's sake you should use merge branches.

Final flow definition:
* All nonlatest product versions have long-lived branches.
* All (or at least most) feature branches are off of `main`.
* Periodically make a new "Merge branch" to update `product_version_1`, a "Merge branch" to update `product_version_2`, etc.

This is essentially the next case, but involves a shortcut in making `main` synonymous with `product_version_latest`.

### Latest is trunk, each version also has a branch (including trunk version)

Final flow definition:
* All product versions have long-lived branches.
* All (or at least most) feature branches are off of `main`.
* Periodically make a new "Merge branch" to update `product_version_1`, a "Merge branch" to update `product_version_2`, etc.

### Oldest is trunk, new versions get new branches

Final flow definition:
