import threading
import time

# Simulate handle request
def handle_request(req_id, duration):
    print(f"[Thread-{req_id}] Starting request {req_id}")
    # Simulate I/O-bound operation (like network/database call)
    time.sleep(duration)
    print(f"[Thread-{req_id}] Finished request {req_id}")

# List of "requests" with simulated durations
requests = [
    (1, 3),  # request_id=1, duration=3 seconds
    (2, 2),  # request_id=2, duration=2 seconds
    (3, 1),  # request_id=3, duration=1 second
]

threads = []

# Create a thread for each request
for req_id, duration in requests:
    thread = threading.Thread(target=handle_request, args=(req_id, duration))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print('All requests have been handled')