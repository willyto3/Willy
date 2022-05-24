import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class PokeService {
  private baseUrl: string = 'https://pokeapi.co/api/v2/pokemon';
  constructor(private http: HttpClient) {}

  getList(page: number = 0) {
    return this.http.get(`${this.baseUrl}`, {
      params: { offset: page, limit: 16 },
    });
  }

  getPokeData(name: string) {
    return this.http.get(`${this.baseUrl}/${name}`);
  }
}
