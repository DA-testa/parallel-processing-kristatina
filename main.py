# python3
import heapq
def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    
    for i in range(m):
        time = data[i]
        completion_time, thread_index = heapq.heappop(threads)
        new_completion_time = completion_time + time
        heapq.heappush(threads, (new_completion_time, thread_index))
        output.append((thread_index, completion_time))

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    #n = 0
    #m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_index, completion_time in output:
        print(thread_index, completion_time)


if __name__ == "__main__":
    main()
