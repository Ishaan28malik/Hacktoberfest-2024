class hill 
{ 

// generates the key matrix for the key string 
static void getKeyMatrix(String key, int keyMatrix[][]) 
{ 
	int k = 0; 
	for (int i = 0; i < 3; i++) 
	{ 
		for (int j = 0; j < 3; j++) 
		{ 
			keyMatrix[i][j] = (key.charAt(k)) % 65; 
			k++; 
		} 
	} 
} 

// Following function encrypts the message 
static void encrypt(int cipherMatrix[][],int keyMatrix[][],int messageVector[][]) 
{ 
	int x, i, j; 
	for (i = 0; i < 3; i++) 
	{ 
		for (j = 0; j < 1; j++) 
		{ 
			cipherMatrix[i][j] = 0; 
		
			for (x = 0; x < 3; x++) 
			{ 
				cipherMatrix[i][j] += 
					keyMatrix[i][x] * messageVector[x][j]; 
			} 
		
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26; 
		} 
	} 
} 

// Function to implement Hill Cipher 
static void HillCipher(String message, String key) 
{ 
	int [][]keyMatrix = new int[3][3]; 
	getKeyMatrix(key, keyMatrix); 

	int [][]messageVector = new int[3][1]; 

	// Generate vector for the message 
	for (int i = 0; i < 3; i++) 
		messageVector[i][0] = (message.charAt(i)) % 65; 

	int [][]cipherMatrix = new int[3][1]; 

	//generates encrypted vector 
	encrypt(cipherMatrix, keyMatrix, messageVector); 

	String CipherText=""; 

	// Generate the encrypted text from the encrypted vector 
	for (int i = 0; i < 3; i++) 
		{CipherText += (char)(cipherMatrix[i][0] + 65);} 

	//print the ciphertext 
	System.out.print(" Ciphertext:" + CipherText); 
} 

public static void main(String[] args) 
{ 
	String message = "Hacktoberfest"; 

	String key = "HYANCKUKP"; 

	HillCipher(message, key); 
	} 
} 

