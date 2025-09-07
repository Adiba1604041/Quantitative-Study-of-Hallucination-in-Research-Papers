import requests
import os
def parse_pdf_with_science_parse(pdf_path):
    url = "http://localhost:8080/v1"  # Science Parse API URL
    headers = {"Accept": "application/json"}  # Accept JSON response

    with open(pdf_path, "rb") as pdf_file:
        files = {"file": pdf_file}
        response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        return response.json()  
    else:
        print(f"Error: {response.status_code}")
        return None
pdf_directory = "/XXXX/ACL/year2024"
parsed_data = []

list_of_list=[]
count=0

for filename in os.listdir(pdf_directory):

    if filename.endswith(".pdf"):
        try:
            count=count+1
            title_abs=[]
            pdf_file = os.path.join(pdf_directory, filename)
            parsed_data = parse_pdf_with_science_parse(pdf_file)

            title=parsed_data['title']
            title_abs.append(title)
            abstract= parsed_data['abstractText']
            title_abs.append(abstract)
            paragraphs=parsed_data['sections']
            temp=title_abs.copy()
            for p in paragraphs:
                paragraph=p['text']
                title_abs.append(paragraph)
                list_of_list.append(title_abs)
                title_abs=temp.copy()
        except:
            print("Sorry")

print(count)
