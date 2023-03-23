#include <stdio.h>
#include <unistd.h>

int main(){
	char flag[30]="flag{NULL_BYTE_1S_ENDP0INT}";
	char buf[10];
	int a=0;

	puts("Hi! Whats up?: ");
	scanf("%s", buf);

	puts("how old you?: ");
	scanf("%d",&a);
	buf[a]='a';

	printf("if you have any question, pls call me! %s!",buf);
	return 0;
}


