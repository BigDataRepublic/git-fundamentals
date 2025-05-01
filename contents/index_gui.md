# Git Collaboration Exercise (GUI Version)

This exercise will help you practice Git collaboration skills using GitHub Desktop or VS Code's Git extension. You'll work with a shared repository and learn to contribute changes following best practices, including handling merge conflicts.

## Prerequisites

- Git installed on your computer
- GitHub Desktop or VS Code with Git extension
- A GitHub account

## Setup

1. **Clone the repository:**
   - **GitHub Desktop:** 
     - Click "File" > "Clone Repository"
     - Select the repository from GitHub or enter the URL
     - Choose where to save it locally and click "Clone"
   
   - **VS Code:**
     - Open VS Code
     - Click on the Source Control icon in the sidebar
     - Click "Clone Repository"
     - Enter the repository URL and select a local folder

2. **Create a new branch:**
   - **GitHub Desktop:**
     - Click the "Current Branch" dropdown
     - Click "New Branch"
     - Name it "feature/username"
     - Click "Create Branch"
   
   - **VS Code:**
     - Click on the branch name in the bottom-left corner
     - Select "Create new branch"
     - Name it "feature/username"
## Exercise Tasks

### Task 1: Create Your Personal File

1. Create a new folder with your GitHub username inside the repository's "users" folder.

2. Create a new markdown file named "about-me.md" inside your folder.

3. Add some content to your file. For example:
   ```markdown
   # About Me
   
   ## Name
   Your Name
   
   ## Interests
   - Interest 1
   - Interest 2
   - Interest 3
   
   ## Favorite Programming Languages
   1. Language 1
   2. Language 2
   3. Language 3
   ```

4. Commit your changes:
   - **GitHub Desktop:**
     - Enter a summary like "Add personal information file"
     - Click "Commit to feature/username"
   
   - **VS Code:**
     - Enter a commit message in the Source Control panel
     - Click the checkmark to commit

### Task 2: Update the Index File

1. Open the "contents/index.md" file.

2. Find the "Team Members" section in the index file and add a link to your personal file:
   ```markdown
   - [Your Name](../users/your-username/about-me.md)
   ```

3. Additionally, modify the "Project Description" section by adding one new sentence of your choice.

4. Commit your changes:
   - **GitHub Desktop:**
     - Enter a summary like "Update index with my information"
     - Click "Commit to feature/username"
   
   - **VS Code:**
     - Enter a commit message in the Source Control panel
     - Click the checkmark to commit

### Task 3: Push Your Changes and Create a Pull Request

1. Push your branch to GitHub:
   - **GitHub Desktop:**
     - Click "Publish branch" or "Push origin"
   
   - **VS Code:**
     - Click the cloud icon with an arrow in the status bar or "Push" in the Source Control panel

2. Create a Pull Request on GitHub:
   - Go to the repository on GitHub
   - You should see a prompt to create a pull request for your recently pushed branch
   - Click "Compare & pull request"
   - Add a title and description
   - Click "Create pull request"

### Task 4: Handle Merge Conflicts

Since multiple people will be editing the same file (`contents/index.md`), you'll likely encounter merge conflicts. Here's how to handle them:

1. Update your main branch:
   - **GitHub Desktop:**
     - Switch to the main branch from the "Current Branch" dropdown
     - Click "Fetch origin" then "Pull origin"
     - Switch back to your feature branch
     - Click "Choose a branch to merge into your-username-feature"
     - Select "main" and click "Merge main into your-username-feature"
   
   - **VS Code:**
     - Switch to the main branch using the branch selector in the bottom-left
     - Click the sync button in the status bar to pull changes
     - Switch back to your feature branch
     - Open the Command Palette (Ctrl+Shift+P)
     - Type "Git: Merge Branch..." and select main

2. If conflicts occur, you'll be notified:
   - **GitHub Desktop:**
     - You'll see a notification that there are conflicts
     - Click "Open in Visual Studio Code" (or your preferred editor)
   
   - **VS Code:**
     - Files with conflicts will be marked in the Source Control panel
     - Open the conflicted file to see the conflict markers

3. In the editor, you'll see conflict markers like this:
   ```
   <<<<<<< HEAD
   Your changes
   =======
   Changes from main
   >>>>>>> main
   ```

4. Edit the file to resolve the conflict:
   - VS Code provides helpful buttons above the conflict to accept your changes, incoming changes, or both
   - Alternatively, manually edit the text and remove the conflict markers

5. Mark the conflict as resolved:
   - **VS Code:**
     - Save the file
     - Click the "+" (Stage Changes) for the file in the Source Control panel
   
   - **GitHub Desktop:**
     - Save the file in your editor
     - Return to GitHub Desktop where it should show the conflict is resolved

6. Complete the merge by committing:
   - **GitHub Desktop:**
     - Enter a summary like "Resolve merge conflicts"
     - Click "Commit to feature/username"
   
   - **VS Code:**
     - Enter "Resolve merge conflicts" as the commit message
     - Click the checkmark to commit

7. Push the updated branch:
   - **GitHub Desktop:** Click "Push origin"
   - **VS Code:** Click the sync button in the status bar

Your pull request will automatically update with the resolved conflicts.

## Expected Repository Structure

After everyone completes the exercise, the repository should look like:

```
collaboration-exercise/
├── contents/
│   └── index.md
└── users/
    ├── user1/
    │   └── about-me.md
    ├── user2/
    │   └── about-me.md
    └── your-username/
        └── about-me.md

Sample Contents of index.md

```
# Team Collaboration Project

## Project Description
This is a sample project to learn Git collaboration. 
[Your added sentence will go here]

## Team Members
- [Team Member 1](../users/user1/about-me.md)
- [Team Member 2](../users/user2/about-me.md)
- [Your Name](../users/your-username/about-me.md)
```

Tips for Success

Refresh often in GitHub Desktop or use the sync button in VS Code to stay updated
Create meaningful commit messages describing your changes
Don't rush through conflict resolution - take time to understand whose changes to keep
Use the visual diff tools in your editor to help understand changes
Communicate with your team about which files you're working on
Remember that Pull Requests are the proper way to get your code into the main branch

Happy collaborating!
