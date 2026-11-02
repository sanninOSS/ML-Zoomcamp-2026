import json
from urllib.request import Request, urlopen

lead = {
    'lead_source': 'organic_search',
    'industry': 'technology',
    'employment_status': 'employed',
    'location': 'europe',
    'number_of_courses_viewed': 4,
    'annual_income': 80304.0,
    'interaction_count': 7,
    'lead_score': 0.74,
}

body = json.dumps(lead).encode('utf-8')
request = Request(
    'http://127.0.0.1:9696/predict',
    data=body,
    headers={'Content-Type': 'application/json'},
)

with urlopen(request, timeout=20) as response:
    result = json.load(response)

print(result)
print('Conversion probability:', result['conversion_probability'])
