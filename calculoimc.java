package calculoimc;

import javax.swing.JOptionPane;

public class CalculoImc {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        float peso, altura, calcImc;
        String resuPeso, respAltura;
        
        //ENTRADA DO PESO
        resuPeso = JOptionPane.showInputDialog("Digite seu peso em KG: ");
        peso = Integer.parseInt(resuPeso);
        
        //ENTRADA DA ALTURA
        respAltura = JOptionPane.showInputDialog("Digite sua altura em CM: ");
        altura = Integer.parseInt(respAltura);
        
        //CALCULO
        calcImc = peso / ((altura / 100) * (altura / 100));
        
        if (calcImc < 17){
            JOptionPane.showMessageDialog(null, String.format("O seu IMC é: %.2f", 
                    calcImc) + "\n Situação: Muito abaixo do peso");            
        }else if ((calcImc > 17) && (calcImc < 18.49)){
            JOptionPane.showMessageDialog(null, String.format("O seu IMC é: %.2f", 
                    calcImc) + "\n Situação: Abaixo do peso");        
        }else if ((calcImc > 18.50) && (calcImc < 24.99)){
            JOptionPane.showMessageDialog(null, String.format("O seu IMC é: %.2f", 
                    calcImc) + "\n Situação: Peso normal"); 
        }else if ((calcImc > 25) && (calcImc < 29.99)){
            JOptionPane.showMessageDialog(null, String.format("O seu IMC é: %.2f", 
                    calcImc) + "\n Situação: Acima do peso");
        }else if ((calcImc > 30) && (calcImc < 34.99)){
            JOptionPane.showMessageDialog(null, String.format("O seu IMC é: %.2f", 
                    calcImc) + "\n Situação: Obesidade I");
        }else if ((calcImc > 35) && (calcImc < 39.99)){
            JOptionPane.showMessageDialog(null, String.format("O seu IMC é: %.2f", 
                    calcImc) + "\n Situação: Obesidade II [severa]");
        }else{
            JOptionPane.showMessageDialog(null, String.format("O seu IMC é: %.2f", 
                    calcImc) + "\n Situação: Obesidade III [mórbida]");
        }               
    }
}