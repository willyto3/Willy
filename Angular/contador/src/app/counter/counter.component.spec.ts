import { TestBed } from '@angular/core/testing';
import { ButtonAddComponent } from './button-add/button-add.component';
import { CounterComponent } from './counter.component';

describe('CounterComponent', () => {
  // NOTE: Pruebas de HTML

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CounterComponent, ButtonAddComponent],
    }).compileComponents();
  });

  it('Se debe crear el componente Counter', () => {
    const fixture = TestBed.createComponent(CounterComponent);
    expect(fixture.componentInstance).toBeTruthy();
  });

  it('Se debe crear el texto Contador 0', () => {
    const fixture = TestBed.createComponent(CounterComponent);
    // Prueba para verificar si se renderizo el campo
    fixture.detectChanges();
    const compiled: HTMLElement = fixture.nativeElement;
    expect(compiled.querySelector('h1')?.textContent).toEqual('Contador 0');
  });

  // NOTE Pruebas Logicas
  it('valor inicial del contador es 0', () => {
    const counter = new CounterComponent();

    expect(counter.contador).toBe(0);
  });
});
