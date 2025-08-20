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

### Persona
Pain：
1. Spending 45+ minutes on complex applications just to find a hidden risk factor
2. Pressure to hit weekly targets while keeping defaults under 4%
3. Getting blamed for “obvious misses” in hindsight during quarterly reviews
4. Juggling gut feeling with outdated risk rules that miss modern borrower patterns

Key Decisions Can Makes:
“Approve with conditions” (e.g., require co-signer) vs straight approve/reject
Whether to escalate to the lending manager for exceptions
How to explain denials to frustrated applicants fairly and clearly

How the Model Help:
Gives a clear, data-backed risk score in <30 secs
Flags non-obvious risks (e.g., rapid recent credit inquiries + high debt-to-income)
Lets people focus on deep experience on edge cases, not routine screening
