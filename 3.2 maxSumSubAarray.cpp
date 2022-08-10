/* 3.3 子数组的最大累加和问题:
  思路：如果某段累加和<0,则对后续累加无(正)贡献,需终止本段累加，重启新累加；求多伦的最大值。
  1) 累加：从左到右，累加；
  2）累加控制：
     α.累加和>0,继续累加；
     β.累加和<0,
      a、终止本轮累加；
      b、max(当前累加和最值，本次累加之前的和)
      c、重启累加：调到1），从数组当前元素，；
  4）最后一元素<0,则不计入最后一轮累加。
*/
#include <stdio.h>

int main()
{
    int N, d;
    int s = 0, m = 0;
    scanf("%d", &N);

    for (int i = 0; i < N - 1; i++)
    {
        scanf("%d", &d);
        s += d;
        if (s < 0)
        {
            s = s - d;
            m = s > m ? s : m;
            s = 0;
        }
    }
    scanf("%d", &d);
    if (d > 0)
        s += d;

    if (s > 0)
        m = s > m ? s : m;

    printf("%d", m);
}