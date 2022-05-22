#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <err.h>
#include <termios.h>
#include <fcntl.h>
#include <windows.h>
#include "control.h"
#include <pthread.h>

pid_t Ppid;
pid_t Kpid;
int rk=1;
IntVec camera_direction = {0};
IntVec character_direction = {0};

void attackLeft(void){
    char com[128] = "python/minecraft/clickLeft.py";
    pid_t c_pid = fork();
    if (c_pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (c_pid == 0) {
        int f = execl("python/python.exe" , "python/python.exe" ,com , NULL);
        if(f != 0 && WEXITSTATUS(f) != 0 ){
            printf("error:attackLeft\n");
            exit(1);
        }
    }
}
void attackRight(void){
    char com[128] = "python/python.exe python/minecraft/clickRight.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:attackRight\n");
        exit(1);
    }
}

void moveForward(void){
    character_direction.x = 1;
    keyControl(camera_direction, character_direction);
}
void moveLeft(void){
    character_direction.y = -1;
    keyControl(camera_direction, character_direction);
}
void moveRight(void){
    character_direction.y = 1;
    keyControl(camera_direction, character_direction);
}
void moveBack(void){
    character_direction.x = -1;
    keyControl(camera_direction, character_direction);
}
void moveJump(void){
    //未実装
    keyControl(camera_direction, character_direction);
}
void moveReset(void){
    character_direction.x = 0;
    character_direction.y = 0;
    keyControl(camera_direction, character_direction);
}


void init(void){
    char com[128] = "python/python.exe python/minecraft/init.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:init\n");
        exit(1);
    }
}

void setTime(void){
    char com[128] = "python/python.exe python/minecraft/setTime.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:init\n");
        exit(1);
    }
}

void setMorning(void){
    char com[128] = "python/python.exe python/minecraft/setMorning.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:init\n");
        exit(1);
    }
}

void setSurvival(void){
    char com[128] = "python/python.exe python/minecraft/setSurvival.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:init\n");
        exit(1);
    }
}

void setCreative(void){
    char com[128] = "python/python.exe python/minecraft/setCreative.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:init\n");
        exit(1);
    }
}

void cameraPos(void){
    char com[128] = "python/python.exe python/minecraft/initCameraPos.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:cameraPos\n");
        exit(1);
    }
}

void cameraDown(void){
    camera_direction.y = -1;
    keyControl(camera_direction, character_direction);
}
void cameraLeft(void){
    camera_direction.x = -1;
    keyControl(camera_direction, character_direction);
}
void cameraRight(void){
    camera_direction.x = 1;
    keyControl(camera_direction, character_direction);
}
void cameraUp(void){
    camera_direction.y = 1;
    keyControl(camera_direction, character_direction);
}
void cameraReset(void){
    camera_direction.x = 0;
    camera_direction.y = 0;
    keyControl(camera_direction, character_direction);
}
void cameraResetVertical(void){
    camera_direction.y = 0;
    keyControl(camera_direction, character_direction);
}
void cameraResetHorizontal(void){
    camera_direction.x = 0;
    keyControl(camera_direction, character_direction);
}

void pushKey(char* key){
    char com[128] = "python/python.exe python/minecraft/pushKey.py ";
    strcat(com, key);
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:pushKey\n");
        exit(1);
    }
}


int kbhit(void){
    struct termios oldt, newt;
    int ch;
    int oldf;

    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
    fcntl(STDIN_FILENO, F_SETFL, oldf | O_NONBLOCK);

    ch = getchar();

    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    fcntl(STDIN_FILENO, F_SETFL, oldf);

    if (ch != EOF){
        ungetc(ch, stdin);
        return 1;
    }

    return 0;
}

Buf detectZombie(void){
    FILE	*fp;
	char	fname[] = "tmp.txt";
    int tmp = 0;
    double d_tmp = 0;
    Buf buf = {0};

	if ( (fp=fopen(fname,"r")) ==NULL) {
		printf("error:detectZombie\n");
		exit(1);
	}
	fscanf(fp, "%d", &tmp);
    buf.vec.x = tmp / 10.0;
    fscanf(fp, "%d", &tmp);
    buf.vec.y = tmp / 10.0;
    fscanf(fp, "%d", &tmp);
    buf.size = tmp;
    fscanf(fp, "%lf", &d_tmp);
    buf.white = d_tmp;
	(void) fclose(fp);

    return buf;
}
void keyControl(IntVec camera, IntVec character){
    FILE *fp;
    char fname[] = "control.txt";
    if ( (fp=fopen(fname,"w")) ==NULL) {
		printf("error:keyControl\n");
		exit(1);
	}
    fprintf(fp, "%d\n%d\n%d\n%d\n", camera.x, camera.y, character.x, character.y);
	(void) fclose(fp);
}

void killPython(void){
    int ret1,ret2;
    ret1 = kill(Ppid, SIGKILL);
    ret2 = kill(Kpid, SIGKILL);
    if (ret1 == -1 || ret2 == -1) {
        perror("error:kill");
        exit(1);
    }
}

void *exeDetectZombie(void *args){
    char com[128] = "python/python.exe python/minecraft/detectZombie.py";
    
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:pushKey\n");
        exit(1);
    }
}

void *isInterrupt(void *args){
    while(1){
        if (GetKeyState(VK_F12) < 0 ){
            fprintf(stderr , "終了コード送信\n" );
            killPython();
            rk=0;
        }
        Sleep(100);
    }
    rk=0;
}

void exePython(void){
    char com[128] = "python/python.exe python/minecraft/aiDetector.py";

    pthread_t key;
    int ret;
    keyControl(camera_direction, character_direction); //ファイルのリセット
    Ppid = fork ();
    if (-1 == Ppid){
        err (EXIT_FAILURE, "can not fork");
        exit(-1);
    }else if (0 == Ppid){
        int f = execl("python/python.exe" , "python/python.exe" ,"python/minecraft/aiDetector.py" , NULL);
        if(f != 0 && WEXITSTATUS(f) != 0 ){
            printf("error:exePython\n");
            exit(1);
        }
    }
    Sleep(100);
    Kpid = fork ();
    if (-1 == Kpid){
        err (EXIT_FAILURE, "can not fork");
        exit(-1);
    }else if (0 == Kpid){
        int f = execl("python/python.exe" , "python/python.exe" ,"python/minecraft/keyControl.py" , NULL);
        if(f != 0 && WEXITSTATUS(f) != 0 ){
            printf("error:exePython\n");
            exit(1);
        }
    }
   
    if ((ret = pthread_create(&key, NULL, &isInterrupt , NULL)) != 0) {
        fprintf(stderr, "スレッド作成失敗");
        exit(1);
    }
}