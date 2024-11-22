namespace App {

  class Carro{
    public string marca;
    public string modelo;
    private int ano;
    public bool automatico = false;
    private string cor; 

    public string GetCor(){
      get{return cor;}
      set{cor = value;}
    }

    public int GetAno(){
      return ano;
    }

    public void SetAno(int ano){
      ano = novoAno;
    }
  
    public void Ligar(){
      Console.WriteLine("O carro está ligado!");
    }
    
    private void Acelerar(float velocidade){
      console.WriteLine("O carro está acelerando a {0} km/h", velocidade);
    }
    
    public void Desligar(){
      Console.WriteLine("O carro está desligado!");
    }
    
}
