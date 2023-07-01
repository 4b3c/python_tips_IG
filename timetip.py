
import time
start_time = time.process_time()

print("Hello World!")
time.sleep(1)
print("Hello World but 1 second later!")

end_time = time.process_time()
print(end_time - start_time)

timestamp = time.time()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

print(timestamp) # Output: 1688183567.2664804
print(formatted_time) # Output: 2023-06-30 20:52:47
