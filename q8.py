# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer: Prompt B

# Q8b: Give TWO reasons to support your choice.
# Your answer (Reason 1): Clear Structure and Formatting. Prompt B breaks down the request using distinct headers (Role, Task, Data, Steps, Audience, Constraints). This structure makes it incredibly easy for an AI to parse the exact requirements without having to extract them from a block of text.
# Your answer (Reason 2): Explicit Constraints and Guardrails. Prompt B provides explicit rules under "Constraints" (e.g., "free of technical jargon"), which tells the AI exactly what tone to avoid for the CEO presentation. Prompt A hints at this ("easy to understand") but doesn't define it as a strict limitation.

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer: Prompt A provides much more natural context and a realistic narrative about the current situation (e.g., the data is currently "stored in a spreadsheet" and the team "just finished a three-month campaign"). This helps the AI better understand the real-world workflow and background of the request.


# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.

# What I borrowed: I took the highly specific, detailed data description from Prompt A ("satisfaction rating from 1 to 5, and a short written comment") and injected it into the "Data" section of Prompt B.
# Why I borrowed it: Prompt B's data section was a bit vague about the metrics. Adding the specific "1 to 5" scale and "short written comment" description gives the AI exact parameters of the dataset, which helps it choose the right analytical approach (like numerical averaging vs. text sentiment tracking).

# Enhanced Prompt:
"""
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 spreadsheet responses containing customer age group, product purchased, satisfaction rating measured on a scale from 1 to 5, and a short written comment.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""
