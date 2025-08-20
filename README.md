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


Topic: Inaccurate loan approval decisions.
Problem: A two-sided failure: 
1) False approvals lead to bad debt losses (False Positives), and
2) 2) False rejections lead to lost revenue opportunities (False Negatives). This directly impacts profitability and competitive advantage.

The Stakeholder & End User:
Primary Stakeholder (The Decider/Owner): The Chief Risk Officer (CRO) or Head of Lending. This is the person accountable for the outcome, concerned with the profitability and risk level of the entire loan portfolio.
End User (The Operator): The Loan Officer. This is the person who will use the output of your model daily. Your design must fit seamlessly into their workflow and habits.

The Useful Answer:
Type: Predictive. We are not merely describing historical data nor conducting a strict causal experiment; we are predicting the future probability of default.
Metric: Default Probability Score. This is a specific and actionable continuous value that provides more information than a simple "yes/no" classification.
Artifact: An integrated software component (e.g., an API). This clarifies that the final deliverable is not an isolated notebook or report, but a tool that can be embedded into the existing system to generate tangible value.
