import unicodecsv

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