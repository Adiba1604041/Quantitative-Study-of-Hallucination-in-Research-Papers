Overview
The study focuses on finding the trend of context inconsistencies in research papers published in ACL in the pre-LLM and post-LLM timelines. 


##Data

The **data** folder contains six csv files: five files contain data from five distinct years (2020-2024) and the sixth csv file contains a dataset that was used to fine-tune model for inconsistency detection.

**Final_2020.csv, Final_2021.csv and Final_2022.csv files contain the data from the pre-LLM era and have the following columns:**

Title: title of the research paper.

Abstract: summary of the paper.

Paragraph: excerpt from the paper.

Context_Inconsistency: "positive" if inconsistency exists; otherwise "negative". (The column name was derived by renaming the "Majority_Label" for better understanding.)


**Final_2023.csv and Final_2024.csv files contain the data from the post-LLM era and have the following columns:**

Title: title of the research paper.

Abstract: summary of the paper.

Paragraph: excerpt from the paper.

Context_Inconsistency: "positive" if inconsistency exists; otherwise "negative". (The column name was derived by renaming the "Majority_Label" for better understanding.)

AI_Hum: Inconsistent paragraphs are labeled either AI-generated or Human-written. 

**Final_for_finetune.csv contains the following columns:**

Title: title of the research paper.

Abstract: summary of the paper.

Paragraph: excerpt from the paper.

Label: "positive" if inconsistency exists; otherwise "negative".

##Code 

The **code** is organized in four different folders marked by the step number.
