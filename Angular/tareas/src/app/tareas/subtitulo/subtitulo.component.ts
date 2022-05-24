import { Component } from '@angular/core';
import { TareasService } from '../services/tareas.service';

@Component({
  selector: 'app-subtitulo',
  templateUrl: './subtitulo.component.html',
})
export class SubtituloComponent {
  constructor(private tareasService: TareasService){}

  get getTareas(){
    return this.tareasService.tareas.length
  }
}
