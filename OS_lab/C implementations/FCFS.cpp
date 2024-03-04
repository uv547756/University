#include <iostream>
using namespace std;

int main(){
    int a[10], n, w[10], avg = 0, i;
    cout<<"Enter the no. of Jobs: ";
    cin>>n;
    for(i=0; i<n;i++){
        cout<<"Enter time taken for Job"<<i+1<<": ";
        cin>>a[i];
    }
    w[0] = 0;
    for(i=0;i<n;i++){
        w[i+1]=w[i]+a[i];
    }
    cout<<"\nGantt Chart for the given Jobs: \n";
    for(i=0;i<n;i++){
        cout<<"J"<<i+1<<"\t";
    }
    cout<<"\n";
    for(i=0;i<n;i++){
        cout<<w[i]<<"\t";
    }
    w[n]=w[n-1]+a[n-1];
    cout<<w[n];
    cout<<"\n\nReadQ. \tTime \t Wait Time";
    for(i=0;i<n;i++){
        avg += w[i];
    }
    avg /= n;
    cout<<"\n Average Wait Time: "<<avg<<"\n\n";
    return 0;
}
