#include<iostream.h>
#include <conio.h>
class bank{
char name[20], acc_type[10];
long no;
float acc_bal, up_bal;
public:
void details(){
	cout<<"Enter details: name, type, balance, acc_no: ";
	cin>>name>>acc_type>>acc_bal>>no;
	if(acc_bal<1000){
		cout<<"Balance must be >1000, Enter the bal again: ";
		cin>>acc_bal;
		}
	}
void deposit(){
	cout<<"Enter amount you wish to deposit: ";
	cin>>up_bal;
	acc_bal+=up_bal;
	}
void display(){
	cout<<name<<" "<<no<<" "<<acc_bal<<" "<<acc_type<<endl;
	}
void withdraw(){
	int wd;
	if(acc_bal < 1000){
		cout<<"Your acc balance is <1000, you can't withdraw"<<endl;
		}
	else{
		cout<<"Enter amount to withdraw: "<<endl;
		cin>>wd;
		acc_bal-=wd;
		cout<<"You withdrew: "<<wd<<endl;
		}
	}
};
void main(){
	bank b;
	clrscr();
	b.details();
	b.deposit();
	b.display();
	b.withdraw();
	b.display();
	getch();
}