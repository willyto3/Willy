import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoggingService {

  constructor() { }
  enviarMensajeAConsola(mensaje: string) {
    console.log(mensaje);
  }
}
