import javax.swing.JOptionPane;

public class MRU {
    public static void main(String[] args) {
        String velocidadStr, tiempoStr;
        double velocidad, tiempo, distancia;
    
        velocidadStr = JOptionPane.showInputDialog("Ingrese la velocidad constante (m/s):");
        velocidad = Double.parseDouble(velocidadStr);

        tiempoStr = JOptionPane.showInputDialog("Ingrese el tiempo (s):");
        tiempo = Double.parseDouble(tiempoStr);

        distancia = velocidad * tiempo;

        JOptionPane.showMessageDialog(null, "La distancia recorrida es: " + distancia + " metros");
    }
}
