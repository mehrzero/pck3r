#include <iostream>
#define RED  "\x1B[31m" /*color zone*/
#define GRN  "\x1B[32m" 
#define YEL  "\x1B[33m" 
#define WHT  "\x1B[37m" 
using namespace std;
void sys_error(){
	system("sleep 1");
    cout<<RED<<"尸⼕长㇌尺 : ERROR !"<<WHT<<endl;/* error */
 }
void sys_ok(){
	system("sleep 1");
    cout<<GRN<<"尸⼕长㇌尺 : OK !"<<WHT<<endl;/*no error*/
}
int main(int argc, char **argv){
	string browser="";
	cout<<YEL<<"Select your browser:\n\t 1 or firefox\n\t 2 or chrome\n\t 3 or chromium\n\t 4 or brave\n\t 5 or opera "<<WHT;
	while(true){
		cout<<YEL<<"\n➜  "<<WHT;
		cin>>browser;
		cout<<endl;
		if(browser=="1" || browser =="firefox" ){/*browser -> firefox*/
			if((system("firefox https://github.com/amzy-0/pck3r"))!=0){
				cout<<RED<<"This browser does not exist \nPlease try again"<<endl<<WHT;
			}
			else{sys_ok();return 0;}
		}
		else if(browser=="2" || browser =="chrome" ){/*browser -> chrome*/
			if((system("chrome https://github.com/amzy-0/pck3r"))!=0){
				cout<<RED<<"This browser does not exist \nPlease try again"<<endl<<WHT;
			}
			else{sys_ok();return 0;}
		}
		else if(browser=="3" || browser =="chromium" ){/*browser -> chromium*/
			if((system("chromium https://github.com/amzy-0/pck3r"))!=0){
				cout<<RED<<"This browser does not exist \nPlease try again"<<endl<<WHT;
			}
			else{sys_ok();return 0;}
		}
		else if(browser=="4" || browser =="brave" ){/*browser -> brave*/
			if((system("brave https://github.com/amzy-0/pck3r"))!=0){
				cout<<RED<<"This browser does not exist \nPlease try again"<<endl<<WHT;
			}
			else{sys_ok();return 0;}
		}
		else if(browser=="5" || browser =="opera" ){/*browser -> opera*/
			if((system("opera https://github.com/amzy-0/pck3r"))!=0){
				cout<<RED<<"This browser does not exist \nPlease try again"<<endl<<WHT;
			}
			else{sys_ok();return 0;}
		}
		else{sys_error();}	
	}
	return 0;
}
