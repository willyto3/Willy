import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-calculo',
  templateUrl: './calculo.component.html',
  styleUrls: ['./calculo.component.css'],
})
export class CalculoComponent {
  operandoA: number;
  operandoB: number;

  @Output() resultadoSuma = new EventEmitter<number>();

  sumar(): void {
    let resultado = this.operandoA + this.operandoB;
    this.resultadoSuma.emit(resultado)

}
}
