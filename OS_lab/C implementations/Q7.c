//Implementing "ls" unix command using C.
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <dirent.h>
void main(int argc, char *argv[]){
    DIR *dp;
    struct dirent *dirp;
    if(argc<2){
        printf("Need more than 1 arguement. \n");
        exit(1);
    }
    if((dp=opendir(argv[1]))==NULL){
        printf("\n Cannot open %s file. \n",argv[1]);
        exit(1);
    }
while((dirp=readdir(dp))!=NULL)
printf("%s \n",dirp->d_name);
closedir(dp);
}