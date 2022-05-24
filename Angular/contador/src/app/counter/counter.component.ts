import { Component } from '@angular/core';

@Component({
  selector: 'app-counter',
  templateUrl: './counter.component.html',
  styleUrls: ['./counter.component.css'],
})
export class CounterComponent {
  contador: number = 0;

  handleCount(value: number) {
    this.contador = value;
  }
}
