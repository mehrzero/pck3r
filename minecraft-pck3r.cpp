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
int Tlauncher(){
	if((system("wget https://tlauncher.org/jar;unzip jar;rm README-EN.txt README-RUS.txt jar;mv TLauncher-2.75.jar .TLauncher-2.75.jar;"))!=0){
        sys_error();
        return -1;  
     }
     else{
        sys_ok();
        cout<<GRN<<"Route .TLauncher-2.75.jar was created";
        return 0;
     }	
}
int main(){
	cout<<YEL<<"\nPrerequisites for installing software minecraft are:\n\t1.Update the entire system \n\t2.install openjfx\n\t3.install openjdk-8-jre\n";
	start_install();
	chdir(HOME);
	string path=HOME;
	system("sudo apt update && sudo apt full-upgrade -y");//update and upgrade (full upgrade)
	system("sleep 3");cout<<YEL<<endl<<"next"<<WHT<<endl;//sleep system
	/* (install openjfx) * (install openjdk-8-jre)*/
	system("sudo apt install openjfx -y && sudo apt install openjdk-8-jre -y");	
	system("sleep 3");cout<<YEL<<endl<<"next"<<WHT<<endl;//sleep system
	if((Tlauncher())!=0){/* TLAUNCHER install */
		cout<<RED<<"The operation was a failure\n"<<"Tlauncher not found !\n";	   
		return 0;
	}
	else{
		
		cout<< GRN<<path+"/.TLauncher-2.75.jar\n"<<"Please try : \n$ pck3r minecraft\n";
	}
	
	return 0;
}