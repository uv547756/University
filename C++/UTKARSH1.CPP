#include <iostream.h>
#include <conio.h>
#include <stdio.h>
class B{
	int a;
	public:
	int b;
	void get_ab();
	int get_a();
	void show_a();
	};
class D:public B{
	int c;
	public:
	void multiply();
	void display();
	};
	void B::get_ab(){
	a=5;
	b=10;
	}
	int B::get_a(){
	return a;
	}
	void D::multiply(){
	c=get_a()*b;
	}
	void B::show_a(){
	cout<<a<<endl;
	}
	void D::display(){
	cout<<"a=";show_a();
	cout<<"b="<<b<<endl;
	cout<<"c="<<c<<endl;
	}
int main(){
	D d;
	clrscr();
	d.get_ab();
	d.multiply();
	d.show_a();
	d.display();
	d.b = 20;
	d.multiply();
	d.display();
	getch();
	return 0;
	}
