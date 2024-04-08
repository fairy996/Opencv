/*******************************************************************************
* @FilePath     : \Opencv_Study\Z_ClassTask\task1.c
* @Author       : Yang Shuaige
* @File Version : V1.0.0
* @Create Date  : 2024-03-18 10:03:04
* @Description  : ֱ��ͼ���⻯
* @Copyright (c) 2024 by Yang Shuaige, All Rights Reserved. 
********************************************************************************/

#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
//#include <opencv2/matplotlib/matplotlib/matplotlibcpp.h>  //��ͼ�����⣬����ͼƬ��Ӧֱ��ͼ
#include <iostream>

using namespace cv;
int main(int argc, char *argv[])
{
    Mat image = imread("F:\\Deep Learning\\Opencv_Study\\material\\lena.jpg",0);//��������0����Ҷ�ͼ
   //ͼ���ȡʧ��
    if(image.empty())
    {
        std::cout << "Could not open or find the image" << std::endl;
        return -1;
    }
    imshow("ԭͼ",image);
    //�˲��ִ����ǽ�BGR���ֻ���ɫ�ֱ���о��⻯�Ĳ�����ͨ��split��ͼƬ�����ط�Ϊ��ά���飬Ȼ��ֱ����equalizeHist������
    // Mat imageRGB[3];
    // split(image,imageRGB);
    // for(int i=0;i<3;i++)
    // {
    //     equalizeHist(imageRGB[i],imageRGB[i]);
    // }
    //  merge(imageRGB,3,image);
    //ֻ���лҶ�ͼ��ֱ��ͼ���⻯
    equalizeHist(image,image);
    imshow("ֱ��ͼ���⻯",image);
    waitKey(0);
    return 0;
}