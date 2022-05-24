import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { CalculoComponent } from './calculo/calculo.component';
import { ResultadoComponent } from './resultado/resultado.component';

@NgModule({
  declarations: [AppComponent, CalculoComponent, ResultadoComponent],
  imports: [BrowserModule, FormsModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
