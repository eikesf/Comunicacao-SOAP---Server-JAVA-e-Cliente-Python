package Model;

import java.util.LinkedList;
import java.util.Queue;

public class Recurso {

	String estado;
	public Queue<String> fila = new LinkedList<>();
	
	public Recurso(String estado) {
		this.estado = estado;
	}
	
	public String getEstado() {
		return estado;
	}
	
	public void setEstado(String estado) {
		this.estado = estado;
	}
	
	public Queue<String> getFila(){
		return fila;
		}
	}