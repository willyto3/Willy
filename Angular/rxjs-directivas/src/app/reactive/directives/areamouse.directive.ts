import { Directive, ElementRef, OnInit, Input } from '@angular/core';

@Directive({
  selector: '[areaMouse]',
})
export class AreamouseDirective implements OnInit {

  @Input()
  color = 'green';

  @Input()
  height = '100';

  constructor(private el: ElementRef<HTMLDivElement>) {}
  ngOnInit() {
    this.setBackGround();
    this.setHeight();
  }

  setBackGround() {
    this.el.nativeElement.style.backgroundColor = this.color;
  }
  setHeight() {
    this.el.nativeElement.style.height = `${this.height}px`;
  }
}
