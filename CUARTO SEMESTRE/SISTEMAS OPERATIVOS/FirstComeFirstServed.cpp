#include <iostream>
#include <time.h>

using namespace std;

int main()
{
    srand(time(NULL));

    int n, bt[20], wt[20], tat[20], avwt = 0, avtat = 0, i, j;
    cout << "Enter total number of processes(maximum 20): ";
    cin >> n;

    //cout << "\nEnter Process Burst Time aka DURATION \n";
    for (i = 0; i < n; i++)
    {
        bt[i] = rand()%50 + 1;
        //cout << "P[" << i + 1 << "]:";
        //cin >> bt[i];
    }
    // tiempo de espera del primer procesos es 0
    wt[0] = 0;
    // calculamaos tiempo de espera de los otros procesos
    for (i = 1; i < n; i++)
    {
        wt[i] = 0;
        for (j = 0; j < i; j++)
            wt[i] += bt[j];
    }
    cout << "\nProcess\t\tBurst Time\tWaiting Time\tTurnaround Time";
    // calculating turnaround time
    for (i = 0; i < n; i++)
    {
        tat[i] = bt[i] + wt[i];
        avwt += wt[i];
        avtat += tat[i];
        cout << "\nP[" << i + 1 << "]" << "\t\t" << bt[i] << "\t\t" << wt[i] << "\t\t" << tat[i];
    }
    avwt /= i;
    avtat /= i;
    cout << "\n\nAverage Waiting Time: " << avwt;
    cout << "\nAverage Turnaround Time: " << avtat;

    return 0;
}