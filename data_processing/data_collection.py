import requests
import csv
import time
import json
import os

Features = ['domain', 'domain_age', 'blacklisted', 'dnsblock_threat_count', 'ip_bad_count_total',
            'ip_bad_count_bad', 'facebook_comments_total_count', 'facebook_comments_negative_comment_count',
            'popularity_rank', 'average_review_score', 'whois_domain_status',
            'whois_registration_created', 'whois_registration_expires', 'whois_registrant_country', 'whois_valid_email',
            'ssl_valid']


def get_features(domain):
    url = "https://scamadviser1.p.rapidapi.com/v1/trust/single"
    querystring = {"domain": domain, "refresh": "false"}
    headers = {
    'x-rapidapi-key': "api-key",
    'x-rapidapi-host': "scamadviser1.p.rapidapi.com"
}
    response = requests.get(url, headers=headers, params=querystring)
    save_json(response.json(), website)
    return response.json()


def save_json(data, domain):
    # Remove protocol (http, https) and www, then split by '/' to get the domain part
    simplified_domain = domain.replace("http://", "").replace("https://", "").replace("www.", "").split("/")[0]
    # Extract the basic domain name without TLD
    simplified_domain = simplified_domain.split(".")[0]
    folder_path = "newblackjsons"
    filename = f"{simplified_domain}.json"
    full_path = os.path.join(folder_path, filename)

    with open(full_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

websites = [ ] # list of websites go hers
for website in websites:
    data = get_features(website)
    time.sleep(120)
