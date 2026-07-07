import pyperclip
import time

string_to_copy ='''

import java.util.Scanner;

class BankAccount {
    private String accountNumber;
    private double balance;

    public String getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        BankAccount account = new BankAccount();

        account.setAccountNumber(sc.nextLine());
        account.setBalance(sc.nextDouble());

        System.out.println(account.getAccountNumber());
        System.out.println(account.getBalance());

        sc.close();
    }
}
'''


while True:
    pyperclip.copy(string_to_copy)
    time.sleep(1)  # Copies to clipboard every second