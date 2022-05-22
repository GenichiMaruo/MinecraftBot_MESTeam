#include <stdio.h>
#include <unistd.h>
#include "control.h"
#include <time.h>
#include <windows.h>

enum LastZombie {
    Left,
    Right
};

int main(char *argv){
    Buf buf, old_buf = {0};
    time_t zerotime = time(NULL), nowtime;
    int flag=0;
    int last_zombie=Left;
    double fps=24.0;
    init();
    setTime();
    exePython();
    setSurvival();
    buf = detectZombie();
    while(rk){
        while(buf.size!=0&&(buf.size==old_buf.size&&buf.white==old_buf.white)){
            Sleep(1000/fps);
            buf = detectZombie();
        }
        printf("cprogram: [%.1f, %.1f] %d %.1f%%\n", buf.vec.x, buf.vec.y, buf.size, buf.white);

        if(buf.size!=0){
            if(buf.vec.x<-8.0){
                cameraLeft();
                printf("left\n");
                last_zombie = Left;
            }else if(buf.vec.x>8.0){
                cameraRight();
                printf("right\n");
                last_zombie = Right;
            }else{
                cameraResetHorizontal();
            }
            if(buf.vec.y<-14.0){
                cameraUp();
                printf("up\n");
            }else if(buf.vec.y>14.0){
                cameraDown();
                printf("down\n");
            }else{
                cameraResetVertical();
            }
        }
        if(buf.size==0){
            cameraReset();
            moveReset();
            nowtime = time(NULL);
            if(nowtime-zerotime>1){
                if(buf.white>60&&(buf.white!=old_buf.white||buf.white>80)){
                    cameraUp();
                }else if(buf.white<40&&(buf.white!=old_buf.white||buf.white<20)){
                    cameraDown();
                }
                switch (last_zombie){
                case Left:
                    cameraLeft();
                    break;
                case Right:
                    cameraRight();
                    break;
                }
            }else{
                Sleep(1000/fps);
            }
        }else if(buf.size>550){
            //大人ゾンビ 至近距離
            zerotime=time(NULL);
            attackLeft();
            moveBack();
            moveLeft();
        }else if(buf.size>250){
            //大人ゾンビ 下がる必要なし
            zerotime=time(NULL);
            attackLeft();
            moveReset();
        }else if(buf.size>160&&buf.white>70){
            //子供ゾンビ用 下向いた状態で160以上の大きさ
            zerotime=time(NULL);
            attackLeft();
            moveReset();
        }else{
            //ゾンビ検知 遠距離
            zerotime=time(NULL);
            moveForward();
        }
        Sleep(1000/fps);
        old_buf = buf;
        buf = detectZombie();
    }
    setCreative();
    setMorning();
}
