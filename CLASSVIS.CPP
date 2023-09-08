#include <stdio.h>
#include <conio.h>
#include <iostream.h>
class A{
	private:
	int privdataA;
	protected:
	int protdataA;
	public:
	int pubdataA;
	};
class B:public A{
	public: void fun(){
		int a;
		a = privdataA;
		a = protdataA;
		a = pubdataA;
		}
	};
class C: private A{
	public:
	void fun(){
		int a;
		a = privdataA;
		a = protdataA;
		a = pubdataA;
		}
	};
void main(){
	int a;
	clrscr();
	B objB;
	a = objB.privdataA;
	a = objB.protdataA;
	a = objB.pubdataA;
	C objC;
	a = objC.privdataA;
	a = objC.protdataA;
	a = objC.pubdataA;
	getch();
	}
