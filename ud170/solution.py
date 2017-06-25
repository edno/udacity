import unicodecsv
from datetime import datetime
from collections import defaultdict
import numpy as np

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

def set_record_type(data, column, data_type):
    for record in data:
        if record[column]:
            if data_type == 'float':
                record[column] = float(record[column])
            elif data_type == 'integer':
                record[column] = int(float(record[column]))
            elif data_type == 'date':
                record[column] = datetime.strptime(record[column],'%Y-%m-%d')
            elif data_type == 'boolean':
                record[column] = bool(record[column])
        else:
            record[column] = None
    return data

def get_unique_students(data):
    return set([rec['account_key'] for rec in data])

def remove_udacity_account(data):
    return [rec for rec in data if rec['account_key'] not in udacity_test_accounts]

def remove_free_trial(data):
    return [rec for rec in data if rec['account_key'] in paid_students]

def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7 and time_delta.days >= 0

def sum_grouped_data(data, entry):
    sum_group = {}
    for key,record in data.items():
        total = 0
        for rec in record:
            total += rec[entry]
        sum_group[key] = total
    return sum_group

def print_statistics(data):
    data_list = list(data.values())
    print('Mean:', np.mean(data_list))
    print('Standard deviation:', np.std(data_list))
    print('Minimum:', np.min(data_list))
    print('Maximum:', np.max(data_list))

def group_data_by(data, key):
    grouped_data = defaultdict(list)
    for rec in data:
        group_key = rec[key]
        grouped_data[group_key].append(rec)
    return grouped_data

enrollments = read_csv('./ud170/resources/enrollments.csv')
daily_engagement = read_csv('./ud170/resources/daily_engagement.csv')
project_submissions = read_csv('./ud170/resources/project_submissions.csv')

enrollments = set_record_type(enrollments, 'join_date', 'date')
enrollments = set_record_type(enrollments, 'cancel_date', 'date')
enrollments = set_record_type(enrollments, 'days_to_cancel', 'integer')
enrollments = set_record_type(enrollments, 'is_udacity', 'boolean')
enrollments = set_record_type(enrollments, 'is_canceled', 'boolean')

daily_engagement = set_record_type(daily_engagement, 'utc_date', 'date')
daily_engagement = set_record_type(daily_engagement, 'num_courses_visited', 'integer')
daily_engagement = set_record_type(daily_engagement, 'total_minutes_visited', 'float')
daily_engagement = set_record_type(daily_engagement, 'lessons_completed', 'integer')
daily_engagement = set_record_type(daily_engagement, 'projects_completed', 'integer')

project_submissions = set_record_type(project_submissions, 'creation_date', 'date')
project_submissions = set_record_type(project_submissions, 'completion_date', 'date')

for rec in daily_engagement:
    rec['account_key'] = rec['acct']
    del[rec['acct']]

enrollment_num_rows = len(enrollments)
enrollment_unique_students = get_unique_students(enrollments)
enrollment_num_unique_students = len(enrollment_unique_students)

engagement_num_rows = len(daily_engagement)
engagement_unique_students = get_unique_students(daily_engagement)
engagement_num_unique_students = len(engagement_unique_students)

submission_num_rows = len(project_submissions)
submission_unique_students = get_unique_students(project_submissions)
submission_num_unique_students = len(submission_unique_students)

problem_students_num = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in engagement_unique_students and enrollment['join_date'] != enrollment['cancel_date']:
        problem_students_num += 1

udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity'] == 'True':
        udacity_test_accounts.add(enrollment['account_key'])

enrollments_non_udacity = remove_udacity_account(enrollments)
engagement_non_udacity = remove_udacity_account(daily_engagement)
submission_non_udacity = remove_udacity_account(project_submissions)

paid_students = {}
for enrollment in enrollments_non_udacity:
    if not enrollment['days_to_cancel'] or enrollment['days_to_cancel'] > 7:
        student = enrollment['account_key']
        join_date = enrollment['join_date']
        if student not in paid_students or join_date > paid_students[student]:
            paid_students[student] = join_date

enrollments_paid = remove_free_trial(enrollments_non_udacity)
engagement_paid = remove_free_trial(engagement_non_udacity)
submission_paid = remove_free_trial(submission_non_udacity)

paid_engagement_in_first_week = []
for rec in engagement_paid:
    student = rec['account_key']
    if within_one_week(paid_students[student], rec['utc_date']):
        paid_engagement_in_first_week.append(rec)

engagement_by_account = group_data_by(paid_engagement_in_first_week, 'account_key')

total_minutes_by_accounts = sum_grouped_data(engagement_by_account,'total_minutes_visited')
print_statistics(total_minutes_by_accounts)

total_lessons_completed_by_accounts = sum_grouped_data(engagement_by_account,'lessons_completed')
print_statistics(total_lessons_completed_by_accounts)

for _,record in engagement_by_account.items():
    for rec in record:
        rec['has_visited'] = 1 if rec['num_courses_visited'] > 0 else 0

total_num_courses_visited = sum_grouped_data(engagement_by_account,'has_visited')
print_statistics(total_num_courses_visited)

subway_project_lesson_keys = ['746169184','3176718735']
rating_pass_values = ['PASSED','DISTINCTION']
pass_subway_project = set()
for rec in submission_paid:
    if rec['lesson_key'] in subway_project_lesson_keys and rec['assigned_rating'] in rating_pass_values:
        pass_subway_project.add(rec['account_key'])

print(len(pass_subway_project))

passing_engagement = []
non_passing_engagement = []
for rec in paid_engagement_in_first_week:
    if rec['account_key'] in pass_subway_project:
        passing_engagement.append(rec)
    else:
        non_passing_engagement.append(rec)

print(len(passing_engagement))
print(len(non_passing_engagement))
