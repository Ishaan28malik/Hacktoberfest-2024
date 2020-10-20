import java.util.Scanner;

class pattern {

    public static void main(String[] args) {
        int n, i, j, k, s, m, b, x = 0, y, h;
        Scanner scan = new Scanner(System.in);
        System.out.print("EnTer tHe nUmBer YoU WaNt tO dIsplaY PattErn ");
        n = scan.nextInt();
        k = 1;
        for (i = n; i > 0; i--) {
            s = n;
            b = n;
            for (j = 0; j < i; j++) {
                System.out.print(i);
            }

            for (j = 2; j < i; j++) {
                if (i == 1) {
                    System.out.print("2");
                } else
                    System.out.print(i);
            }
            b = b - x;
            for (m = 0; m < k; m++) {
                if (b == 1) {
                    b = b + 1;
                } else {
                    System.out.print(b);
                    b++;
                }
            }

            System.out.print("\n");

            for (m = 0; m < k && k < n; m++) {
                System.out.print(s);
                s--;
            }
            k++;
            x++;
        }
        y = n;
        for (i = 1; i < n; i++) {
            h = n;
            b = n;
            for (j = y - 2; j > 0; j--) {
                System.out.print(h);
                h--;
            }
            for (j = 0; j <= i; j++) {
                System.out.print(i + 1);
            }
            y--;

            for (m = 0; m < i; m++) {
                System.out.print(i + 1);
            }

            b = i + 2;
            for (m = 1; m < n - 1 && b <= n; m++) {
                System.out.print(b);
                b++;
            }

            System.out.print("\n");
        }
    }
}