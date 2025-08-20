# Bootcamp Repository

## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.

## Project Folder Rules
- Keep project files organized and clearly named.# bootcamp_Ting_Yu


### Problem Statement
We're losing money and missing out on good loans because our current approval process is inefficient. We need a smarter way to sort the risky applicants from the reliable ones.

### Stakeholder & User
Decision owner: Lending Manager (owns the results)
Tool/operator: Loan Officers (use the tool daily)

### Useful Answer
Forecast: Predicts who will likely default
Output: A risk score (0-100) delivered as a simple tool in our current system

### Assumptions & Constraints
Enough past loan data exists to train the system
Must return a score in under 2 seconds
Must comply with fair lending rules
Built for personal loans only

### Known Unknowns / Risks
Data might be messy or contain hidden biases
Economic shifts could make predictions less accurate
Loan officers might not trust or might over-rely on the tool

### Lifecycle Mapping
Define success → Scoping → Project charter & memo
Get data ready → Data Prep → Clean dataset & reports
Build predictor → Modeling → Trained model & validation
Put to use → Deployment → Working tool & docs
Keep current → Maintenance → Monitoring dashboard
