import requests
import time
import os

def collect_privatebin_urls(base_url, output_file, delay=2):
    collected_urls = set()
    if os.path.exists(output_file):
        with open(output_file, "r") as file:
            collected_urls.update(line.strip() for line in file)

    print("Starting  URL collect")
    
    while True:
        try:
            response = requests.get(base_url, allow_redirects=False)
            if 'Location' in response.headers:
                redirect_url = response.headers['Location']
                if redirect_url not in collected_urls:
                    collected_urls.add(redirect_url)
                    with open(output_file, "a") as file:
                        file.write(redirect_url + "\n")
                    print(f"Collected: {redirect_url}")
                else:
                    print(f"Already collected: {redirect_url}")
            else:
                print("No redirect found!")
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(delay) 

if __name__ == "__main__":
    base_url = "https://privatebin.info/directory/forward-me"
    output_file = "collected_links.txt"
    collect_privatebin_urls(base_url, output_file, delay=1)
