import time
import logging
import threading
import concurrent.futures


def thread_function(name):
	logging.info("Thread %s: starting", name)
	time.sleep(2)
	logging.info("Thread %s: finishing", name)


def create_single_thread():
	format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format, level=logging.INFO, datefmt="%H%M%S")
	logging.info("Main 		:before creating thread")
	"""
	Create a new thread with function of thread_function()
	A daemon thread will shut down immediately when the program exits, while
	the main thread will wait the thread if its not a daemon thread
	"""
	x = threading.Thread(target=thread_function, args=(1,), daemon=False)	# Try daemon=True

	logging.info("Main 		:before runing thread")
	# start the tread
	x.start()

	logging.info("Main 		:wait for the thread to finish")

	# x.join()	# To tell main thread wait thread x, before it exits.

	logging.info("Main 		: all done")


# using a threadPoolExecutor
def create_threads_with_threadPool():
	format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format, level=logging.INFO, datefmt="%H%M%S")
	with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
		executor.map(thread_function, range(3))


if __name__ == "__main__":
	# create_single_thread()
	create_threads_with_threadPool()


# using a threadPoolExecutor
if __name__ == "__main__":
	format





