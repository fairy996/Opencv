/*******************************************************************************
* @FilePath     : \Opencv_Study\Z_ClassTask\task1.c
* @Author       : Yang Shuaige
* @File Version : V1.0.0
* @Create Date  : 2024-03-18 10:03:04
* @Description  : 直方图均衡化
* @Copyright (c) 2024 by Yang Shuaige, All Rights Reserved. 
********************************************************************************/

#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
//#include <opencv2/matplotlib/matplotlib/matplotlibcpp.h>  //绘图函数库，绘制图片对应直方图
#include <iostream>

using namespace cv;
int main(int argc, char *argv[])
{
    Mat image = imread("F:\\Deep Learning\\Opencv_Study\\material\\lena.jpg",0);//给定参数0读入灰度图
   //图像获取失败
    if(image.empty())
    {
        std::cout << "Could not open or find the image" << std::endl;
        return -1;
    }
    imshow("原图",image);
    //此部分代码是将BGR三种基础色分别进行均衡化的操作，通过split将图片的像素分为三维数组，然后分别进行equalizeHist操作。
    // Mat imageRGB[3];
    // split(image,imageRGB);
    // for(int i=0;i<3;i++)
    // {
    //     equalizeHist(imageRGB[i],imageRGB[i]);
    // }
    //  merge(imageRGB,3,image);
    //只进行灰度图的直方图均衡化
    equalizeHist(image,image);
    imshow("直方图均衡化",image);
    waitKey(0);
    return 0;
}