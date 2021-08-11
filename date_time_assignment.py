import datetime

job_post = datetime.date.today()
job_exp = datetime.timedelta(days = 12)
job_valid = job_post + job_exp

print(job_post)
print(job_post.day)
print(job_post.month)
print(job_post.year)
print(job_post.ctime())

print(f"job expires on {job_valid}")
# print(f"job expires on {job_post + job_exp}")

exp_date = job_valid - job_post

print(f"job expires after {exp_date} days")
