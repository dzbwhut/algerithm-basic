#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;
#define BYTE    unsigned char 
#define INT16   short
#define BILINE //双线性插值

#pragma pack(2)
typedef struct __ST_PIXLCODE
{
	char snIndexImage; // if through fusion, the second image's index is snIndexImage + 1;
	//float sgWeight1;//左图像素亮度所占权重
	unsigned char sgWeight1;//左图像素亮度所占权重
	INT16 snX1; //左图横坐标
	INT16 snY1; //左图纵坐标
	INT16 snX2; //右图横坐标
	INT16 snY2; //右图纵坐标

#ifdef BILINE //双线性插值
	#ifdef SGLE_ORIGIN_MODE
        float wgtDL1[4];//左图双线性插值的4个权重
        float wgtDL2[4];//右图双线性插值的4个权重
    #else
        BYTE wgtDL1[4];//左图双线性插值的4个权重
        BYTE wgtDL2[4];//右图双线性插值的4个权重
    #endif
#endif
	// 灰度比值
} ST_PIXLCODE, *LPST_PIXLCODE;
#pragma pack()
int snWCanvas,snHCanvas;
//计算重叠区域左、右位置
int overlappedRegion[7][2];
LPST_PIXLCODE m_stPixlBook;

typedef struct __point{
    int x;
    int y;
}POINT_ST,*LP_POINT_ST;

void params_transform(int a[2][3], POINT_ST p[6])
{
    cout<<"\t"<<"x"<<"\t"<<"y"<<endl;
    for(int i=0;i<6;i++)  
        cout<<"\t"<<p[i].x<<"\t"<<p[i].y<<endl;

    cout<<"\t"<<"x"<<"\t"<<"y"<<endl;
    for(int i=0;i<2;i++){
        for(int j=0;i<3;i++)
            cout<<"\t"<<a[i];
        cout<<endl;
    }
}

void test_param_array()
{
    int *a[3]=(int *) malloc(6*sizeof(int));
    LP_POINT_ST p=(LP_POINT_ST) malloc(6*sizeof(POINT_ST));

    for(int i=0;i<6;i++)
    {
        a[i]=i;
        p[i].x=i*2;
        p[i].y=p[i].x+1;
    }
    params_transform(a, p);
}
int main(int argn, char *argv[])
{
    //cout<<"C + +"<<endl;
    test_param_array();
    return 1;
    // 以写模式打开文件
    char * fname="F:\\82A\\82A-R2.02-V150\\Release\\data_input\\interpolation_table_01.dat";
    FILE *fp_weight=fopen(fname,"r");
    int m_snSizePanorama[2];
    m_stPixlBook =(LPST_PIXLCODE)malloc(sizeof(ST_PIXLCODE)*snHCanvas*snWCanvas);
    memset((char *)m_stPixlBook, 0, sizeof(ST_PIXLCODE)*snHCanvas*snWCanvas);    
    
    fread(&m_snSizePanorama[0], sizeof(int),2,fp_weight);
    snWCanvas = m_snSizePanorama[0];
    snHCanvas = m_snSizePanorama[1];    
    fread((void *)m_stPixlBook, 1, sizeof(ST_PIXLCODE)*snWCanvas * snHCanvas,fp_weight);
    fread((void *)overlappedRegion, 1, sizeof(int)*7 * 2, fp_weight);
    fclose(fp_weight);

    return 0;
}