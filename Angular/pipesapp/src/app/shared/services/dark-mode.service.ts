import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class DarkModeService {
  dark: boolean = false;
  constructor() {}

  chageMode(){
    this.dark = !this.dark;
  }
}
