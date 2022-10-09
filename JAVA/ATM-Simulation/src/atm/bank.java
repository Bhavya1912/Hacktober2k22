/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package atm;

import java.util.ArrayList;

/**
 *
 * @author Administrator
 */
public class bank {

    private static final bank bankO = new bank();

    private double balance = 1000;
    ArrayList<String> transactions = new ArrayList<>(20);

    public static bank getInstance() {
        return bankO;

    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void deposite(double balance, int added) {
        this.balance = balance + added;
        transactions.add("you added " + added + " to your balance \n");

    }

    private bank() {
    }

    public void withdrawl(double balance, int number) {
        if (balance > 0) {
            double newbalance = balance - number;
            transactions.add(" you withdrew " + number + " from your balance \n");
            setBalance(newbalance);
        }
    }

    public void transfer(double balance, int number, int userid) {
        this.balance = balance - number;
        transactions.add("you transferred " + number + " from your balance,\n to " + userid);
    }

}
