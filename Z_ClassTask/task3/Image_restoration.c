#include <opencv2/opencv.hpp>
using namespace cv;

// 定义全局变量，image用于存储原图，inpaintMask用于存储绘制的遮罩
Mat image;
Mat inpaintMask;


// 鼠标回调函数
void onMouse(int event, int x, int y, int flags, void *userdata)
{
    // 定义用于记录上一个点位置的局部变量
    static Point prevPt(-1,-1);

    if (event == EVENT_LBUTTONUP || !(flags & EVENT_FLAG_LBUTTON)) 
        prevPt = Point(-1, -1); // 鼠标松开，重置prevPt
    else if (event == EVENT_LBUTTONDOWN)
        prevPt = Point(x, y); // 更新prevPt为新的点击位置
    else if (event == EVENT_MOUSEMOVE && (flags & EVENT_FLAG_LBUTTON)) 
    {
        Point pt(x, y); // 获取当前鼠标位置
        // 绘制白色圆圈到mask上，半径为5（对于本张图片来说，更容易复原）
        circle(inpaintMask, pt, 5, Scalar::all(255), -1);
        // 显示mask,掩模图像
        imshow("inpaintMask", inpaintMask);
        // 定义result用于存储修复后的图像
        Mat result;
        // 图像修复及保存
        inpaint(image, inpaintMask, result, 1, INPAINT_NS);
        imshow("result", result);
        imwrite("F:/Deep Learning/
        Opencv_Study/Z_ClassTask/task3/image/result_image.jpg", result);
    } 
}

// 主函数
int main(void)
{
    // 读入原始图像
    image = imread("F:/Deep Learning/Opencv_Study/
    Z_ClassTask/task3/image/target_Img.png");
    // 创建同大小的mask，初始化为全0，类型为8位无符号整数
    inpaintMask = Mat::zeros(image.size(), CV_8U);

    // 创建名为'image'的窗口
    namedWindow("image", WINDOW_AUTOSIZE);
    // 设置窗口的鼠标回调
    setMouseCallback("image", onMouse, 0);

    // 显示原始图像
    imshow("image", image);
    // 等待按键事件
    waitKey(0);
    return 0;
}
