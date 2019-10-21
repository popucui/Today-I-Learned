## Problem
Sometimes we need to roll back code base to a specific version(commit).
## Solution

```bash
cd /path/to/repo/ 
git reset --hard <tag/branch/commit id>
```

Note:
- `git reset` without `--hard` only resets commit history, not the files
- use `git push <reponame> -f` if you want the remote repo also points to the rolled back commit

references:
- [roll back git repo](https://stackoverflow.com/questions/1616957/how-do-you-roll-back-reset-a-git-repository-to-a-particular-commit)
- [git reset](https://git-scm.com/docs/git-reset/)