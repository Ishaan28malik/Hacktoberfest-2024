import java.net.UnknownHostException;
import java.net.InetAddress;
import java.net.NetworkInterface;

public class Mac_Address {
    public static void main(String[] args) throws UnknownHostException {
        InetAddress ip;
        InetAddress addr = InetAddress.getLocalHost();
        try {
            String hostname = addr.getHostName();
            System.out.println("Host Name : " + hostname);

            ip = InetAddress.getLocalHost();
            System.out.println("Current IP address : " + ip.getHostAddress());

            NetworkInterface network = NetworkInterface.getByInetAddress(ip);

            byte[] mac = network.getHardwareAddress();

            System.out.print("Current MAC address : ");

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < mac.length; i++) {
                sb.append(String.format("%02X%s", mac[i], (i < mac.length - 1) ? "-" : ""));
            }
            System.out.println(sb.toString());

        } catch (Exception e) {

            e.printStackTrace();

        }

    }
}



