import unicodecsv
from datetime import datetime as dt

enrollments_filename = 'data/enrollments.csv'
engagement_filename = 'data/daily_engagement.csv'
submissions_filename = 'data/project_submissions.csv'

with open(enrollments_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

print(enrollments[0])
print('---------------')

with open(engagement_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    engagement = list(reader)
print(engagement[0])
print('---------------')

with open(submissions_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    submission = list(reader)
print(submission[0])
print('---------------')

# now lets update the values of enrolment for all strings, eg is_canceled should be boolean and cancel_date should be date

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

def if_int(i):
    if i == '':
        return None
    else:
        return int(i)


for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = if_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

print(enrollments[0])
print('------enrollment cleaned up -----------')

