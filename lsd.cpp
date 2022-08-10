#include <opencv2/imgproc.hpp>
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>

using namespace std;
using namespace cv;

int main()
{
    bool useRefine = true;
    bool useCanny = true;
    Mat image = imread("image_0.png", IMREAD_GRAYSCALE);
    if( image.empty() )
    {
        cout << "Unable to load Image" << endl;
        return 1;
    }
    imshow("Source Image", image);

    if (useCanny)
        Canny(image, image, 50, 200, 3); 

    Ptr<LineSegmentDetector> ls = useRefine ? createLineSegmentDetector(LSD_REFINE_STD) : createLineSegmentDetector(LSD_REFINE_NONE);

    vector<Vec4f> lines_std;

    ls->detect(image, lines_std);

    // Show found lines
    if (useCanny)
        image = Scalar(0, 0, 255);

    ls->drawSegments(image, lines_std);

    imshow("result", image);
    waitKey();
    return 0;
}