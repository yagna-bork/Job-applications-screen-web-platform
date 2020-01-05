from crontab import CronTab

cron = CronTab(user=True)

job = cron.new(command = '/Library/Frameworks/Python.framework/Versions/3.7/bin/python3 /Users/nathanbailey/OneDrive/Uni/Year2/Term2/CS261/GroupProject/Code/Project/MachineLearning/report.py')
job.minute.every(1)

cron.write()

