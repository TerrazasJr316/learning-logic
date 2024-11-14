import javax.swing.JOptionPane;

public class promedioEstudiantil {
    public static void main(String[] args) {
        double suma = 0;
        int totalNotas = 3;

        for (int i = 1; i <= totalNotas; i++) {
            try {
                String notaStr = JOptionPane.showInputDialog("Ingrese la nota " + i + ":");
                double nota = Double.parseDouble(notaStr);
                suma += nota; // Sumar la nota al total
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Por favor ingrese un valor numérico válido para la nota " + i);
                i--; 
            }
        }

        double promedio = suma / totalNotas;

        JOptionPane.showMessageDialog(null, "El promedio es: " + promedio);
    }
}

