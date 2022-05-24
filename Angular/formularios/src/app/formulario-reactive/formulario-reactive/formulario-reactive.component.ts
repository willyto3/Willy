import { Component, OnInit } from '@angular/core';
import {
  FormArray,
  FormBuilder,
  FormControl,
  FormGroup,
  Validators,
} from '@angular/forms';

@Component({
  selector: 'app-formulario-reactive',
  templateUrl: './formulario-reactive.component.html',
  styleUrls: ['./formulario-reactive.component.css'],
})
export class FormularioReactiveComponent implements OnInit {
  miFormularioR: FormGroup = this.fb.group({
    proyecto: this.fb.control('', [
      Validators.required,
      Validators.minLength(3),
      Validators.maxLength(15),
    ]),
    horas: this.fb.control('', [
      Validators.required,
      Validators.min(1),
      Validators.max(50),
    ]),
    tecnologias: this.fb.array([]),
  });

  tecnologia: FormControl = this.fb.control('', [
    Validators.required,
    Validators.minLength(3),
    Validators.maxLength(20),
  ]);

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {}

  proyectos: any[] = [];

  get getTecnologias() {
    return this.miFormularioR.get('tecnologias') as FormArray;
  }

  validar() {
    return this.miFormularioR.invalid && this.miFormularioR.touched;
  }

  agregarTecnologia() {
    if (this.tecnologia.invalid) {
      this.miFormularioR.markAllAsTouched();
      return;
    }

    this.getTecnologias.push(this.fb.control(this.tecnologia.value));
    this.tecnologia.reset();
  }

  agregarProyecto() {
    if (this.miFormularioR.invalid) {
      this.miFormularioR.markAllAsTouched();
      return;
    }
    this.proyectos.push(this.miFormularioR.value);
    this.miFormularioR.reset();
    this.getTecnologias.clear();
  }
}
