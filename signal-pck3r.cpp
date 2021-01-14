#include <iostream> 
#include <string.h>
#include <unistd.h>
/* mehrzero@gmail.com * https://github.com/mehrzero */
#define RED  "\x1B[31m" /*color zone*/
#define GRN  "\x1B[32m" 
#define YEL  "\x1B[33m" 
#define WHT  "\x1B[37m" 
using namespace std;
const char *HOME= getenv("HOME");

void sys_error();
void sys_ok();
void start_install();
int software_key();

int main(){
	cout<<YEL<<"\nPrerequisites for installing software signal are:\n\t1.Update the entire system \n\t2.software signing key\n\t3.repository\n";
	start_install();
	chdir(HOME);
	system("sudo apt update && sudo apt full-upgrade -y");//update and upgrade (full upgrade)
	system("sleep 3");cout<<YEL<<endl<<"next"<<WHT<<endl;//sleep system
	if((software_key())!=0){/* software signing key */
		cout<<RED<<"The operation was a failure\n"<<"software signing key !\n";	   
		return 0;
	}
	else{	
		cout<< GRN<<" software signing key \n";
	}
	system("sleep 3");cout<<YEL<<endl<<"next"<<WHT<<endl;//sleep system
	/*Add our repository to your list of repositories*/
	system("sudo echo 'deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main' | sudo tee -a /etc/apt/sources.list.d/signal-xenial.list");
	system("sleep 3");cout<<YEL<<endl<<"next"<<WHT<<endl;//sleep system
	system("sudo apt install signal-desktop");
	cout<<"Please try : \n$ pck3r signal\n";
	//
	system("signal-desktop");
	return 0;
}

void sys_error(){
     cout<<RED<<"尸⼕长㇌尺 : ERROR !"<<WHT<<endl;/* error */
 }
void sys_ok(){
     cout<<GRN<<"尸⼕长㇌尺 : OK !"<<WHT<<endl;/*no error*/
}
void start_install(){
	cout<<YEL<<endl<<"Press ENTER key to continue ..."<<WHT;
	getchar();cout<<WHT<<endl;
}

int software_key(){
	if((system("sudo wget -O- https://updates.signal.org/desktop/apt/keys.asc | sudo apt-key add -"))!=0){
        sys_error();
        return -1;  
     }
     else{
        sys_ok();
        cout<<GRN<<"The official key of the public software signature is installed";
        return 0;
     }	
}
