# Git Collaboration Guide for Beginners

This guide will help you start collaborating on a shared Git repository, even if you've never used Git before.

## Getting Started

### 1. Clone the Repository
First, you need to make a local copy of the repository on your computer:

```bash
git clone https://github.com/username/repository-name.git
```
This creates a new folder with the repository name containing all project files.

### 2. Navigate to the Repository Folder
```bash
cd repository-name
```

## Making Changes

### 3. Create a New Branch
Always create a new branch for your changes. This keeps your work separate from the main codebase:

```bash
git branch my-feature-branch
git checkout my-feature-branch
```

OR use the shortcut command:

```bash
git checkout -b my-feature-branch
```

### 4. Make Your Changes
Edit, add, or delete files as needed for your task.

### 5. Check the Status of Your Changes
To see which files you've modified:

```bash
git status
```

### 6. Stage Your Changes
Add your modified files to the staging area:

```bash
git add filename.txt        # Add a specific file
git add foldername/         # Add a folder and its contents
git add .                   # Add all changes
```

### 7. Commit Your Changes
Save your changes with a descriptive message:

```bash
git commit -m "Brief description of your changes"
```

### 8. Push Your Branch to the Remote Repository
Upload your branch to the remote repository:

```bash
git push origin my-feature-branch
```

## Staying Updated

### 9. Fetch Latest Changes
To see what others have been working on:

```bash
git fetch
```

### 10. Update Your Main Branch
Keep your local main branch updated:

```bash
git checkout main
git pull origin main
```

### 11. Update Your Feature Branch
Incorporate the latest changes from main into your feature branch:

```bash
git checkout my-feature-branch
git merge main
```
If there are conflicts, Git will notify you and you'll need to resolve them.

## Contributing Your Changes

### 12. Create a Pull Request (PR)
**Important:** This is how your code gets merged into the main codebase!

1. Go to the repository on GitHub/GitLab/etc.
2. Click on "Pull Requests" or "Merge Requests"
3. Click "New Pull Request"
4. Select your branch as the source
5. Add a title and description explaining your changes
6. Submit the pull request

Your team members will review your code, suggest changes if needed, and eventually merge it into the main branch.

## Common Scenarios

### Discard Local Changes
If you want to undo changes to a file:

```bash
git checkout -- filename
```

### Check Branch History
To see the commit history:

```bash
git log
```

### Switch Between Branches
```bash
git checkout branch-name
```

## Remember:
- **Never commit directly to main**
- **Always create a Pull Request for changes**
- **Pull regularly** to stay updated with others' work
- **Communicate with your team** about which files you're working on

Happy coding!
