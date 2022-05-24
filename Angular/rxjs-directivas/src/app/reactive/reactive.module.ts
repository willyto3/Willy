import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveContainerComponent } from './reactive-container/reactive-container.component';
import { AreamouseDirective } from './directives/areamouse.directive';

@NgModule({
  declarations: [ReactiveContainerComponent, AreamouseDirective],
  imports: [CommonModule],
  exports: [ReactiveContainerComponent],
})
export class ReactiveModule {}
