import multiprocessing

core_count = [i +1  for i in range(multiprocessing.cpu_count())]

print([i for i in core_count])