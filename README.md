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
