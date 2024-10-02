import java.rmi.Naming;

public class Client {
    public static void main(String[] args) {
        try {
            // Localiza o objeto remoto no registro RMI
            Hello obj = (Hello) Naming.lookup("rmi://localhost/Hello");

            // Chama o método remoto
            String message = obj.sayHello();
            System.out.println("Mensagem do servidor: " + message);
        } catch (Exception e) {
            System.out.println("Erro no cliente: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
