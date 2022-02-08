package sistemadist.trabalho2.soap.api;

import javax.jws.WebService;
import Model.Recurso;
import Control.Token;

@WebService(endpointInterface = "sistemadist.trabalho2.soap.api.InterfaceServidor")
public class ServidorImpl  implements InterfaceServidor{

	public ServidorImpl () {}
	
	Recurso recurso1 = new Recurso("Released");
	Recurso recurso2 = new Recurso("Released");
	Token tk1 = new Token("Recurso1","None");
	Token tk2 = new Token("Recurso2","None");
	
	String feedback;
	
		@Override
		public void registrarInteresse(String recurso, String idCliente) {
		
			if("Recurso1".equals(recurso)) {
				System.out.println("### RECURSO 1  ###");
				if(recurso1.fila.isEmpty() && "Released".equals(recurso1.getEstado())) {
					grantToken(recurso,idCliente);
				}
				else {
					recurso1.fila.add(idCliente);
					System.out.println("Cliente "+idCliente+" foi adicionado a fila para consumir o "+recurso);
				}
			
			}
		
			else if ("Recurso2".equals(recurso)){
				System.out.println("### RECURSO 2 ###");
				if(recurso2.fila.isEmpty() && "Released".equals(recurso2.getEstado())) { 
					grantToken(recurso,idCliente);
				}
				else {
					recurso2.fila.add(idCliente);
					System.out.println("Cliente "+idCliente+" foi adicionado a fila para consumir o "+recurso);
					}
			}
	    }
		@Override
		public void grantToken(String recurso, String idCliente) {
			
			if("Recurso1".equals(recurso)){
				tk1.setUtilizador(idCliente);
				recurso1.setEstado("Held");
				System.out.println("Recurso "+recurso+" → "+verEstadoRecurso(recurso));
				System.out.println("Recurso "+recurso+" → "+verUtilizadorRecurso(recurso));
			}
			else{
				tk2.setUtilizador(idCliente);
				recurso2.setEstado("Held");
				System.out.println("Recurso "+recurso+" → "+verEstadoRecurso(recurso));
				System.out.println("Recurso "+recurso+" → "+verUtilizadorRecurso(recurso));
			}
			
			feedback = "SEÇÃO CRÍTICA >> Token do "+recurso+" concedido para cliente: "+idCliente;
			System.out.println(feedback);
		}
		
		@Override
		public void sairSC(String recurso, String idCliente){
			
			if("Recurso1".equals(recurso) && idCliente.equals(verUtilizadorRecurso(recurso))){
				recurso1.setEstado("Released");
				tk1.setUtilizador("None");
				feedback = "Token LIBERADO do "+recurso+"pelo cliente: "+idCliente;
				System.out.println("Recurso "+recurso+" → "+verEstadoRecurso(recurso));
				Feedback();
				
				if((!recurso1.fila.isEmpty()) && "Released".equals(recurso1.getEstado())) {
					idCliente = recurso1.fila.poll();
					System.out.println("saiu da fila recurso1");
					}
			}
			
			else if ("Recurso2".equals(recurso) && idCliente.equals(verUtilizadorRecurso(recurso))){
				recurso2.setEstado("Released");
				tk2.setUtilizador("None");
				feedback = "Token LIBERADO do "+recurso+"pelo cliente: "+idCliente;
				System.out.println("Recurso "+recurso+" → "+verEstadoRecurso(recurso));
				Feedback();
				
				if((!recurso2.fila.isEmpty()) && "Released".equals(recurso2.getEstado())) {
					idCliente = recurso2.fila.poll();
					System.out.println("saiu da fila recurso2");
					}
			}
			
			else {
				System.out.println("Você não pode liberar o recurso em que não possue o token");
			}
		}
		@Override
		public String verEstadoRecurso(String recurso){
			String estado;
			
			if("Recurso1".equals(recurso)) {
				estado = recurso1.getEstado();
				}
			else {
				estado = recurso2.getEstado();
			}
			return estado;
		}
		@Override
		public String verUtilizadorRecurso(String recurso){
			String utilizador;
			
			if("Recurso1".equals(recurso)) {
				utilizador = tk1.getUtilizador();
				}
			else {
				utilizador = tk2.getUtilizador();
			}
			return utilizador;
		}
		@Override
		public String Feedback(){
			return feedback;
		}
		
		
}