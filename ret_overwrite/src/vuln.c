#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>


//ここを呼び出せれば勝ち
int win(){
	__asm__(
		"mov spl, 0"
	);
	system("/bin/sh");
}

int writer(){
	char buf[10];
	int index=0;
	int value=0;

	// このほうがスタックが分かりやすかったのでforを使わないで見た
	// 1回目
	printf("type index>");
	fflush(stdout); // この関数はバッファのデータを吐き出させる関数です。問題の本質的な部分とは関係ないので無視しておｋ
	scanf("%d",&index);

	printf("type value in hex>");
	fflush(stdout);
	scanf("%x", &value);
	
	buf[index]=(char)value;
	printf("writing!\n");
	fflush(stdout);
	
	// 2回目
	printf("type index>");
	fflush(stdout);
	scanf("%d",&index);

	printf("type value in hex>");
	fflush(stdout);
	scanf("%x", &value);
	
	buf[index]=(char)value;
	printf("writing!\n");
	fflush(stdout);

	return 0;
}

int main(){
	writer();
	return 0;
}


