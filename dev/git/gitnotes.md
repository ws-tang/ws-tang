# Git Notes

**Table of Contents**

- [Git](#git)
  - [Common Command Notes](#git_common_cmd_notes)
- [Typical Workflows](#typlical_workflows)
  - [Code update](#typlical_workflows_code_update)
  - [Simplify commits before delivery](#typlical_workflows_simplify_commits)

<br/>

## Git <a name="git"></a>

- [Download](https://git-scm.com/downloads)
- [Documentation of Git Commands](https://git-scm.com/docs)

<br/>

## Common Command Notes <a name="git_common_cmd_notes"></a>

Clone a remote repository

```
git clone repoURL

git clone https://github.com/ws-tang/ws-tang.git
```

<br/>

Change the remote repository name locally

```
git remote rename origin newRemoteRepoName
```

<br/>

Check the status of the current branch

```
git status [- | grep modified]
```

<br/>

Get the latest from the remote repository

```
git pull
```

<br/>

Deliver a local branch to the remote repository

```
git push
```

<br/>

Deliver a local branch to the remote repository forcibly (**not recommended, use with care**)

```
git push [--force | -f ]
```

<br/>

View the last N formatted commit logs, say N is 10

```
git log --oneline --date=short --pretty=format:"%h%x09%s" -10

git log --oneline --date=short --pretty=format:"%h%x09%ad%x09%s" -10

git log --oneline --date=short --pretty=format:"%h%x09%ad%x09%an%x09%s" -10
```

<br/>

Stash the changes in the current work branch

```
git stash list => list the current stashed entries

git push => Stash the changes in the current work branch

git pop => Pop the top stashed entry out
```

<br/>

## Typical Workflows <a name="typlical_workflows"></a>

### Code update <a name="typlical_workflows_code_update"></a>

1. Switch to the local target branch.
2. Pull the latest for the target branch locally from the remote repository.
3. Create a work branch and check it out off the target branch.
4. Update the code as needed in the work branch and make commits accordingly.
5. Switch to the local target branch.
6. Pull the latest for the target branch locally from the remote repository.
7. Switch to the work branch.
8. Rebase to the latest of the local target branch and resolve any discrepancy.
9. If there are multiple commits in the work branch, consolidate the commits into one. Refer the steps noted in [Simplify commits before delivery](#simplify-commits-before-delivery)
10. Switch to the local target branch.
11. Merge the work branch into the local target branch.
12. Commit the local target branch to the remote target branch.
13. Delete the local work branch when done.

```
(1) git checkout localTargetBranch

(2) git pull

(3) git checkout -b workBranchName

(4) git commit

(5) git checkout localTargetBranch

(6) git pull

(7) git checkout workBranchName

(8) git rebase localTargetBranch

(9) ... ...

(10) git checkout localTargetBranch

(11) git merge workBranchName

(12) git push

(13) git branch -d workBranchName
```

<br/>

---

### Simplify commits before delivery <a name="typlical_workflows_simplify_commits"></a>

The procedure is to simplify a number of commits for code changes in a development work branch into one commit before delivering the update to the remote (main) repository. This will significantly reduce the clutter in Git commit history.

1. Switch to the work branch
2. Check the last N local commits, say N is **10**.
3. Identify the rebase target commit. The target commit is the one before the code change starts. Tag it with a proper tag such as **branchPrefix_target**.
4. Identify the rebase recover commit. The recover commit is the latest commit of the code change. Tag it with a proper tag such as **branchPrefix_recover**.
5. Run **git rebase** comamnd with the option **-i** to squash the commits between the target and recover tags.
6. Mark the commit at the top line as **p** (pick) and everyone else as **s** (squash). Set the commit message properly during the squash steps. If the editor is vi/vim, use [ESC] then ":wq!" to save and exit.
7. After the successful delivery of the squashed commits, make sure to remove the tags in the work branch.

```
(1) git checkout workBranchName

(2) git log --oneline --date=short --pretty=format:"%h%x09%ad%x09%an%x09%s" -10

(3) git tag branchPrefix_target targetHash

(4) git tag branchPrefix_recover recoverHash

(5) git rebase -i branchPrefix_target

(6)
p hashNum commitMsg1
s hashNum commitMsg1
s hashNum commitMsg1

Use [ESC] then ":wq!"

(7) git tag -d branchPrefixTarget branchPrefixRecover

```

<br/>
