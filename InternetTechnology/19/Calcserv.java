import java.rmi.Naming;

public class Calcserv {

    Calcserv() {
        try {
            Calc c = new Calcimpl();
            Naming.rebind("rmi://localhost:1099/calcservice", c);
        } catch (Exception e) {
            System.out.println("Exception:" + e);
        }
    }

    public static void main(String arg[]) {
        new Calcserv();
    }

}