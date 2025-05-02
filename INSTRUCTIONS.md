# Team Git Collaboration: Pandas Data Analysis Exercise

This exercise will help your team practice Git collaboration while building a data analysis tool together. Each team member will implement a specific analysis function, then collaborate to integrate all functions into a working application.

## Project Overview

You'll build a collaborative data analysis tool that processes a sales dataset. Each team member will:
1. Implement one analysis function in their own Python file
2. Update the main application to use their function
3. Handle any merge conflicts that arise when integrating their work

## Prerequisites

- Git installed
- GitHub account
- Python 3.10 with pandas and matplotlib installed
- A Git client of your choice (command line, GitHub Desktop, VS Code, etc.)

## Repository Structure

```
sales-analysis-project/
├── data/
│   └── sales_data.csv
| tests/
│   ├── test_data_utils.py
│   ├── test_main.py
|── utils/
│   ├── __init__.py
|   └── data_utils.py
├── main.py
├── README.md
└── analysis/
    ├── __init__.py
    └── [team_member_name].py  # Each person creates their own file
```

## Getting Started

### Step 1: Repository Setup (Team Lead)

Clone the repository to your local machine:
```bash
git clone https://github.com/BigDataRepublic/git-fundamentals.git
cd git-fundamentals
```

### Step 2: Choose Your Function

Each team member should choose one of the following analysis functions to implement:

1. **Sales by Region**: Create a function that groups sales data by geographical region and calculates total sales per region.

2. **Sales by Product Category**: Create a function that analyzes sales distribution across different product categories.

3. **Monthly Sales Trend**: Create a function that analyzes sales trends over time, grouping by month.

4. **Top Customers**: Create a function that identifies the top N customers by total sales amount.

5. **Sales by Weekday**: Create a function that analyzes which days of the week have the highest sales.

6. **Average Order Value**: Create a function that calculates the average order value overall and by category.

7. **Product Correlation Analysis**: Create a function that identifies which products are frequently purchased together.

8. **Seasonal Sales Analysis**: Create a function that detects seasonal patterns in the sales data.

9. **Sales Growth Rate**: Create a function that calculates the month-over-month or quarter-over-quarter growth rate.

10. **Customer Segmentation**: Create a function that segments customers based on purchase frequency and amount.

### Step 3: Implementation Process

For each team member:

1. Create a new branch for your feature
   ```
   git checkout -b feature/your-name
   ```

2. Create your Python file in the analysis folder with your name (e.g., `alice.py`)

3. Implement your chosen analysis function that:
   - Takes a pandas DataFrame as input
   - Processes the data according to your function's purpose
   - Creates at least one visualization
   - Returns a pandas DataFrame or Series with the results

4. Test your function with the sample dataset

5. Commit your changes
   ```
   git add analysis/your_name.py
   git commit -m "Add function to analyze [your analysis type]"
   ```

6. Push your branch to GitHub
   ```
   git push origin feature/your-name
   ```

### Step 4: Integration with main.py

After implementing your function:

1. Modify `main.py` to:
   - Import your function
   - Call your function with the dataset
   - Display or save the results

2. Commit these changes
   ```
   git add main.py
   git commit -m "Integrate [your analysis] function into main.py"
   ```

3. Push your changes
   ```
   git push origin feature/your-name
   ```

4. Create a pull request on GitHub

### Step 5: Handle Merge Conflicts

As team members submit pull requests:

1. You'll likely encounter merge conflicts in `main.py`
2. Update your branch with the latest changes from main
3. Resolve any conflicts
4. Test that the code still runs
5. Push the resolved changes
6. Update your pull request

### Step 6: Code Review and Merge

1. Review each other's pull requests
2. Merge the approved pull requests into the main branch
3. Test the final application with all functions integrated

## Sample Dataset

The repository will include a sample sales dataset with columns such as:
- Date
- Region
- Customer
- Category
- Product
- Amount

## Expectations for Each Function

Your implementation should:
- Follow Python best practices
- Include docstrings and comments
- Create at least one visualization
- Return processed data in a useful format
- Handle potential errors in the data

## Handling Git Collaboration

Throughout this exercise, you'll need to:
- Communicate with your team about what you're working on
- Pull changes frequently to minimize conflicts
- Use branches for isolated development
- Create descriptive commit messages
- Review code thoughtfully
- Resolve merge conflicts carefully

## Success Criteria

Your team will succeed when:
- Each person has implemented their function
- All functions are integrated into main.py
- The application runs successfully
- All merge conflicts have been resolved
- Everyone has experienced the full Git collaboration workflow

Good luck with your collaboration!