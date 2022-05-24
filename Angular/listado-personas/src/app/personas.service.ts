import { Injectable } from '@angular/core';
import { LoggingService } from './logging.service';
import { Persona } from './persona.model';

@Injectable({
  providedIn: 'root',
})
export class PersonasService {
  //? Arreglo Personas
  personas: Persona[] = [
    new Persona('Juan', 'Perez'),
    new Persona('Orlando', 'Corzo'),
    new Persona('Willy', 'Corzo'),
  ];

  constructor(private loggingService: LoggingService) {}

  agregarPersona(persona: Persona) {
    this.loggingService.enviarMensajeAConsola(
      'Agregamos Persona ' + persona.nombre
    );
    this.personas.push(persona);
  }
}
