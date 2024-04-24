#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <vector>
#include <iostream>

using namespace cv;
using namespace std;
void compressImage(string inputPath, string outputPath, int compressionRatio, int ImwriteFlags)
{

    // 读取图像

    Mat image = imread(inputPath);

    // 压缩图像

    if (!image.empty())
    {
        vector<int> compression_params; // vector为一个能够存放各种数据类型的数组

        // IMWRITE_JPEG_QUALITY：JPEG压缩质量，取值范围为0-100，数值越大表示质量越高。 IMWRITE_JPEG_QUALITY        = 1
        // IMWRITE_PNG_COMPRESSION：PNG压缩级别，取值范围为0-9，数值越大表示压缩率越高。IMWRITE_PNG_COMPRESSION     = 16
        // IMWRITE_WEBP_QUALITY：WEBP压缩质量，取值范围为0-100，数值越大表示质量越高。IMWRITE_WEBP_QUALITY        = 64,
        compression_params.push_back(ImwriteFlags);
        compression_params.push_back(compressionRatio);

        // 保存压缩后的图像
        imwrite(outputPath , image, compression_params); // 此时compression_paras为一个类似于结构体的作用
        
    }
    else
    {
        cout << "Error: Failed to read image from " << inputPath << endl;
    }
}

int main()
{
    char Input_path_jpg[] = "F:/Deep Learning/Opencv_Study/Z_ClassTask/task2/Input/lena.jpg";
    char Input_path_png[] = "F:/Deep Learning/Opencv_Study/Z_ClassTask/task2/Input/AM.png";
    char Output_path_jpg_min[] = "F:/Deep Learning/Opencv_Study/Z_ClassTask/task2/output/image_jpg_qualitymin";
    char Output_path_jpg_max[] = "F:/Deep Learning/Opencv_Study/Z_ClassTask/task2/output/image_jpg_qualitymax";
    char Output_path_png_min[] = "F:/Deep Learning/Opencv_Study/Z_ClassTask/task2/output/image_png_qualitymin";
    char Output_path_png_max[] = "F:/Deep Learning/Opencv_Study/Z_ClassTask/task2/output/image_png_qualitymax";
    // jpg_min  jpg用三种方式压缩，最大压缩程度（画质最差）
    compressImage(Input_path_jpg, Output_path_jpg_min, 0, 1);
    compressImage(Input_path_jpg, Output_path_jpg_min, 9, 16);
    compressImage(Input_path_jpg, Output_path_jpg_min,0, 64);
    // jpg_max jpg用三种方式压缩，最小压缩程度（画质最好）
    compressImage(Input_path_jpg, Output_path_jpg_min, 0, 1);
    compressImage(Input_path_jpg, Output_path_jpg_min, 9, 16);
    compressImage(Input_path_jpg, Output_path_jpg_min, 0, 64);
    // png_min png用三种方式压缩，最大压缩程度（画质最差）
    compressImage(Input_path_png, Output_path_png_min, 0, 1);
    compressImage(Input_path_png, Output_path_png_min, 9, 16);
    compressImage(Input_path_png, Output_path_png_min, 0, 64);
    // png_max png用三种方式压缩，最小压缩程度（画质最好）
    compressImage(Input_path_png, Output_path_png_max, 0, 1);
    compressImage(Input_path_png, Output_path_png_max, 9, 16);
    compressImage(Input_path_png, Output_path_png_max, 0, 64);
    return 0;
}

int main()
{
    // 定义输入路径和相应的输出路径
    struct ImagePath
    {
        const char *inputPath;      // 输入图像的路径
        const char *outputBasePath; // 输出图像的基本路径
    };
    // 初始化图像路径数组
    ImagePath paths[] = {
        {"F:/Deep Learning/Opencv_Study/Z_ClassTask/task2/Input/lena.jpg", 
        "F:/Deep Learning/Opencv_Study/Z_ClassTask/task2/output/image_jpg_quality"}, // jpg图像的输入路径和处理结果输出路径
        {"F:/Deep Learning/Opencv_Study/Z_ClassTask/task2/Input/AM.png", 
        "F:/Deep Learning/Opencv_Study/Z_ClassTask/task2/output/image_png_quality"}    // png图像的输入路径和处理结果输出路径
    };
    // 定义压缩设置
    struct CompressionSetting
    {
        int compressionRatio; // 压缩比率
        int imwriteFlag;      // 指定图像格式的标志（例如JPEG、PNG）
        const char *suffix;   // 输出文件的后缀名，用于区分不同的压缩设置
    };

    // 初始化压缩设置数组
    CompressionSetting settings[] = {
        {0, 1, "min.jpg"},    // JPEG格式，最低质量
        {100, 1, "max.jpg"},  // JPEG格式，最低质量
        {9, 16, "min.png"},   // PNG格式，最低质量
        {0, 16, "max.png"},   // PNG格式，最高质量
        {0, 64, "min.webp"},  // WEBP格式，最低质量
        {100, 64, "max.webp"} // WEBP格式，最高质量
    };

    // 遍历每个图像路径
    for (const auto &path : paths)
    {
        // 遍历每个压缩设置
        for (const auto &setting : settings)
        {
            // 构造输出路径
            string outputPath = string(path.outputBasePath) + "_" + setting.suffix;

            // 调用compressImage函数进行图像压缩
            compressImage(path.inputPath, outputPath, setting.compressionRatio, setting.imwriteFlag);
        }
    }

    return 0;
}