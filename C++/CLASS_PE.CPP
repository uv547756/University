#include <iostream.h>
#include <conio.h>
class person{
char Name[64];
int age;
float salary;
char addr[64];
public:
void init(){
	cout<<"Input the values: Name, Age, Salary, Address: ";
	cin>>Name>>age>>salary>>addr;
}
void print(){
	cout<<endl<<"The information is:"<<endl;
	cout<<"Name:"<<Name<<endl<<"Age:"<<age<<endl<<"Salary: "<<salary<<endl<<"Address: "<<addr<<endl;
}
void compare(person *p);
};
void person::compare(person *p){
	int min = p[0].age;
	for(int i=1; i<5; i++){
		if(p[i].age<min)
		min = p[i].age;
		}
	int max = p[0].age;
	for(i=1; i<5; i++){
		if(p[i].age > max)
		max = p[i].age;
		}
	cout<<"Minimun age: "<<min<<endl<<"Max age: "<<max;
	}
void main(){
person p[5];
clrscr();
for(int i=0; i<5; i++){
	p[i].init();
	}
	p[0].compare(p);
	p[1].print();
getch();
}