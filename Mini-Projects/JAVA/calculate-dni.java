class CalculateDni{

    String juegoCaracteres="TRWAGMYFPDXBNJZSQVHLCKE";

    public char calculate(){
        int modulo= dni % 23;
        char letra = juegoCaracteres.charAt(modulo);

         return letra;
    }

}

	public static void main(String args[]) 
	{ 

        CalculateDni example = new CalculateDni();

        System.out.println(example.CalculateDni());
	} 