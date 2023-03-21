#Eén van de oudste vormen van encryptie werd naar verluid gebruikt door Julius
#Caesar. Hij wilde instructies sturen naar zijn generaals, zonder dat zijn vijanden de
#boodschap zouden kunnen ontcijferen mocht ze in hun handen belanden. Hiervoor
#werd het zgn Caesarcijfer ontwikkeld (https://nl.wikipedia.org/wiki/Caesarcijfer). Het
#idee erachter is eenvoudig: elke letter in de originele boodschap wordt verschoven
#met 3 plaatsen: A wordt D, B wordt E, C wordt F enz.
#De drie laatste letters van het alfabet mappen terug op de beginletters. Niet-letter
#karakters worden niet aangepast. Schrijf een programma die de encryptie uitvoert.
#Laat de gebruiker toe de boodschap in te geven, alsook het getal dat dient te worden
#opgeschoven (hierboven was dat 3). Zorg ervoor dat je programma zowel kleine als
#grote letters encodeert. Je programma moet ook negatieve shifts ondersteunen,
#zodat het programma ook kan gebruikt worden om de boodschap te ontcijferen.
#Tip:
#https://www.w3schools.com/python/ref_func_ord.asp
#https://www.w3schools.com/python/ref_func_chr.asp

import java.util.Scanner;

public class CaesarCipher {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a message: ");
        String message = input.nextLine();
        System.out.print("Enter a shift: ");
        int shift = input.nextInt();
        String encrypted = encrypt(message, shift);
        System.out.println("Encrypted message: " + encrypted);
        String decrypted = decrypt(encrypted, shift);
        System.out.println("Decrypted message: " + decrypted);
    }

    public static String encrypt(String message, int shift) {
        StringBuilder encrypted = new StringBuilder();
        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    c = (char) ('a' + (c - 'a' + shift) % 26);
                } else {
                    c = (char) ('A' + (c - 'A' + shift) % 26);
                }
            }
            encrypted.append(c);
        }
        return encrypted.toString();
    }

    public static String decrypt(String message, int shift) {
        return encrypt(message, -shift);
    }
}
