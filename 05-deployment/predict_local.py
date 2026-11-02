from pathlib import Path
import pickle
import sys

source = Path(__file__).resolve().parent / '.course/cohorts/2026/homework/05-deployment'
sys.path.insert(0, str(source))

from model import normalize_record

lead = {
    'lead_source': 'paid_ads',
    'industry': 'technology',
    'employment_status': 'employed',
    'location': 'north_america',
    'number_of_courses_viewed': 2,
    'annual_income': 79276.0,
    'interaction_count': 4,
    'lead_score': 0.41,
}

with open(source / 'pipeline.bin', 'rb') as f:
    pipeline = pickle.load(f)

probability = pipeline.predict_proba([normalize_record(lead)])[0, 1]
print('Q3:', float(probability))
