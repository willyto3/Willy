import { Injectable } from '@angular/core';
import { Tarea } from '../interfaces/tarea.interface';

@Injectable()
export class TareasService {
  tareas: Array<Tarea> = [
    {
      tarea: 'Barrer',
      completada: false,
    },
    {
      tarea: 'Trapear',
      completada: false,
    },
    {
      tarea: 'Cocinar',
      completada: false,
    },
    {
      tarea: 'Leer',
      completada: false,
    },
  ];

  deleteTarea(nombreTarea: String) {
    this.tareas = this.tareas.filter((tareas) => tareas.tarea !== nombreTarea);
  }

  completeTarea(nombreTarea: String) {
    const tarea: Tarea = this.tareas.find((tarea) => {
      return tarea.tarea === nombreTarea;
    })!;

    tarea.completada = !tarea.completada;
    console.log(tarea);
  }
}
