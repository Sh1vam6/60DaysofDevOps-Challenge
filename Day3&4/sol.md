

## Challenge 1: Fork and Clone  Project

1. Fork the repository on GitHub (https://github.com/sd031/eks-auto-mode-workshop)
2. Clone your forked repository:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/eks-auto-mode-workshop.git
   ```
   Example: `git clone https://github.com/Sh1vam6/eks-auto-mode-workshop.git`

3. To sync future updates from the original repository:
   ```bash
   cd eks-auto-mode-workshop
   git remote add upstream https://github.com/sd031/eks-auto-mode-workshop.git
   ```

4. Check your git remotes:
   ```bash
   git remote -v
   ```

5. Fetch and merge updates from the original repo:
   ```bash
   git fetch upstream
   git merge upstream/main
   ```

## Challenge 2: Create a New Branch, Switch, and Commit Changes

```bash
# Create and switch to a new branch
git checkout -b feature-branch

# Create a new file
echo "hello devops" > feature.txt

# Add and commit changes
git add .
git commit -m "feature file added"

# Push the branch to remote
git push origin feature-branch
```

## Challenge 3: Merge Feature Branch into Main

```bash
# Switch to main branch
git checkout main

# Pull latest changes
git pull origin main

# Merge feature branch
git merge feature-branch

# Push changes to remote
git push origin main
```

### Deleting Branches

```bash
# Delete a local branch
git branch -d feature-branch

# Delete a remote branch
git push origin --delete feature-branch
```

## Challenge 4: Undo a Commit

```bash
# Completely remove the last commit (discards changes)
git reset --hard HEAD~1

# Undo the commit but keep the changes
git reset --soft HEAD~1

# Undo a specific commit without changing history
git revert <commit-hash>

# View commit history
git log --oneline
```

## Challenge 5: Rebase Feature Branch onto Main

```bash
git checkout feature-branch
git rebase main
```

### Rebase vs Merge Comparison

| Feature | Rebase (`git rebase main`) | Merge (`git merge main`) |
|---------|----------------------------|--------------------------|
| History | Creates a clean linear history | Keeps a branching history |
| Commits | Moves commits on top of the latest main | Merges main changes with a merge commit |
| Conflicts | Can require resolving multiple conflicts | Resolves conflicts once at merge |
| Recommended When | You want a clean history (before merging) | You need a clear branch history |

## Challenge 6: Create a Pull Request on GitHub

```bash
# Push your feature branch
git push origin feature-branch
```

Then go to the GitHub repository and create a pull request.

### Using GitHub CLI (Optional)

```bash
gh pr create --base main --head feature-branch --title "New Feature" --body "Description of the feature"
```
(Requires GitHub CLI: `gh auth login` before using this command)

## Challenge 7: Create and Resolve Conflicting Changes

```bash
# Create a change in feature branch
git checkout feature-branch
echo "hello" > file.txt
git add .
git commit -m "by feature-branch"

# Create a conflicting change in main
git checkout main
echo "hi" > file.txt
git add .
git commit -m "by main branch"

# Try to merge (will create conflict)
git merge feature-branch
```

To resolve:
1. Open the file and manually resolve the conflict
2. Add the resolved file: `git add .`
3. Commit the resolution: `git commit -m "solved conflict"`
4. Push to remote: `git push origin main`

## Challenge 8: Use Git Stash

```bash
# Make changes to a file
echo "Uncommitted changes" >> file.txt

# Check status
git status

# Stash uncommitted changes
git stash

# Check status again (clean working directory)
git status

# Apply stashed changes and remove from stash
git stash pop

# Or apply changes but keep them in stash
git stash apply

# List all stashes
git stash list
```

## Challenge 9: Add Version Tags to Commits

```bash
# View recent commits
git log --oneline --graph --decorate -n 5

# Create a lightweight tag
git tag v1.0.0

# Create an annotated tag (with message)
git tag -a v1.0.0 -m "Release version 1.0.0"

# List tags
git tag

# Push a specific tag
git push origin v1.0.0

# Push all tags
git push --tags

# Delete a local tag
git tag -d v1.0.0

# Delete a remote tag
git push origin --delete v1.0.0

# Create a branch from a tag
git checkout -b release-1.0 v1.0.0
```

## Challenge 10: Edit Past Commits

### Amend the Last Commit

```bash
git commit --amend -m "Updated commit with new changes"

# Force push if already pushed to remote
git push origin main --force
```

### Interactive Rebase to Edit Older Commits

```bash
# Start interactive rebase for the last 3 commits
git rebase -i HEAD~3
```

In the editor that opens, change actions:
- `pick` - use commit as is
- `reword` - change the commit message
- `edit` - amend the commit
- `squash` - combine with previous commit
- `drop` - remove the commit

Example editor changes:
```
reword 5bdc6f0 by shiv
edit 80bfdaa by main
pick 75e5b29 by feature/shiv
```

For `edit` commits:
1. Make your changes
2. Stage them: `git add .`
3. Amend the commit: `git commit --amend`
4. Continue the rebase: `git rebase --continue`

After editing history, force push is required:
```bash
git push origin feature-branch --force
```

