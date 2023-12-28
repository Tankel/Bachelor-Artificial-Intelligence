#include <iostream>
#include <vector>
#include <queue>
#include <thread>
#include <mutex>

using namespace std;

// Create a mutex to protect the priority queue
mutex m;

// Define a process structure
struct process {
    int pid;        // process ID
    int arrival;    // arrival time
    int burst;      // burst time
};

// Define a comparison function for the priority queue
struct CompareProcess {
    bool operator()(const process& p1, const process& p2) const {
        return p1.arrival > p2.arrival;
    }
};

// Define a function to execute the processes for a single core
void execute_processes(int core_id, priority_queue<process, vector<process>, CompareProcess> pq, mutex& m) {
    while (!pq.empty()) {
        // Get the next process to execute
        process p = pq.top();
        pq.pop();
        
        // Execute the process
        cout << "Core " << core_id << " executing process " << p.pid << endl;
        this_thread::sleep_for(chrono::seconds(p.burst));
        
        // Release the mutex to allow other threads to access the priority queue
        m.unlock();
    }
}

int main() {
    // Create a vector of processes
    vector<process> processes = {
        {1, 0, 5},
        {2, 1, 3},
        {3, 2, 8},
        {4, 3, 6},
        {5, 4, 4}
    };
    
    // Create a priority queue to store the processes waiting to be executed
    priority_queue<process, vector<process>, CompareProcess> pq;
    for (auto p : processes) {
        pq.push(p);
    }
    
    // Create a vector of threads to simulate multiple cores
    vector<thread> threads;
    for (int i = 0; i < 2; i++) {
        threads.push_back(thread(execute_processes, i, pq, ref(m)));
    }
    
    // Wait for the threads to finish
    for (auto& t : threads) {
        t.join();
    }
    
    return 0;
}
