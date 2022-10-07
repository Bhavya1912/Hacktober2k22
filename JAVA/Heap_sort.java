package Assignment9;

import java.util.*;

public class HeapSort {
    public static void main(String a[])
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];

        for (int j = 0; j < n; j++) {
            arr[j] = sc.nextInt();
        }
        for(int i=arr.length; i>1; i--)
        {
            heapSort(arr, i-1);
        }
        System.out.println(Arrays.toString(arr));
    }
    public static void heapSort(int n[], int n_ubound)
    {
        int i, o;
        int lChild, rChild, mChild, root, temp;
        root=(n_ubound-1)/2;
        for(o=root;o>=0;o--)
        {
            for(i=root;i>=0;i--)
            {
                lChild=(2*i)+1;
                rChild=(2*i)+2;
                if((lChild<=n_ubound) && (rChild <= n_ubound))
                {
                    if(n[rChild]>=n[lChild])
                        mChild=rChild;
                    else
                        mChild=lChild;
                }
                else
                {
                    if(rChild>n_ubound)
                        mChild=lChild;
                    else
                        mChild=rChild;
                }
                if(n[i]<n[mChild])
                {
                    temp=n[i];
                    n[i]=n[mChild];
                    n[mChild]=temp;
                }
            }
        }
        temp=n[0];
        n[0]=n[n_ubound];
        n[n_ubound] = temp;
    }
}
