import pandas as pd
import os
import nltk
from nltk.tokenize import sent_tokenize

df = pd.read_csv(r"/XXXX/2024/acl2024.csv",encoding="ISO-8859-1")

## Drop duplicates
df_unique = df.drop_duplicates()


## Drop rows where paragraphs have less than 3 sentences
def count_sentences(paragraph):
    if isinstance(paragraph, str):
        return len(sent_tokenize(paragraph))
    else:
        return 0  #Treat missing/invalid as 0 sentences

# Filter rows where paragraph has 3 or more sentences (Need proper paragraphs for context)
df_filtered = df_unique[df_unique['Paragraph'].apply(count_sentences) >= 3]

folder_path = "/XXXX/ACL/CSVs/2024"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)  

csv_path = os.path.join(folder_path, "Filtered_acl2024.csv")

df_filtered.to_csv(csv_path, index=False)

print(f"CSV file saved at: {csv_path}")
