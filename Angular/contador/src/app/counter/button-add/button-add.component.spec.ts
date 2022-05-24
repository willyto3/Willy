import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ButtonAddComponent } from './button-add.component';

describe('ButtonAddComponent', () => {
  let component: ButtonAddComponent;
  let fixture: ComponentFixture<ButtonAddComponent>;
  // NOTE: Pruebas de HTML

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ButtonAddComponent],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ButtonAddComponent);
    component = fixture.componentInstance;
    // Prueba para verificar si se renderizo el campo
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
  let nuevoContador = 0;

  it('Debe Emitir el valor de 1', () => {
    component.onAdd.subscribe((contador) => {
      nuevoContador = contador;
    });

    component.add();

    expect(nuevoContador).toBe(1);
  });
});
