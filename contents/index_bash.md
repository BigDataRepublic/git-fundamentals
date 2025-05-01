# Git Collaboration Exercise (bash version)

This exercise will help you practice Git collaboration skills, including handling merge conflicts. You'll work with a shared repository and learn to contribute changes following best practices.

## Prerequisites

- Git installed on your computer
- A GitHub account
- Basic familiarity with command line

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/BigDataRepublic/git-fundamentals
   cd git-fundamentals 
   ```

2. Create and switch to a new branch with your name:
   ```bash
   git checkout -b feature/username
   ```

## Exercise Tasks

### Task 1: Create Your Personal File

1. Create a new folder with your GitHub username if it doesn't exist already:
   ```bash
   mkdir users/your-username
   ```

2. Create a new markdown file inside your folder:
   ```bash
   touch users/your-username/about-me.md
   ```

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

4. Stage and commit your changes:
   ```bash
   git add users/your-username/about-me.md
   git commit -m "Add personal information file"
   ```

### Task 2: Update the Index File

1. Open the index file:
   ```bash
   nano contents/index.md
   ```

2. Find the "Team Members" section in the index file and add a link to your personal file:
   ```markdown
   - [Your Name](../users/your-username/about-me.md)
   ```

3. Additionally, modify the "Project Description" section by adding one new sentence of your choice.

4. Stage and commit your changes:
   ```bash
   git add contents/index.md
   git commit -m "Update index with my information"
   ```

### Task 3: Push Your Changes and Create a Pull Request

1. Push your branch to the remote repository:
   ```bash
   git push origin username-feature
   ```

2. Go to the repository on GitHub and create a pull request:
   - Click on "Pull Requests"
   - Click "New Pull Request"
   - Select your branch as the source
   - Add a title and description
   - Submit the pull request

### Task 4: Handle Merge Conflicts

Since multiple people will be editing the same file (`contents/index.md`), you'll likely encounter merge conflicts. Here's how to handle them:

1. Before your PR is merged, update your local main branch:
   ```bash
   git checkout main
   git pull origin main
   ```

2. Switch back to your feature branch:
   ```bash
   git checkout username-feature
   ```

3. Merge the latest changes from main into your branch:
   ```bash
   git merge main
   ```

4. If you encounter conflicts, Git will tell you which files have conflicts. Open these files in your editor.

5. You'll see conflict markers like this:
   ```
   <<<<<<< HEAD
   Your changes
   =======
   Changes from main
   >>>>>>> main
   ```

6. Edit the file to resolve the conflict. Keep your changes, the other changes, or combine them as appropriate. Remove the conflict markers.

7. Once you've resolved all conflicts, stage the resolved files:
   ```bash
   git add contents/index.md
   ```

8. Complete the merge:
   ```bash
   git commit -m "Resolve merge conflicts"
   ```

9. Push the updated branch:
   ```bash
   git push origin username-feature
   ```

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
```

## Sample Contents of index.md

```markdown
# Team Collaboration Project

## Project Description
This is a sample project to learn Git collaboration. 
[Your added sentence will go here]

## Team Members
- [Team Member 1](../users/user1/about-me.md)
- [Team Member 2](../users/user2/about-me.md)
- [Your Name](../users/your-username/about-me.md)
```

## Tips for Success

1. **Communicate with your team** about which files you're working on
2. **Pull regularly** to stay updated with others' work
3. **Create meaningful commit messages** describing your changes
4. **Don't panic** when you encounter merge conflicts - they're a normal part of collaboration!
5. **Ask for help** if you get stuck

Happy collaborating!
