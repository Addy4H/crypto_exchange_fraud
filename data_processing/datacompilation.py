import json
import csv
from datetime import datetime
import os

Features = ['domain', 'trust_score', 'blacklisted', 'ip_bad_count_total', 'ip_bad_count_bad', 'ssl_valid',
'ip_country', 'anonymous_whois', 'alexa_rank', 'dnsblock_threat_count', 'whois_registration_duration', 'whois_valid_email',
'avg_review_score', 'facebook_comments_total_count', 'facebook_comments_negative_count', 'facebook_comments_positive_count',
'popularity_rank','scamadviser_votes_legit', 'scamadviser_votes_scam', 'scamadviser_votes_fake', 'is_legit']


def calculate_average_review_score(reviews):
    total_score, total_reviews = 0, 0
    for review in reviews:
        avg_score = review.get('avg_score') or 0
        count = review.get('count') or 0
        total_score += avg_score * count
        total_reviews += count
    return round(total_score / total_reviews, 2) if total_reviews else 0


def get_site_registration_duration(data):
    date_format = "%Y-%m-%d"
    # Extract dates
    date_created_str = data['whois']['registration_created'] if 'whois' in data else None
    # date_expires_str = data['whois']['registration_expires'] if 'whois' in data else None

    if  date_created_str is None:
        return 0

    # Convert strings to datetime objects
    date_created = datetime.strptime(date_created_str, date_format)
    today_date = datetime.now()

    # Calculate difference in years
    duration = (today_date - date_created)
    years_difference = duration.days / 365
    # print("year difference: ", years_difference)
    return round(years_difference, 2)


def append_to_csv(data, filename):
    fields = Features
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        
        ip_bad_count = data['ip_bad_count'] if 'ip_bad_count' in data else None
        network_info = data['networkinfo']['ip']['country'] if ('networkinfo' in data and 'ip' in data['networkinfo'] and 'country' in data['networkinfo']['ip']) else None
        dns_threat = data['dnsblock']['threat'] if 'dnsblock' in data else None
        facebook_comments = data['facebook_comments'] if 'facebook_comments' in data else None
        scamadviser_votes = data['scamadviser_votes'] if 'scamadviser_votes' in data else None
        average_review_score = calculate_average_review_score(data['reviews']) if 'reviews' in data else 0

        registration_duration = get_site_registration_duration(data)
        writer.writerow({
            'domain': data['domain'] if 'domain' in data else None,
            'trust_score': data['score'] if 'score' in data else -1,
            'blacklisted': data['blacklisted'] if 'blacklisted' in data else False,
            'ip_bad_count_total': ip_bad_count['total'] if ip_bad_count else 0,
            'ip_bad_count_bad': ip_bad_count['bad'] if ip_bad_count else 0,
            'ssl_valid': data['ssl']['valid'] if 'ssl' in data else False,
            'ip_country': network_info,
            'anonymous_whois': data['whois']['anonymous_whois'] if 'whois' in data else False,
            'alexa_rank': data['alexa']['rank'] if 'alexa' in data and data['alexa']['rank'] else -1,
            'dnsblock_threat_count': dns_threat['count'] if dns_threat else 0,
            'whois_registration_duration': registration_duration,
            'whois_valid_email': data['whois']['registrant']['valid_email'] if 'whois' in data else False,
            'avg_review_score': average_review_score,
            'facebook_comments_total_count': facebook_comments['total_count'] if facebook_comments else 0,
            'facebook_comments_negative_count': facebook_comments['negative']['comment_count'] if facebook_comments else 0,
            'facebook_comments_positive_count': facebook_comments['positive']['comment_count'] if facebook_comments else 0,
            'popularity_rank': data['popularity']['rank'] if 'popularity' in data else -1,
            'scamadviser_votes_legit': scamadviser_votes['count_legit'] if scamadviser_votes and scamadviser_votes['count_legit']else 0,
            'scamadviser_votes_scam': scamadviser_votes['count_scam'] if scamadviser_votes and scamadviser_votes['count_scam'] else 0,
            'scamadviser_votes_fake': scamadviser_votes['count_fake'] if scamadviser_votes and scamadviser_votes['count_fake'] else 0,
            'is_legit': False
            })



# write headers to csv
with open('fraud.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=Features)
    writer.writeheader()


folder_path = '700blacklist'
json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

for json_file in json_files:
    with open(os.path.join(folder_path, json_file), 'r', encoding='utf-8') as file:
        data = json.load(file)
        append_to_csv(data, 'fraud.csv')

