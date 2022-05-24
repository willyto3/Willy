import { Component, OnDestroy, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'rxjs-directivas';

  visible = true;

  setVisible() {
    this.visible = !this.visible;
  }

  ngOnInit(): void {
    this.title = 'Entro al OnInit';
    throw new Error('Method not implemented.');
  }
  ngOnDestroy(){
    this.title = 'Componente eliminado';
  }
}
