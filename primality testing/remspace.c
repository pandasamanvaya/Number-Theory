#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

	FILE *fin, *fout;
	char buf;

	if(argc != 3){
		fprintf(stderr, "Usage : [program] [in_file] [out_file]\n");
		exit(1);
	}

	fin = fopen(argv[1], "r");
	fout = fopen(argv[2], "w");

	while(fscanf(fin, "%c", &buf) != EOF){
		if(buf == ' ' || buf == '\n');
		else
			fprintf(fout, "%c", buf);
	}

	fclose(fin);
	fclose(fout);

	exit(1);
}