import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AboutModule } from './about/about.module';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ContactoModule } from './contacto/contacto.module';
import { ProyectosModule } from './proyectos/proyectos.module';
import { ShareModule } from './shared/components/share.module';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ShareModule
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
