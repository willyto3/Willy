import { Component, OnDestroy, OnInit } from '@angular/core';
import { fromEvent, Subscription } from 'rxjs';

@Component({
  selector: 'app-reactive-container',
  templateUrl: './reactive-container.component.html',
  styleUrls: ['./reactive-container.component.css'],
})
export class ReactiveContainerComponent implements OnInit, OnDestroy {
  suscriptor: Subscription | null = null;
  x: number = 0;
  y: number = 0;

  ngOnInit() {
    const obs = fromEvent<MouseEvent>(
      document.querySelector('#area')!,
      'mousemove'
    );

    this.suscriptor = obs.subscribe((ev) => {
      console.log('evento');
      this.x = ev.clientX;
      this.y = ev.clientY;
    });
  }
  ngOnDestroy() {
    console.log('Se cerro el evento');
    this.suscriptor!.unsubscribe();
  }

  /**
    miIntervalo: Observable<number> = interval(1000).pipe(
      map((value) => value + 1),
      take(10),
      filter((value) => value % 2 === 0)
    );
    constructor() {}

    miSubscription: Subscription | null = null;

    /**let numero = 0;
        const miObservable = new Observable<number>((observer) => {
          setInterval(() => {
            numero++;
            observer.next(numero);
            observer.complete();
            if (numero == 3) {
              observer.error('Número Erroneo');
            }
          }, 3000);
        });

        miObservable.subscribe({
          next: (result) => {
            console.log(result);
          },
          error: (error) => {
            console.error(error);
          },
          complete: () => {
            console.log('Observable Completado');
          },
        });
      }

    ngOnInit(): void {
      this.miSubscription = this.miIntervalo.subscribe({
        next: (value) => console.log(value),
        complete: () => console.log('Estos son los primeros 5 numeros pares'),
      });
    }

    ngOnDestroy(): void {
      this.miSubscription!.unsubscribe();
      console.log('Componente Destruido');
    }
  */
}
