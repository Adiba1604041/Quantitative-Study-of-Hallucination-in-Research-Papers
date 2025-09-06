import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

def download_acl_2024_papers(output_dir="ACL_2024_Papers", max_papers=450):
   
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # ACL 2024 proceedings URL
    url = "https://aclanthology.org/events/acl-2024/"
    
    print(f"Downloading up to {max_papers} papers from ACL 2024...")
    
    try:
        # Fetch the page
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all paper entries - this targets the ACL 2020 specific page structure
        paper_entries = soup.find_all('p', class_='d-sm-flex align-items-stretch')
        
        downloaded_count = 0
        
        for entry in paper_entries:
            if downloaded_count >= max_papers:
                break
                
            # Find PDF link
            pdf_link = entry.find('a', class_='badge badge-primary align-middle mr-1', href=True)
            if not pdf_link:
                continue
                
            pdf_url = pdf_link['href']
            
            # Handle relative URLs
            if not pdf_url.startswith('http'):
                pdf_url = urljoin(url, pdf_url)
            
            # Extract paper title for filename
            title = entry.find('strong')
            title_text = title.get_text(strip=True) if title else "paper"
            
            # Create safe filename
            filename = f"{downloaded_count+1:03d}_{title_text[:50]}.pdf".replace(' ', '_').replace('/', '_')
            save_path = os.path.join(output_dir, filename)
            
            # Skip if already downloaded
            if os.path.exists(save_path):
                print(f"  Already exists: {filename}")
                continue
            
            # Download the paper
            print(f"  Downloading {downloaded_count+1}/{max_papers}: {title_text[:50]}...")
            try:
                pdf_response = requests.get(pdf_url, headers=headers, stream=True)
                pdf_response.raise_for_status()
                
                with open(save_path, 'wb') as f:
                    for chunk in pdf_response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                downloaded_count += 1
                
                # delay between requests
                time.sleep(1)
            
            except Exception as e:
                print(f"    Failed to download {title_text[:50]}: {str(e)}")
                continue
        
        print(f"\nSuccessfully downloaded {downloaded_count} papers to '{output_dir}'")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    OUTPUT_DIR = "/XXXX/ACL/year_2024"
    
    MAX_PAPERS = 401
    
    download_acl_2024_papers(OUTPUT_DIR, MAX_PAPERS)