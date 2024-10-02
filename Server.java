import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public  class Server {
    public static void main(String[] args) {
        try {
            // Cria e exporta o objeto remoto
            HelloImpl obj = new HelloImpl();

            // Cria o registro na porta 1099
            LocateRegistry.createRegistry(1099);

            // Publica o objeto remoto no registro RMI com o nome "Hello"
            Naming.rebind("Hello", obj);

            System.out.println("Servidor RMI pronto.");
        } catch (Exception e) {
            System.out.println("Erro no servidor: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
