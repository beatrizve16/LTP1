class Contabancaria{
  private string titular;
  private int numeroConta;
  protected float saldo;
  
public Contabancaria(string titular, int numeroConta){
  this.titular = titular;
  this.numeroConta = numeroConta;
  this.saldo = 0;
}

  public virtual void VerificarSaldo(){
    Console.WriteLine("Conta indisponível");
  }
}

class ContaCorrente : Contabancaria {
  public ContaCorrente(string titular, int numeroConta) : base(titular, numeroConta){ 
  }

  public override void VerificarSaldo(){
    Console.WriteLine($"Saldo: {this.saldo}");
  }
}
