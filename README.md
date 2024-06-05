https://github.com/SatrioAjiTI/UAS_RPLBO_71200538_D.git



class Mobile Banking "dikembangkan lagiii"

package com.ug9.eTransactionProject;

public class MobileBanking extends DigitalPayment{
    private String noRekening;
    private boolean checkFee = false;

    public MobileBanking(String nama, long saldo, String s) {
        super(nama, saldo);
        this.noRekening = s;
    }

    @Override
    public void transfer(DigitalPayment digitalPayment, long l) {
        super.transfer(digitalPayment, l);
        if (l < 0){
            System.out.println("input tidak valid!");
        } else if (this.getSaldo() < l) {
            System.out.println("gagal di proses!");
        }else {
            setCheckFee(true);
            digitalPayment.setSaldo(digitalPayment.getSaldo() + l);
            this.setSaldo(this.getSaldo() - l);
        }
    }

    public String getNoRekening() {
        return noRekening;
    }

    public void setNoRekening(String noRekening) {
        this.noRekening = noRekening;
    }

    public boolean isCheckFee() {
        return checkFee;
    }

    public void setCheckFee(boolean checkFee) {
        this.checkFee = checkFee;
    }
}


CLASS MOBILEWALLET:

package com.ug9.eTransactionProject;

//import sun.security.jca.GetInstance;

public class MobileWallet extends DigitalPayment{
    private long feeTransferBank = 6000;
    private String noHp;

    public MobileWallet(String nama, long saldo, String s) {
        super(nama, saldo);
        this.noHp = s;
    }

    @Override
    public void transfer(DigitalPayment digitalPayment, long l) {
        super.transfer(digitalPayment, l);
        if(l < 0){
            System.out.println("Nominal yang Anda input tidak valid!");
        } else if (this.getSaldo() < l) {
            System.out.println("Transfer gagal! Saldo Anda tidak mencukupi.");
        }else{
            if (digitalPayment instanceof BNImo || digitalPayment instanceof BRImo){
                digitalPayment.setSaldo(digitalPayment.getSaldo() + l);
                this.setSaldo(this.getSaldo() - l - feeTransferBank);
                digitalPayment.printBuktiTranfer(digitalPayment, l);
            }else {
                digitalPayment.setSaldo(digitalPayment.getSaldo() + l);
                this.setSaldo(this.getSaldo() - l);
                digitalPayment.printBuktiTranfer(digitalPayment, l);
            }
        }
    }

    public long getFeeTransferBank() {
        return feeTransferBank;
    }

    public void setFeeTransferBank(long feeTransferBank) {
        this.feeTransferBank = feeTransferBank;
    }

    public String getNoHp() {
        return noHp;
    }

    public void setNoHp(String noHp) {
        this.noHp = noHp;
    }
}

