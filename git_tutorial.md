# Git Basics

## Clone the project

Run this once to download the project, then enter its folder:

```powershell
git clone https://github.com/MarioTheOne/PP4AI.git
cd PP4AI
```

## Check your changes

See which files Git notices and what has changed:

```powershell
git status
git diff
```

## Save a commit

Stage the files you want to include, then create a commit. A commit is a
saved snapshot in your local repository.

```powershell
git add README.md
git commit -m "Describe your change"
```

Use `git add .` to stage all changed files in the current project. Check
`git status` first, especially to avoid staging secrets or generated files.

## Get and share updates

Pull downloads and integrates the latest commits from GitHub. Push uploads
your local commits. Pull before starting work and before pushing:

```powershell
git pull
git push
```

For a new branch that has not been pushed before, publish it and set its
upstream with:

```powershell
git push -u origin your-branch-name
```

## Branches

Branches let you work on a change separately from the main line of work:

```powershell
git branch
git switch -c my-change
```

After committing, push the new branch with the command above. Replace
`my-change` and `your-branch-name` with your branch name. The default branch
is often called `main`; use your repository's branch name when needed.

## Useful history commands

```powershell
git log --oneline
git remote -v
```

If `git pull` or `git push` reports a conflict or rejection, read the message,
resolve conflicts before continuing, and avoid overwriting remote work.