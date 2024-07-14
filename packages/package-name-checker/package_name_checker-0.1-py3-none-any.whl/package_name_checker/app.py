from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = 'your_secret_key'

GOOGLE_PLAY_DETAILS_URL = "https://play.google.com/store/apps/details?id={}"

def get_app_details(package_name):
    url = GOOGLE_PLAY_DETAILS_URL.format(package_name)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting app name
        app_name_tag = soup.find('h1', class_='Fd93Bb')
        app_name = app_name_tag.text.strip() if app_name_tag else "N/A"

        # Extracting developer name
        developer_name_tag = soup.find('div', class_='Vbfug auoIOc').find('span')
        developer_name = developer_name_tag.text.strip() if developer_name_tag else "N/A"

        # Extracting app icon URL
        app_icon_tag = soup.find('img', class_='T75of nm4vBd arM4bb')
        app_icon_url = app_icon_tag['src'] if app_icon_tag else ""

        # Extracting app rating
        app_rating_tag = soup.find('div', itemprop='starRating').find('div', class_='TT9eCd')
        app_rating = app_rating_tag.text.strip().split(' ')[0] if app_rating_tag else "N/A"

        # Extracting number of reviews
        num_reviews_tag = soup.find('div', class_='g1rdde')
        num_reviews = num_reviews_tag.text.strip() if num_reviews_tag else "N/A"

        # Extracting number of downloads
        downloads_tag = soup.select_one('div.wVqUob > div.ClM7O')
        downloads = downloads_tag.text.strip() if downloads_tag else "N/A"

        return {
            'package_name': package_name,
            'app_name': app_name,
            'developer_name': developer_name,
            'app_icon_url': app_icon_url,
            'app_rating': app_rating,
            'num_reviews': num_reviews,
            'downloads': downloads,
            'url': url
        }
    else:
        return None

@app.route('/get_app_details', methods=['POST'])
def get_app_details_api():
    data = request.json
    app_name = data.get('app_name', '').strip().lower()
    company_name = data.get('company_name', '').strip().lower()

    # Construct package name
    package_name = f"com.{app_name}.{company_name}"
    
    # Get app details
    app_details = get_app_details(package_name)
    if app_details:
        return jsonify(app_details)
    else:
        return jsonify({'message': 'Package name is unique!'})

if __name__ == '__main__':
    app.run(debug=True)