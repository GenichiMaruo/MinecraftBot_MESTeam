extern pid_t pid;
extern int rk;

typedef struct vector{
    double x;
    double y;
}Vec;
typedef struct int_vector{
    int x;
    int y;
}IntVec;
typedef struct buffer{
    Vec vec;
    int size;
    double white;
}Buf;

void attackLeft(void);
void attackRight(void);
void moveForward(void);
void moveLeft(void);
void moveRight(void);
void moveBack(void);
void moveJump(void);
void moveReset(void);


void init(void);
void setTime(void);
void setMorning(void);
void setSurvival(void);
void setCreative(void);
void cameraPos(void);

void cameraDown(void);
void cameraLeft(void);
void cameraRight(void);
void cameraUp(void);
void cameraReset(void);
void cameraResetVertical(void);
void cameraResetHorizontal(void);
void pushKey(char* key);

int kbhit(void);
void *isInterrupt(void *args);
void *exeDetectZombie(void *args);
void killPython(void);

Buf detectZombie(void);
void keyControl(IntVec, IntVec);
void exePython(void);
