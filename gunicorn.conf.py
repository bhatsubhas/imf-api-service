import multiprocessing

bind = "0.0.0.0:9080"
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = "-"
