count_done_tasks = 12
count_spend_times = 1.5
name_of_kurs = 'Python'
time_for_one_task = ((count_spend_times * 60) / count_done_tasks) / 60
print(name_of_kurs, ', всего задач:', count_done_tasks, ', затрачено часов: ', count_spend_times,
      ', среднее время выполнения ', time_for_one_task, ' часа.')
