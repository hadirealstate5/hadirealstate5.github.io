import requests

# Aapka IndexNow API Key
api_key = "eeaf6ecb33cd40c1a1b1e88094c54418"

# 🔽 Yaha pe apne URLs daalo — jitne chahe
urls = [
    "https://www.easyfie.com/read-blog/2387165_full-list-of-official-expedi-customer-service-contact-numbers-in-usa-the-ultimate-official-guide",
"https://www.easyfie.com/read-blog/2387173_full-list-of-expedi-customerservice-number-in-usa-official-expedi-help-center",
"https://www.easyfie.com/read-blog/2387176_complete-official-list-of-expedi-customer-contact-numbers-in-usa-a-ultimate-step-by-step-guide"
]

# Loop ke through har URL ko submit karenge
for url in urls:
    endpoint = "https://www.bing.com/indexnow"
    params = {
        "url": url,
        "key": api_key
    }

    response = requests.get(endpoint, params=params)

    print(f"Submitted: {url}")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
    print("-" * 40)




