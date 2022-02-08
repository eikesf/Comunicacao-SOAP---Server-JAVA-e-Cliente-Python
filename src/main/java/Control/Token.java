package Control;

public class Token {

	String recurso;
	String utilizador;
	
	public Token(String recurso,String utilizador) {
		this.recurso = recurso;
		this.utilizador = utilizador;
	}
	
	public String getRecurso() {
		return recurso;
	}
	
	public String getUtilizador() {
		return utilizador;
	}
	
	public void setUtilizador(String utilizador) {
		this.utilizador = utilizador;
	}
}
