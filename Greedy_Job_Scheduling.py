def job_scheduling(jobs):
    jobs.sort(key = lambda x: x[1])
    schedule = []
    current_time = 0

    for i,job in enumerate(jobs):
        start,finish = job
        if start >= current_time:
            schedule.append((i+1, start, finish))
            current_time=finish
    return schedule

jobs = []
num_jobs = int(input("Enter the number of jobs : "))
for i in range(num_jobs):
    start_time = int(input(f"Enter the start time of job {i+1} : "))
    finish_time = int(input(f"Enter the finish time of job {i+1} : "))
    jobs.append((start_time,finish_time))
schedule = job_scheduling(jobs)
print("\nOptimized Schedule :")
for job in schedule:
    print("Job",job[0],":",job[1], "-",job[2])