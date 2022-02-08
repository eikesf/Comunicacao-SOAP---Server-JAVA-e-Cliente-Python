package sistemadist.trabalho2.soap.api;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;;


@WebService
@SOAPBinding(style = Style.RPC)
public interface InterfaceServidor {
	
	@WebMethod public String verEstadoRecurso (String recurso);
	
	@WebMethod String verUtilizadorRecurso(String recurso);
	
	@WebMethod String Feedback();
	
	@WebMethod void registrarInteresse(String recurso, String idCliente);
	
	@WebMethod void sairSC (String recurso, String idCliente);
	
	@WebMethod void grantToken(String recurso, String idCliente);

}