package sistemadist.trabalho2.soap.api;

import javax.xml.ws.Endpoint;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Trabalho2SoapApplication {

	public static void main(String[] args) {
		Endpoint.publish("http://localhost:8080/trabalho2/soap", new ServidorImpl());
		//SpringApplication.run(Trabalho2SoapApplication.class, args);
		
	}

}
