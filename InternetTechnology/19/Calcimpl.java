import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class Calcimpl extends UnicastRemoteObject implements Calc {

    protected Calcimpl() throws RemoteException {
        super();
    }

    public long addition(long a, long b) throws RemoteException {
        return a + b;
    }

    public long subtraction(long a, long b) throws RemoteException {
        return a - b;
    }

    public long multiplication(long a, long b) throws RemoteException {
        return a * b;
    }

    public long divition(long a, long b) throws RemoteException {
        return a / b;
    }

}