import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-key-value',
  templateUrl: './key-value.component.html',
  styleUrls: ['./key-value.component.css']
})
export class KeyValueComponent implements OnInit {

  persona = {
    nombre: 'Lauren',
    edad: 10,
    ocupacion: 'estudiante',
  };
  constructor() { }

  ngOnInit(): void {
  }

}
